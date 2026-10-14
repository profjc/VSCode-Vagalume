#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# INVENTARIO DE RECURSOS — curso Vaga Lume (Moodle 4.5)
# Base do relatorio de estimativa de carga horaria (ver docs/relatorios/carga-horaria/).
#
# Uso:
#   python3 scripts/inventario-recursos.py
#
# Saidas (padrao):
#   docs/relatorios/carga-horaria/inventario-recursos.csv   (uma linha por pagina)
#   docs/relatorios/carga-horaria/inventario-recursos.md    (leitura humana + totais)
#
# Inventaria, por pagina: palavras visiveis, imagens (marcadores), videos (embedados,
# instruidos e trechos), atividades H5P (com o no de itens lidos do content.json do
# pacote), forum, links externos e PDF associado. Tambem lista os itens das paginas de
# Referencias Bibliograficas e cruza os videos citados com os videos ja usados no curso.
#
# NAO altera nenhum arquivo do curso: apenas le templates/ e assets/ e escreve os
# dois relatorios em docs/relatorios/carga-horaria/.

import argparse, csv, json, os, re, unicodedata, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, 'templates', 'pages')
H5P = os.path.join(ROOT, 'assets', 'h5p')
PDF = os.path.join(ROOT, 'assets', 'pdf')
OUT = os.path.join(ROOT, 'docs', 'relatorios', 'carga-horaria')
MODULOS = {'Boas-vindas': 'M0', 'M1': 'M1', 'M2': 'M2', 'M3': 'M3', 'M4': 'M4',
           'Encontros-sincronos': 'ENC'}
REF_PAGINAS = ['M1/Parte5/M1P5P2.html', 'M2/Parte6/M2P6P2.html',
               'M3/Parte5/M3P5P2.html', 'M4/Parte4/M4P4P2.html']
IGNORAR = ('base/', 'labels/', 'frontpage/')

# Duracoes reais de videos externos (verificadas em 14/10/2026 via oEmbed + lengthSeconds)
DUR_EXTERNAS = {
    'olFTlBgnzGA': 72,     # FMCSV — 5 dicas para gestantes de primeira viagem
    'NVRm2tjoeqw': 268,    # FMCSV — Mudancas Fisicas e Emocionais na Gestante
    'TmNf3cDnM1Q': 224,    # FMCSV — Gestacao, Pre-Natal e Saude do Bebe
    'KrMfedDRUhw': 140,    # ChildFund Brasil — O que e Parentalidade
    'dIyr6srurC0': 5805,   # Sesc SP — SESC Ideias (video completo; no curso usa-se um trecho)
}

RE_COM = re.compile(r'<!--.*?-->', re.S)
RE_BLQ = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.S | re.I)
RE_DUR = re.compile(r'^(?:(\d{1,2})h)?(?:(\d{1,3})min)?(?:(\d{1,3})(?:s|seg))?$')
RE_HHMM = re.compile(r'\b(\d{1,2}):(\d{2})\b')


def texto(html):
    """Texto visivel de um trecho de HTML (sem comentarios, tags, script/style)."""
    t = RE_COM.sub(' ', html)
    t = RE_BLQ.sub(' ', t)
    t = re.sub(r'<br\s*/?>', ' ', t)
    t = re.sub(r'</(p|li|div|h[1-6]|tr|td)>', ' ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'&nbsp;|&amp;|&[a-z]+;', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def palavras(txt):
    return len(re.findall(r'[A-Za-z\u00c0-\u00ff0-9]+', txt))


def seg_de(s):
    """'22min07s' | '1h26min36seg' | '48s' -> segundos (None se nao for duracao)."""
    m = RE_DUR.match(s.strip())
    if not m or not any(m.groups()):
        return None
    h, mi, se = (int(g) if g else 0 for g in m.groups())
    return h * 3600 + mi * 60 + se


def dur_parenteses(trecho):
    """Ultima duracao entre parenteses de uma legenda de creditos."""
    achado = ('', None)
    for s in re.findall(r'\(([^)]*)\)', trecho):
        v = seg_de(s)
        if v is not None:
            achado = (s.strip(), v)
    return achado


def hhmm(s):
    m = RE_HHMM.match(s)
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


def fmt(seg):
    if not seg:
        return '-'
    h, r = divmod(seg, 3600)
    mi, se = divmod(r, 60)
    if h:
        return '%dh%02dmin%02ds' % (h, mi, se)
    return '%dmin%02ds' % (mi, se) if mi else '%ds' % se


def canal_de(credito):
    m = re.search(r'canal:\s*([^)]*)$', credito)
    return m.group(1).strip() if m else ''


def titulo_de(credito):
    return re.sub(r'\s*\([^)]*\)\s*;.*$', '', credito).strip()


def tipo_pagina(html):
    if 'Referências Bibliográficas' in html:
        return 'referencias'
    if 'Fórum:' in html:
        return 'forum'
    if 'Síntese do Módulo' in html or 'O que aprendemos no Módulo' in html:
        return 'sintese'
    if 'Apresentação do Módulo' in html:
        return 'abertura'
    return 'conteudo'


def videos(html):
    """Videos citados na pagina: embedado / instruido / instruido-trecho / sugerido."""
    achados = []
    for m in re.finditer(r'youtube\.com/embed/([A-Za-z0-9_-]+)', html):
        vid = m.group(1)
        cauda = html[m.end():m.end() + 1500]
        cred = re.search(r'<p class="small text-muted[^>]*>(.*?)</p>', cauda, re.S)
        credito = texto(cred.group(1)) if cred else ''
        d, s = dur_parenteses(credito)
        achados.append({'id': vid, 'tipo': 'embedado', 'seg': s, 'dur': d or '-',
                        'canal': canal_de(credito), 'titulo': titulo_de(credito)})
    for m in re.finditer(r'youtube\.com/watch\?v=([A-Za-z0-9_-]+)|youtu\.be/([A-Za-z0-9_-]+)', html):
        vid = m.group(1) or m.group(2)
        ini = html.rfind('<p', 0, m.start())
        ini = ini if ini != -1 else max(0, m.start() - 600)
        fim = html.find('</p>', m.end())
        fim = fim if fim != -1 else m.end() + 600
        ctx = texto(html[ini:fim])
        trecho = re.search(r'(\d{1,2}:\d{2})[^0-9]{1,25}(\d{1,2}:\d{2})', ctx)
        if trecho:
            a, b = hhmm(trecho.group(1)), hhmm(trecho.group(2))
            seg = (b - a) if (a is not None and b is not None and b > a) else None
            tipo, obs = 'instruido-trecho', 'trecho %s-%s' % (trecho.group(1), trecho.group(2))
        elif re.search(r'quer saber mais', ctx, re.I):
            tipo, seg, obs = 'sugerido', DUR_EXTERNAS.get(vid), 'sugestao complementar'
        else:
            tipo, seg, obs = 'instruido', DUR_EXTERNAS.get(vid), 'instruido na pagina'
        achados.append({'id': vid, 'tipo': tipo, 'seg': seg, 'dur': fmt(seg),
                        'canal': '', 'titulo': ctx[:90], 'obs': obs})
    return achados


# ---------- H5P ----------
TIPOS_H5P = [('question-set', 'Question Set'), ('question_set', 'Question Set'),
             ('multipla_escolha_multiplas', 'Multipla escolha (varias corretas)'),
             ('multipla_escolha', 'Multipla escolha'), ('VouF', 'Verdadeiro ou falso'),
             ('verdadeiro_falso', 'Verdadeiro ou falso'), ('associacao', 'Associacao'),
             ('Arrastar_palavras', 'Arrastar palavras'), ('DragDrop', 'Arrastar e soltar'),
             ('virar_cartoes', 'Virar cartoes'), ('caca-palavras', 'Caca-palavras'),
             ('Quiz', 'Quiz (question set)'), ('Desafio', 'Desafio de palavras')]


def tipo_h5p(nome):
    for chave, rotulo in TIPOS_H5P:
        if chave.lower() in nome.lower():
            return rotulo
    return 'H5P'


def h5p_itens(caminho):
    """(chave lida, quantidade) dos itens/questoes de um pacote .h5p."""
    try:
        with zipfile.ZipFile(caminho) as z:
            nomes = [n for n in z.namelist() if n.endswith('content/content.json')]
            if not nomes:
                return 'sem content.json', None
            d = json.loads(z.read(nomes[0]).decode('utf-8', 'replace'))
    except Exception:
        return 'erro de leitura', None
    if not isinstance(d, dict):
        return 'estrutura inesperada', None
    for chave in ('questions', 'cards', 'dialogs', 'answers', 'choices', 'pairs',
                  'steps', 'blanks', 'words'):
        v = d.get(chave)
        if isinstance(v, list) and v:
            return chave, len(v)
    q = d.get('question')
    if isinstance(q, dict):
        tarefa = q.get('task') if isinstance(q.get('task'), dict) else q
        for sub in ('dropZones', 'elements'):
            v = tarefa.get(sub)
            if isinstance(v, list) and v:
                return 'question.' + sub, len(v)
    v = d.get('wordList')
    if isinstance(v, str) and v.strip():
        return 'wordList', len([x for x in re.split(r'[,;]', v) if x.strip()])
    v = d.get('textField')
    if isinstance(v, str):
        n = len(re.findall(r'\*[^*]+\*', v))
        if n:
            return 'textField', n
    return 'nao identificado', None


def catalogo_h5p():
    cat = {}
    for raiz, _, arqs in os.walk(H5P):
        for a in sorted(arqs):
            if a.endswith('.h5p'):
                cam = os.path.join(raiz, a)
                chave, n = h5p_itens(cam)
                cat[a] = {'tipo': tipo_h5p(a), 'chave': chave, 'itens': n,
                          'kb': round(os.path.getsize(cam) / 1024.0, 1), 'paginas': []}
    return cat


# ---------- Referencias bibliograficas ----------
STOP = {'para', 'the', 'com', 'dos', 'das', 'uma', 'que', 'por', 'sobre', 'disponivel',
        'youtube', 'canal', 'nos', 'de', 'da', 'do', 'os', 'as', 'um', 'no', 'na'}


def tokens(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return set(w for w in re.findall(r'[a-z0-9]+', s) if len(w) >= 4 and w not in STOP)


def refs_itens(html):
    itens, secao = [], ''
    for m in re.finditer(r'<h[234][^>]*>(.*?)</h[234]>|<p([^>]*)>(.*?)</p>', html, re.S):
        if m.group(1) is not None:
            secao = texto(m.group(1))
            continue
        corpo = m.group(3)
        t = texto(corpo)
        if len(t) < 12:
            continue
        st = re.search(r'<strong>(.*?)</strong>', corpo, re.S)
        itens.append({'secao': secao, 'texto': t,
                      'titulo': texto(st.group(1)) if st else '',
                      'canal': t.split('.')[0].strip(),
                      'link': bool(re.search(r'<a\s', corpo)), 'match': None})
    return itens


def cruzar(itens, cat_videos):
    for it in itens:
        if 'YouTube' not in it['texto'] and 'youtu' not in it['texto']:
            continue
        alvo, canal = tokens(it['titulo'] or it['texto']), tokens(it['canal'])
        melhor, score = None, 0.0
        for v in cat_videos:
            st = len(alvo & tokens(v['titulo'])) / max(1, len(alvo))
            b = tokens(v['canal'])
            sc = (len(canal & b) / max(1, min(len(canal), len(b)))) if (canal and b) else 0.0
            if (st >= 0.6 or (st >= 0.3 and sc >= 0.6)) and (st + sc) > score:
                melhor, score = v, st + sc
        it['match'] = melhor
    return itens


# ---------- Varredura ----------
def varrer():
    linhas, fora, avisos = [], [], []
    cat_h5p, cat_vid, refs = catalogo_h5p(), {}, {}
    for raiz, _, arqs in os.walk(PAGES):
        for a in sorted(arqs):
            if not a.endswith('.html'):
                continue
            cam = os.path.join(raiz, a)
            rel = os.path.relpath(cam, PAGES).replace(os.sep, '/')
            html = open(cam, encoding='utf-8').read()
            mod = rel.split('/')[0]
            if rel.startswith(IGNORAR):
                fora.append(rel)
                continue
            vs = videos(html)
            ativ = [f.strip() for f in re.findall(r'\[ARQUIVO_H5P:\s*(.+?\.h5p)\]', html)]
            for f in ativ:
                if f in cat_h5p:
                    cat_h5p[f]['paginas'].append(rel)
                else:
                    avisos.append('H5P citado e nao encontrado em assets/h5p/: %s (%s)' % (f, rel))
            for v in vs:
                vv = cat_vid.setdefault(v['id'], {'id': v['id'], 'titulo': v['titulo'],
                                                  'canal': v['canal'], 'seg': v['seg'],
                                                  'tipos': set(), 'paginas': []})
                vv['tipos'].add(v['tipo'])
                vv['paginas'].append(rel)
                if vv['seg'] is None:
                    vv['seg'] = v['seg']
            partes = re.search(r'Parte(\d+)', rel)
            licao = re.search(r'Licao(\d+)', rel)
            forum = re.search(r'<span class="vagalume-destaque">\s*Fórum:\s*(.*?)</span>', html, re.S)
            pdf = os.path.join(PDF, mod, a.replace('.html', '.pdf'))
            linhas.append({
                'arquivo': rel, 'modulo': MODULOS.get(mod, mod),
                'parte': partes.group(1) if partes else '',
                'licao': licao.group(1) if licao else '',
                'tipo_pagina': tipo_pagina(html),
                'palavras': palavras(texto(html)),
                'imagens': len(re.findall(r'cole a imagem aqui', html)),
                'imagens_bloco_temp': len(re.findall(r'APAGAR ESTE BLOCO', html)),
                'videos_embedados': sum(1 for v in vs if v['tipo'] == 'embedado'),
                'videos_instruidos': sum(1 for v in vs if v['tipo'].startswith('instruido')),
                'videos_sugeridos': sum(1 for v in vs if v['tipo'] == 'sugerido'),
                'video_segundos': sum(v['seg'] or 0 for v in vs if v['tipo'] != 'sugerido'),
                'h5p_atividades': len(ativ),
                'h5p_itens': sum((cat_h5p[f]['itens'] or 0) for f in ativ if f in cat_h5p),
                'forum': texto(forum.group(1)) if forum else '',
                'links_externos': len(re.findall(r'target="_blank"', html)),
                'pdf': 'sim' if os.path.exists(pdf) else '',
            })
    for f, dados in sorted(cat_h5p.items()):
        if not dados['paginas']:
            avisos.append('Pacote .h5p sem pagina vinculada (nao entra no curso): %s' % f)
    for v in cat_vid.values():
        v['tipos'] = '/'.join(sorted(v['tipos']))
    for rel in REF_PAGINAS:
        cam = os.path.join(PAGES, rel)
        if os.path.exists(cam):
            refs[rel] = cruzar(refs_itens(open(cam, encoding='utf-8').read()),
                               sorted(cat_vid.values(), key=lambda x: x['id']))
    return linhas, fora, avisos, cat_h5p, cat_vid, refs


# ---------- Saidas ----------
CAMPOS = ['arquivo', 'modulo', 'parte', 'licao', 'tipo_pagina', 'palavras', 'imagens',
          'imagens_bloco_temp', 'videos_embedados', 'videos_instruidos', 'videos_sugeridos',
          'video_segundos', 'h5p_atividades', 'h5p_itens', 'forum', 'links_externos', 'pdf']
SOMA = ['palavras', 'imagens', 'imagens_bloco_temp', 'videos_embedados', 'videos_instruidos',
        'videos_sugeridos', 'video_segundos', 'h5p_atividades', 'h5p_itens']


def resumo_por_modulo(linhas):
    ordem = ['M0', 'M1', 'M2', 'M3', 'M4', 'ENC']
    r = {}
    for l in linhas:
        d = r.setdefault(l['modulo'], dict(paginas=0, foruns=0, pdfs=0))
        for k in SOMA:
            d[k] = d.get(k, 0) + l[k]
        d['paginas'] += 1
        d['foruns'] += 1 if l['forum'] else 0
        d['pdfs'] += 1 if l['pdf'] else 0
    saida = [(m, r[m]) for m in ordem if m in r]
    saida += [(m, r[m]) for m in sorted(r) if m not in ordem]
    return saida


def escrever_md(cam, linhas, fora, avisos, cat_h5p, cat_vid, refs):
    import datetime
    A = []
    A.append('# Inventário de recursos — curso Vaga Lume')
    A.append('')
    A.append('> Gerado automaticamente por `scripts/inventario-recursos.py` em %s.'
             % datetime.date.today().strftime('%d/%m/%Y'))
    A.append('> Escopo: módulos produzidos e validados no Moodle (M0 Boas-vindas, M1, M2, M3, M4) '
             'e a página dos Encontros Síncronos. Este arquivo é a base quantitativa do relatório '
             'de carga horária — método e parâmetros em `PLANO-carga-horaria.md`.')
    A.append('')
    A.append('## 1. Resumo por módulo')
    A.append('')
    A.append('| Módulo | Páginas | Palavras | Imagens | Vídeos (emb./instr.) | Vídeo (tempo) | H5P | Itens H5P | Fóruns | PDFs |')
    A.append('|---|---|---|---|---|---|---|---|---|---|')
    tot = dict(paginas=0, foruns=0, pdfs=0)
    for k in SOMA:
        tot[k] = 0
    for mod, d in resumo_por_modulo(linhas):
        A.append('| %s | %d | %d | %d | %d/%d | %s | %d | %d | %d | %d |' % (
            mod, d['paginas'], d['palavras'], d['imagens'], d['videos_embedados'],
            d['videos_instruidos'], fmt(d['video_segundos']), d['h5p_atividades'],
            d['h5p_itens'], d['foruns'], d['pdfs']))
        tot['paginas'] += d['paginas']
        tot['foruns'] += d['foruns']
        tot['pdfs'] += d['pdfs']
        for k in SOMA:
            tot[k] += d[k]
    A.append('| **TOTAL** | **%d** | **%d** | **%d** | **%d/%d** | **%s** | **%d** | **%d** | **%d** | **%d** |' % (
        tot['paginas'], tot['palavras'], tot['imagens'], tot['videos_embedados'],
        tot['videos_instruidos'], fmt(tot['video_segundos']), tot['h5p_atividades'],
        tot['h5p_itens'], tot['foruns'], tot['pdfs']))
    A.append('')
    A.append('> **Notas de contagem:** "Vídeos (emb./instr.)" = vídeos embedados (iframe) + vídeos '
             'instruídos por link na página/fórum (entram no tempo efetivo). Vídeos **sugeridos** '
             '("Quer saber mais?", bibliografia) são registrados na seção 4 e **não** entram no tempo '
             'efetivo. "Imagens" = marcadores `[cole a imagem aqui]`; `imagens_bloco_temp` no CSV são '
             'os blocos temporários a apagar. "Itens H5P" = questões/itens lidos do `content.json`. '
             'A linha **ENC** é a página dos Encontros Síncronos: seus 2 vídeos são as **gravações** '
             'dos encontros (carga **opcional**; não entram no tempo efetivo dos módulos).')
    A.append('')
    A.append('## 2. Distribuição das páginas por tipo')
    A.append('')
    tipos = {}
    for l in linhas:
        tipos.setdefault(l['tipo_pagina'], [0, 0])
        tipos[l['tipo_pagina']][0] += 1
        tipos[l['tipo_pagina']][1] += l['palavras']
    A.append('| Tipo de página | Páginas | Palavras |')
    A.append('|---|---|---|')
    for t in sorted(tipos, key=lambda x: -tipos[x][0]):
        A.append('| %s | %d | %d |' % (t, tipos[t][0], tipos[t][1]))
    A.append('')
    A.append('## 3. Atividades H5P (por pacote)')
    A.append('')
    A.append('| Pacote | Tipo | Itens/questões | Lido de | Página(s) no curso |')
    A.append('|---|---|---|---|---|')
    for f, d in sorted(cat_h5p.items()):
        A.append('| %s | %s | %s | %s | %s |' % (
            f, d['tipo'], d['itens'] if d['itens'] is not None else 'n/d', d['chave'],
            ', '.join(d['paginas']) if d['paginas'] else '**ÓRFÃO (sem página)**'))
    A.append('')
    A.append('## 4. Vídeos do curso')
    A.append('')
    A.append('| ID | Como entra | Duração | Canal | Título (crédito/contexto) | Página(s) |')
    A.append('|---|---|---|---|---|---|')
    for v in sorted(cat_vid.values(), key=lambda x: (x['tipos'], x['id'])):
        A.append('| %s | %s | %s | %s | %s | %s |' % (
            v['id'], v['tipos'], fmt(v['seg']), v['canal'] or '-', v['titulo'][:70],
            ', '.join(sorted(set(v['paginas'])))))
    A.append('')
    A.append('## 5. Fóruns do curso')
    A.append('')
    A.append('| Módulo | Página | Título no HTML |')
    A.append('|---|---|---|')
    for l in linhas:
        if l['forum']:
            A.append('| %s | %s | %s |' % (l['modulo'], l['arquivo'], l['forum']))
    A.append('')
    A.append('## 6. Referências bibliográficas (carga opcional)')
    A.append('')
    A.append('| Página | Itens | Itens de vídeo | Itens com link externo |')
    A.append('|---|---|---|---|')
    for rel, itens in refs.items():
        A.append('| %s | %d | %d | %d |' % (rel, len(itens),
                 sum(1 for i in itens if 'YouTube' in i['texto']),
                 sum(1 for i in itens if i['link'])))
    A.append('')
    A.append('### Itens de vídeo das Referências — cruzamento com os vídeos do curso')
    A.append('')
    A.append('| Módulo | Canal / autor | Título | Situação |')
    A.append('|---|---|---|---|')
    for rel, itens in refs.items():
        mod = MODULOS.get(rel.split('/')[0], rel.split('/')[0])
        for i in itens:
            if 'YouTube' not in i['texto']:
                continue
            if i['match']:
                m = i['match']
                locais = ', '.join(sorted(set(m['paginas'])))
                if 'embedado' in m['tipos'] or 'instruido' in m['tipos']:
                    situacao = 'já contado no tempo efetivo — `%s` (%s) em %s' % (
                        m['id'], fmt(m['seg']), locais)
                else:
                    situacao = ('presente no curso como **sugestão** ("Quer saber mais?") em %s '
                                '— não contabilizada no tempo efetivo' % locais)
            else:
                situacao = 'não localizado no curso — **sugestão** da bibliografia'
            A.append('| %s | %s | %s | %s |' % (mod, i['canal'][:34], i['titulo'][:60], situacao))
    A.append('')
    A.append('## 7. Fora do conteúdo (interface e navegação)')
    A.append('')
    A.append('%d arquivos: %s' % (len(fora), ', '.join(fora)))
    A.append('')
    A.append('## 8. Avisos e pendências de inventário')
    A.append('')
    for av in avisos:
        A.append('- %s' % av)
    A.append('')
    A.append('## 9. Como reprocessar')
    A.append('')
    A.append('```bash')
    A.append('python3 scripts/inventario-recursos.py')
    A.append('```')
    A.append('')
    A.append('Ao chegar o **Módulo de Encerramento** (Certificação e Avaliação do curso), rodar de '
             'novo: as páginas novas entram automaticamente (§8 do `PLANO-carga-horaria.md`).')
    A.append('')
    open(cam, 'w', encoding='utf-8').write('\n'.join(A) + '\n')



def escrever_csv(cam, linhas):
    with open(cam, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS, delimiter=';')
        w.writeheader()
        for l in linhas:
            w.writerow(l)


def main():
    ap = argparse.ArgumentParser(description='Inventario de recursos do curso Vaga Lume.')
    ap.add_argument('--csv', default=os.path.join(OUT, 'inventario-recursos.csv'))
    ap.add_argument('--md', default=os.path.join(OUT, 'inventario-recursos.md'))
    args = ap.parse_args()
    for cam in (args.csv, args.md):
        pasta = os.path.dirname(cam)
        if pasta and not os.path.isdir(pasta):
            os.makedirs(pasta)
    linhas, fora, avisos, cat_h5p, cat_vid, refs = varrer()
    escrever_csv(args.csv, linhas)
    escrever_md(args.md, linhas, fora, avisos, cat_h5p, cat_vid, refs)
    print('Inventario gerado:')
    print('  %s (%d paginas)' % (args.csv, len(linhas)))
    print('  %s' % args.md)
    print('')
    print('%-6s %8s %9s %8s %8s %11s %6s %8s %6s' % (
        'mod', 'paginas', 'palavras', 'imagens', 'videos', 'video', 'h5p', 'itens', 'foruns'))
    for mod, d in resumo_por_modulo(linhas):
        print('%-6s %8d %9d %8d %8d %11s %6d %8d %6d' % (
            mod, d['paginas'], d['palavras'], d['imagens'],
            d['videos_embedados'] + d['videos_instruidos'], fmt(d['video_segundos']),
            d['h5p_atividades'], d['h5p_itens'], d['foruns']))
    if avisos:
        print('')
        print('AVISOS (%d):' % len(avisos))
        for av in avisos:
            print('  - ' + av)


if __name__ == '__main__':
    main()




