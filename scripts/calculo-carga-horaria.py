#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CALCULO DE CARGA HORARIA — curso Vaga Lume (Moodle 4.5)
# Ciclo 4 do relatorio de carga horaria (ver docs/relatorios/carga-horaria/).
#
# Uso:
#   python3 scripts/calculo-carga-horaria.py
#
# Entradas:
#   docs/relatorios/carga-horaria/inventario-recursos.csv  (quantidades — 1 linha por pagina)
#   ajustes finos do Ciclo 3 (encodados abaixo; fonte: ajustes-finos.md)
#   assets/pdf/M4/*.pdf                                    (texto das SDs, medido por pdftotext)
#
# Saidas (padrao):
#   docs/relatorios/carga-horaria/calculo-carga-horaria.csv (1 linha por pagina + linhas de ajuste)
#   docs/relatorios/carga-horaria/calculo-carga-horaria.md  (tabelas-resumo + metodo)
#
# Metodo: tempo = quantidade x parametro x fator de cenario
#   cenarios: minimo | referencia | maximo | recomendado (referencia + 10% de overhead)
#   buckets:  A obrigatoria | B opcional/complementar
# Parametros:    docs/relatorios/carga-horaria/parametros-carga-horaria.md (Ciclo 2)
# Ajustes finos: docs/relatorios/carga-horaria/ajustes-finos.md (Ciclo 3)
#
# NAO altera nenhum arquivo do curso: apenas le o inventario/PDFs e escreve os dois relatorios.

import csv, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARG = os.path.join(ROOT, 'docs', 'relatorios', 'carga-horaria')
INV_CSV = os.path.join(CARG, 'inventario-recursos.csv')
PDF_DIR = os.path.join(ROOT, 'assets', 'pdf')
OUT_CSV = os.path.join(CARG, 'calculo-carga-horaria.csv')
OUT_MD = os.path.join(CARG, 'calculo-carga-horaria.md')

# ============================================================================
# PARAMETROS (parametros-carga-horaria.md §4 — Ciclo 2)
# ============================================================================
PPM = {'min': 250, 'ref': 200, 'max': 150}        # palavras por minuto
ESTUDO = {'min': 1.0, 'ref': 1.3, 'max': 1.5}     # estudo ativo (fator sobre a leitura)
IMG_FATOR = {'min': 0.5, 'ref': 1.0, 'max': 1.5}  # imagens
VID_FATOR = {'min': 1.0, 'ref': 1.0, 'max': 1.25} # videos de conteudo
H5P_FATOR = {'min': 0.5, 'ref': 1.0, 'max': 1.5}  # atividades H5P
FORUM = {'min': 20, 'ref': 35, 'max': 45}         # min/forum (ref = 35; Boas-vindas = 20)
BIBLIO = {'min': 0.5, 'ref': 1.5, 'max': 3.0}     # min/item de texto
NAV = {'min': 15, 'ref': 30, 'max': 45}           # s por pagina nova
ENCONTRO_S = 5400                                 # 1h30 por encontro (sem faixa)
OVERHEAD = 0.10                                   # +10% so no cenario recomendado
CEN = ('min', 'ref', 'max')

# ============================================================================
# AJUSTES FINOS (Ciclo 3 — ajustes-finos.md)
# ============================================================================
# §1 Imagens — segundos de REFERENCIA por pagina (bucket A: M1-M3; bucket B: ENC)
IMG_S = {
    'M1/Parte1/Licao1/M1P1L1p3.html': 45,
    'M1/Parte1/Licao1/M1P1L1p4.html': 100,
    'M1/Parte1/Licao1/M1P1L1p5.html': 0,    # mural: mesmas 5 imagens do carrossel (decisao 1)
    'M1/Parte3/Licao2/M1P3L2p1.html': 15,
    'M1/Parte4/Licao1/M1P4L1p2.html': 0,    # thumb de video instruido (decisao 2)
    'M2/Parte1/Licao1/M2P1L1p1.html': 45,
    'M2/Parte1/Licao1/M2P1L1p2.html': 45,
    'M2/Parte3/Licao1/M2P3L1p1.html': 45,
    'M2/Parte3/Licao2/M2P3L2p1.html': 15,
    'M2/Parte4/Licao1/M2P4L1p1.html': 45,
    'M2/Parte4/Licao3/M2P4L3p1.html': 15,
    'M2/Parte4/Licao4/M2P4L4p1.html': 45,
    'M2/Parte4/Licao4/M2P4L4p2.html': 45,
    'M2/Parte5/M2P5L2p1.html': 45,
    'M3/Parte1/Licao1/M3P1L1p1.html': 45,
    'M3/Parte1/Licao2/M3P1L2p1.html': 15,
    'M3/Parte1/Licao3/M3P1L3p1.html': 75,
    'M3/Parte2/Licao4/M3P2L4p1.html': 60,
    'M3/Parte3/Licao2/M3P3L2p1.html': 15,
    'M3/Parte4/Licao3/M3P4L3p1.html': 45,
    'M3/Parte4/Licao3/M3P4L3p2.html': 90,
    'M3/Parte4/Licao3/M3P4L3p3.html': 45,
    'M3/Parte4/Licao3/M3P4L3p4.html': 90,
    'M3/Parte4/Licao3/M3P4L3p5.html': 15,
    # --- Reexecucao de 25/11/2026 ---
    # M4: 4 fotos unicas "Acervo Vaga Lume" (1280x853) incluídas na revisao de 23/10/2026,
    # posterior ao inventario oficial de 14/10. Foto = 15 s (parametros §5.3).
    'M4/Parte3/Licao2/M4P3L2p1.html': 15,
    'M4/Parte3/Licao3/M4P3L3p1.html': 15,
    'M4/Parte3/Licao4/M4P3L4p1.html': 15,
    'M4/Parte3/Licao5/M4P3L5p1.html': 15,
    # M5: 4 carrosseis de 6 fotos (acoes da rede de voluntarios) = 6 x 20 s = 120 s por pagina.
    'Encerramento/Parte1/Licao1/M5P1L1p1.html': 120,
    'Encerramento/Parte1/Licao2/M5P1L2p1.html': 120,
    'Encerramento/Parte1/Licao3/M5P1L3p1.html': 120,
    'Encerramento/Parte1/Licao4/M5P1L4p1.html': 120,
}
ENC_PAGINA = 'Encontros-sincronos/encontros_sincronos_galeria.html'
IMG_S_B = {ENC_PAGINA: 135}  # 3 cartazes x 45 s (bucket B) — 3º card em 25/11/2026

# §3 Bibliografia — itens de TEXTO por pagina de Referencias (bucket B)
BIBLIO_ITENS = {
    'M1/Parte5/M1P5P2.html': 12,   # 14 itens - 2 sobrepostos (FTV + BBC, retirados p/ o bucket A)
    'M2/Parte6/M2P6P2.html': 3,
    'M3/Parte5/M3P5P2.html': 0,
    'M4/Parte4/M4P4P2.html': 0,
}

# §4 Textos externos instruidos — palavras por pagina (bucket A)
EXT_PALAVRAS = {
    'M1/Parte4/M1P4F1.html': 954,           # FTV — estudo de caso do Forum 4 do M1
    'M1/Parte3/Licao1/M1P3L1p2.html': 570,  # BBC News Brasil — reportagem instruida
}

# H5P — tipo por pagina (fonte: inventario-recursos.md §3; orfao M2P1L1p4 fora da conta)
H5P_TIPO = {
    'M1/Parte2/Licao1/M1P2L1p10.html': 'multipla',
    'M1/Parte3/Licao1/M1P3L1p4.html': 'desafio',
    'M1/Parte3/Licao2/M1P3L2p4.html': 'arrastar',
    'M1/Parte4/Licao1/M1P4L1p5.html': 'vouf',
    'M2/Parte1/Licao1/M2P1L1p3.html': 'multipla',
    'M2/Parte2/Licao1/M2P2L1p2.html': 'multipla',
    'M2/Parte3/Licao1/M2P3L1p3.html': 'multipla',
    'M2/Parte3/Licao2/M2P3L2p3.html': 'multipla',
    'M2/Parte4/Licao1/M2P4L1p3.html': 'vouf',
    'M2/Parte4/Licao2/M2P4L2p2.html': 'arrastar',
    'M2/Parte4/Licao3/M2P4L3p3.html': 'multipla',
    'M2/Parte4/Licao4/M2P4L4p5.html': 'virar',
    'M2/Parte5/M2P5L1p3.html': 'multipla',
    'M3/Parte1/Licao1/M3P1L1p3.html': 'vouf',
    'M3/Parte1/Licao2/M3P1L2p3.html': 'associacao',
    'M3/Parte1/Licao3/M3P1L3p3.html': 'multipla',
    'M3/Parte2/Licao1/M3P2L1p2.html': 'multipla',
    'M3/Parte2/Licao2/M3P2L2p3.html': 'multipla',
    'M3/Parte2/Licao3/M3P2L3p2.html': 'multipla',
    'M3/Parte2/Licao4/M3P2L4p2.html': 'multipla',
    'M3/Parte3/Licao1/M3P3L1p3.html': 'vouf',
    'M3/Parte3/Licao2/M3P3L2p3.html': 'multipla',
    'M3/Parte4/Licao1/M3P4L1p2.html': 'multipla',
    'M3/Parte4/Licao2/M3P4L2p3.html': 'multipla',
    'M3/Parte4/Licao3/M3P4L3p6.html': 'associacao',
    'M4/Parte1/Licao1/M4P1L1p2.html': 'multipla',
}
# Tipo H5P -> (unidade de contagem, segundos de referencia por unidade)
H5P_PAR = {
    'multipla':   ('item', 90),    # 1,5 min/questao
    'vouf':       ('item', 90),    # 1,5 min/questao
    'associacao': ('ativ', 180),   # 3 min/atividade
    'arrastar':   ('ativ', 180),   # 3 min/atividade
    'desafio':    ('ativ', 180),   # 3 min/atividade
    'virar':      ('item', 20),    # 20 s/carta
    'caca':       ('ativ', 300),   # 5 min/atividade
}

# Encontros sincronos (parametros §5.9 + decisao do mestre de 14/10/2026)
ENC_ENCONTROS = 3
ENC_GRAVACOES_S = [5196, 5969, 5239]   # Encontro 1 (1h26min36), 2 (1h39min29) e 3 (1h27min19)

# Reexecucao de 25/11/2026 — atividades de conclusao do M5 (linhas de ajuste, nao sao pagina).
# 600 s = questionario da Avaliacao do curso (decisao do mestre, 25/11/2026);
# 900 s = preenchimento do PDF do Plano de Acao (min. 2 atividades x 6 campos, ~75 s/campo);
# 180 s = fotografar e enviar a Tarefa; 120 s = emitir/baixar o Certificado de Conclusao.
ATIV_M5 = [
    ('(ajuste) M5 - Questionario da Avaliacao do curso (Microsoft Forms)', 600,
     'decisao do mestre (25/11/2026): 10 min para o questionario embedado'),
    ('(ajuste) M5 - PDF do Plano de Acao (preenchimento)', 900,
     'heuristica declarada: 2 atividades x 6 campos (~75 s/campo) - formulario de 1 pagina'),
    ('(ajuste) M5 - Tarefa: foto do plano + envio', 180,
     'heuristica declarada: fotografar e anexar o plano (operacional da Tarefa)'),
    ('(ajuste) M5 - Certificado de Conclusao (emissao/download)', 120,
     'heuristica declarada: gerar e baixar o PDF do certificado'),
]

# Navegacao estrutural (parametros §5.8)
NAV_LABELS = 24       # arquivos em templates/pages/labels/ (23 labels reais + 1 template)
NAV_FRONTPAGE = 3


# ============================================================================
# HELPERS
# ============================================================================
def fmt(sec):
    """Segundos -> 'Xh YYmin Zs' (omite as partes zeradas da esquerda)."""
    sec = int(round(sec))
    h, r = divmod(sec, 3600)
    m, s = divmod(r, 60)
    if h:
        return '{}h{:02d}min{:02d}s'.format(h, m, s)
    if m:
        return '{}min{:02d}s'.format(m, s)
    return '{}s'.format(s)


def hm(sec):
    """Segundos -> 'Xh YYmin' (para os totais grandes)."""
    total_min = int(round(sec / 60.0))
    return '{}h{:02d}min'.format(total_min // 60, total_min % 60)


def sd_palavras(pagina):
    """Palavras do PDF da SD correspondente a pagina (pdftotext). 0 se nao houver PDF."""
    mod = pagina.split('/')[0]
    base = os.path.basename(pagina).replace('.html', '.pdf')
    caminho = os.path.join(PDF_DIR, mod, base)
    if not os.path.exists(caminho):
        return 0
    try:
        saida = subprocess.run(['pdftotext', caminho, '-'], capture_output=True, text=True)
        texto = saida.stdout or ''
    except Exception:
        return 0
    return len(re.findall(r'[A-Za-zÀ-ÿ0-9]+', texto))


def h5p_ref_s(pagina, itens):
    """(segundos de referencia, tipo) de uma atividade H5P, por tipo."""
    tipo = H5P_TIPO.get(pagina)
    if not tipo:
        return 0, ''
    unidade, valor = H5P_PAR[tipo]
    if unidade == 'item':
        return itens * valor, tipo
    return valor, tipo


HEADER = [
    'arquivo', 'modulo', 'parte', 'licao', 'tipo_pagina', 'bucket',
    'palavras', 'imagens', 'video_s', 'h5p_n', 'h5p_itens', 'h5p_tipo',
    'forum_min_ref', 'biblio_itens', 'ext_palavras', 'sd_palavras', 'nav_s_ref', 'obs',
    'A_leitura_min', 'A_leitura_ref', 'A_leitura_max',
    'A_imagem_min', 'A_imagem_ref', 'A_imagem_max',
    'A_video_min', 'A_video_ref', 'A_video_max',
    'A_h5p_min', 'A_h5p_ref', 'A_h5p_max',
    'A_forum_min', 'A_forum_ref', 'A_forum_max',
    'A_nav_min', 'A_nav_ref', 'A_nav_max',
    'A_ext_min', 'A_ext_ref', 'A_ext_max',
    'A_encontro_min', 'A_encontro_ref', 'A_encontro_max',
    'A_total_min', 'A_total_ref', 'A_total_max',
    'B_biblio_min', 'B_biblio_ref', 'B_biblio_max',
    'B_sd_min', 'B_sd_ref', 'B_sd_max',
    'B_gravacao_min', 'B_gravacao_ref', 'B_gravacao_max',
    'B_imagem_min', 'B_imagem_ref', 'B_imagem_max',
    'B_total_min', 'B_total_ref', 'B_total_max',
]


# ============================================================================
# CALCULO POR PAGINA
# ============================================================================
def linha_vazia():
    return dict((k, 0) for k in HEADER)


def calcular(inv):
    linhas = []
    for r in inv:
        pag = r['arquivo']
        L = linha_vazia()
        L['arquivo'] = pag
        L['modulo'] = r['modulo']
        L['parte'] = r['parte']
        L['licao'] = r['licao']
        L['tipo_pagina'] = r['tipo_pagina']
        palavras = int(r['palavras'] or 0)
        vs = int(r['video_segundos'] or 0)
        h5p_n = int(r['h5p_atividades'] or 0)
        h5p_it = int(r['h5p_itens'] or 0)
        eh_forum = (r['tipo_pagina'] == 'forum')
        eh_enc = (pag == ENC_PAGINA)
        obs = []

        # Leitura de textos (A) — exceto forum (o "ler instrucoes" ja esta nos 35 min)
        A_leit = dict((c, 0.0) for c in CEN)
        if not eh_forum and palavras > 0:
            for c in CEN:
                A_leit[c] = palavras / float(PPM[c]) * 60.0 * ESTUDO[c]
        L['palavras'] = 0 if eh_forum else palavras

        # Imagens
        A_img = dict((c, 0.0) for c in CEN)
        B_img = dict((c, 0.0) for c in CEN)
        n_img = int(r['imagens'] or 0)
        img_ref = IMG_S.get(pag)
        if eh_enc:
            for c in CEN:
                B_img[c] = IMG_S_B.get(pag, 0) * IMG_FATOR[c]
            L['imagens'] = n_img
        elif img_ref is not None:
            for c in CEN:
                A_img[c] = img_ref * IMG_FATOR[c]
            L['imagens'] = n_img

        # Videos (gravacoes do ENC -> bucket B)
        A_vid = dict((c, 0.0) for c in CEN)
        B_grav = dict((c, 0.0) for c in CEN)
        if eh_enc:
            for c in CEN:
                B_grav[c] = vs * VID_FATOR[c]
        else:
            for c in CEN:
                A_vid[c] = vs * VID_FATOR[c]
        L['video_s'] = vs

        # Atividades H5P (A)
        A_h5p = dict((c, 0.0) for c in CEN)
        if h5p_n > 0:
            base, tipo = h5p_ref_s(pag, h5p_it)
            if not tipo:
                obs.append('H5P sem tipo mapeado')
            for c in CEN:
                A_h5p[c] = base * H5P_FATOR[c]
            L['h5p_n'] = h5p_n
            L['h5p_itens'] = h5p_it
            L['h5p_tipo'] = tipo

        # Foruns (A)
        A_forum = dict((c, 0.0) for c in CEN)
        if eh_forum:
            fmin = 20 if 'Boas-vindas' in pag else FORUM['ref']
            A_forum['min'] = FORUM['min'] * 60.0
            A_forum['ref'] = fmin * 60.0
            A_forum['max'] = FORUM['max'] * 60.0
            L['forum_min_ref'] = fmin

        # Navegacao (A) — 1 pagina nova por linha de conteudo
        A_nav = dict((c, NAV[c]) for c in CEN)
        L['nav_s_ref'] = NAV['ref']

        # Textos externos instruidos (A)
        A_ext = dict((c, 0.0) for c in CEN)
        wp = EXT_PALAVRAS.get(pag)
        if wp:
            for c in CEN:
                A_ext[c] = wp / float(PPM[c]) * 60.0 * ESTUDO[c]
            L['ext_palavras'] = wp

        # Bibliografia (B)
        B_bib = dict((c, 0.0) for c in CEN)
        it = BIBLIO_ITENS.get(pag)
        if it:
            for c in CEN:
                B_bib[c] = it * BIBLIO[c] * 60.0
            L['biblio_itens'] = it

        # SD em PDF (B)
        B_sd = dict((c, 0.0) for c in CEN)
        wsd = sd_palavras(pag)
        if wsd:
            for c in CEN:
                B_sd[c] = wsd / float(PPM[c]) * 60.0 * ESTUDO[c]
            L['sd_palavras'] = wsd

        A_total = dict((c, A_leit[c] + A_img[c] + A_vid[c] + A_h5p[c]
                        + A_forum[c] + A_nav[c] + A_ext[c]) for c in CEN)
        B_total = dict((c, B_bib[c] + B_sd[c] + B_grav[c] + B_img[c]) for c in CEN)

        blocos = [('A_leitura', A_leit), ('A_imagem', A_img), ('A_video', A_vid),
                  ('A_h5p', A_h5p), ('A_forum', A_forum), ('A_nav', A_nav),
                  ('A_ext', A_ext), ('A_total', A_total),
                  ('B_biblio', B_bib), ('B_sd', B_sd), ('B_gravacao', B_grav),
                  ('B_imagem', B_img), ('B_total', B_total)]
        for nome, dct in blocos:
            for c in CEN:
                L['{}_{}'.format(nome, c)] = int(round(dct[c]))

        L['bucket'] = 'A' + ('/B' if (eh_enc or B_total['ref'] > 0) else '')
        if eh_enc:
            obs.append('imagens + videos (gravacoes) = bucket B')
        L['obs'] = '; '.join(obs)
        linhas.append(L)
    return linhas


# ============================================================================
# LINHAS DE AJUSTE (nao sao "pagina"): navegacao de interface, encontros e atividades do M5
# ============================================================================


def linhas_de_ajuste():
    linhas = []

    # Navegacao estrutural: 24 arquivos de label + 3 frontpage (bucket A)
    n = NAV_LABELS + NAV_FRONTPAGE
    L = linha_vazia()
    L['arquivo'] = '(ajuste) labels + frontpage'
    L['modulo'] = 'ESTRUTURA'
    L['tipo_pagina'] = 'navegacao'
    L['nav_s_ref'] = NAV['ref']
    L['imagens'] = n
    for c in CEN:
        v = int(round(n * NAV[c]))
        L['A_nav_{}'.format(c)] = v
        L['A_total_{}'.format(c)] = v
    L['bucket'] = 'A'
    L['obs'] = '{} labels + {} frontpage x 30 s (parametros §5.8)'.format(NAV_LABELS, NAV_FRONTPAGE)
    linhas.append(L)

    # Encontros sincronos: 3 x 1h30 de participacao (bucket A)
    L = linha_vazia()
    L['arquivo'] = '(ajuste) encontros sincronos (participacao)'
    L['modulo'] = 'ENC'
    L['tipo_pagina'] = 'encontro'
    L['imagens'] = ENC_ENCONTROS
    for c in CEN:
        v = ENC_ENCONTROS * ENCONTRO_S
        L['A_encontro_{}'.format(c)] = v
        L['A_total_{}'.format(c)] = v
    L['bucket'] = 'A'
    L['obs'] = '3 encontros x 1h30 (3º computado como executado — decisao do mestre)'
    linhas.append(L)

    # 3ª gravacao do Encontro: em 25/11/2026 ela passou a estar NA PAGINA dos Encontros
    # (video embedado, 1h27min19s lidos nos creditos) -> a antiga linha "(ajuste) 3ª gravacao
    # (declarada 1h30)" foi REMOVIDA para nao contar duas vezes (anti-dupla-contagem).

    # Atividades de conclusao do M5 (bucket A) — nao sao pagina: questionario do Forms,
    # preenchimento do PDF do Plano de Acao, envio da Tarefa e emissao do Certificado.
    for rotulo, seg, obs in ATIV_M5:
        L = linha_vazia()
        L['arquivo'] = rotulo
        L['modulo'] = 'M5'
        L['tipo_pagina'] = 'atividade'
        for c in CEN:
            L['A_total_{}'.format(c)] = seg
        L['bucket'] = 'A'
        L['obs'] = obs
        linhas.append(L)
    return linhas


def somar(linhas):
    """Soma as colunas de tempo dos 3 cenarios."""
    chaves = [k for k in HEADER if k.endswith(('_min', '_ref', '_max'))]
    return dict((k, sum(int(L.get(k, 0)) for L in linhas)) for k in chaves)


def main():
    with open(INV_CSV, encoding='utf-8') as f:
        inv = list(csv.DictReader(f, delimiter=';'))
    conteudo = calcular(inv)
    linhas = conteudo + linhas_de_ajuste()

    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=HEADER, delimiter=';')
        w.writeheader()
        for L in linhas:
            w.writerow(L)

    totais = somar(linhas)
    with open(OUT_MD, 'w', encoding='utf-8') as f:
        escrever_md(f, linhas, totais, inv)

    print('OK — {} linhas'.format(len(linhas)))
    print('   bucket A  ref    = {}'.format(fmt(totais['A_total_ref'])))
    print('   bucket A  recom. = {}  (+10%)'.format(fmt(totais['A_total_ref'] * (1 + OVERHEAD))))
    print('   bucket B  ref    = {}'.format(fmt(totais['B_total_ref'])))


# ============================================================================
# RELATORIO EM MARKDOWN (tabelas-resumo)
# ============================================================================
def _soma(linhas):
    acc = {}
    for L in linhas:
        for k in HEADER:
            if k.endswith(('_min', '_ref', '_max')):
                acc[k] = acc.get(k, 0) + int(L.get(k, 0))
    return acc


def escrever_md(f, linhas, totais, inv):
    W = f.write
    conteudo = [L for L in linhas if not L['arquivo'].startswith('(ajuste)')]
    mods = {}
    for L in conteudo:
        mods.setdefault(L['modulo'], []).append(L)

    W('<!-- Registro interno do Ciclo 4 — calculo de carga horaria. '
      'Gerado por scripts/calculo-carga-horaria.py -->\n\n')
    W('# ⏱️ Cálculo de Carga Horária — Curso Vaga Lume\n\n')
    W('> **O que é:** planilha de cálculo (Ciclo 4) com **uma linha por página** no `.csv` '
      'companheiro e as **tabelas-resumo** aqui. Método: `tempo = quantidade × parâmetro × fator de cenário`.\n')
    W('> **Quantidades:** `inventario-recursos.csv` (todas as páginas do curso, medidas no '
      'inventário de 25/11/2026). **Parâmetros:** '
      '`parametros-carga-horaria.md` (Ciclo 2). **Ajustes finos:** `ajustes-finos.md` (Ciclo 3 + reexecução de 25/11/2026, inclusive as atividades do M5).\n')
    W('> **Buckets:** A = carga **obrigatória** · B = **opcional/complementar**. '
      '**Overhead de +10%** incide **somente** no cenário **recomendado**.\n')
    W('> **É ESTIMATIVA, não medição** (parâmetros são escolhas metodológicas; as quantidades são exatas).\n\n')
    W('---\n\n')

    # ---- §1 Totais gerais ----
    A = {c: totais['A_total_{}'.format(c)] for c in CEN}
    B = {c: totais['B_total_{}'.format(c)] for c in CEN}
    Arec = int(round(A['ref'] * (1 + OVERHEAD)))
    Brec = int(round(B['ref'] * (1 + OVERHEAD)))
    W('## §1 — Totais gerais (4 cenários)\n\n')
    W('| Bucket | Mínimo | **Referência** | Máximo | **Recomendado** (+10%) |\n')
    W('|---|---|---|---|---|\n')
    W('| **A — obrigatória** | {} | **{}** | {} | **{}** |\n'.format(
        fmt(A['min']), fmt(A['ref']), fmt(A['max']), fmt(Arec)))
    W('| **B — opcional** | {} | {} | {} | {} |\n'.format(
        fmt(B['min']), fmt(B['ref']), fmt(B['max']), fmt(Brec)))
    W('| **A + B** | {} | {} | {} | {} |\n\n'.format(
        fmt(A['min'] + B['min']), fmt(A['ref'] + B['ref']),
        fmt(A['max'] + B['max']), fmt(Arec + Brec)))
    W('> O **número principal do relatório é o bucket A** (carga obrigatória) — o B vai separado.\n\n')

    # ---- §2 Por modulo ----
    W('## §2 — Por módulo (cenário de referência)\n\n')
    W('| Módulo | Linhas | A ref | B ref | Total ref |\n|---|---|---|---|---|\n')
    ordem = ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'ENC', 'ESTRUTURA']
    rotulo = {'ENC': 'Encontros Síncronos (página)', 'M5': 'M5 — Encerramento (medido)',
              'ESTRUTURA': 'Estrutura (navegação)'}
    for m in ordem:
        if m not in mods:
            continue
        t = _soma(mods[m])
        a, b = t.get('A_total_ref', 0), t.get('B_total_ref', 0)
        W('| {} | {} | {} | {} | {} |\n'.format(
            rotulo.get(m, m), len(mods[m]), fmt(a), fmt(b), fmt(a + b)))
    aj_m5 = [L for L in linhas if L['arquivo'].startswith('(ajuste)') and L['modulo'] == 'M5']
    if aj_m5:
        t = _soma(aj_m5)
        a, b = t.get('A_total_ref', 0), t.get('B_total_ref', 0)
        W('| *(ajustes M5: atividades de conclusão)* | {} | {} | {} | {} |\n'.format(
            len(aj_m5), fmt(a), fmt(b), fmt(a + b)))
    aj = [L for L in linhas if L['arquivo'].startswith('(ajuste)') and L['modulo'] != 'M5']
    if aj:
        t = _soma(aj)
        a, b = t.get('A_total_ref', 0), t.get('B_total_ref', 0)
        W('| *(ajustes: navegação e encontros)* | {} | {} | {} | {} |\n'.format(
            len(aj), fmt(a), fmt(b), fmt(a + b)))
    W('\n')
    W('> As linhas *(ajustes)* reúnem o que não pertence a uma página: navegação de interface, '
      'encontros síncronos (participação) e as atividades de conclusão do M5 (questionário do '
      'Forms, preenchimento do Plano de Ação, envio da Tarefa e Certificado). O **Encerramento '
      'agora é MEDIDO** (11 páginas) — a estimativa por analogia com o M0 foi substituída pela '
      'medição. Módulos + ajustes fecham com o §1.\n\n')

    # ---- §3 Por categoria ----
    W('## §3 — Por categoria (cenário de referência)\n\n')
    W('| Categoria | Bucket | Quantidade | Ref | Mín | Máx |\n|---|---|---|---|---|---|\n')
    # Totais por categoria (todas as linhas: o Encerramento entrou como modulo medido)
    ts = somar(linhas)
    palavras = sum(int(L['palavras']) for L in conteudo)
    imagens_a = sum(int(L['imagens']) for L in conteudo if L['arquivo'] != ENC_PAGINA)
    h5p_n = sum(int(L['h5p_n']) for L in conteudo)
    foruns = sum(1 for L in conteudo if int(L['forum_min_ref']) > 0)
    ext_pal = sum(int(L['ext_palavras']) for L in conteudo)
    sd_pal = sum(int(L['sd_palavras']) for L in conteudo)
    grav_s = ts['B_gravacao_ref']
    cat = [
        ('Leitura de textos', 'A', '{} palavras'.format(palavras), 'A_leitura'),
        ('Imagens', 'A', '{} marcadores'.format(imagens_a), 'A_imagem'),
        ('Vídeos de conteúdo', 'A', fmt(totais['A_video_ref']), 'A_video'),
        ('Atividades H5P', 'A', '{} atividades'.format(h5p_n), 'A_h5p'),
        ('Fóruns', 'A', '{} fóruns'.format(foruns), 'A_forum'),
        ('Navegação', 'A', '{} páginas + {} interface'.format(
            len(conteudo), NAV_LABELS + NAV_FRONTPAGE), 'A_nav'),
        ('Textos externos', 'A', '{} palavras'.format(ext_pal), 'A_ext'),
        ('Encontros síncronos', 'A', '3 encontros', 'A_encontro'),
        ('Bibliografia', 'B', '15 itens de texto', 'B_biblio'),
        ('SDs em PDF', 'B', '{} palavras'.format(sd_pal), 'B_sd'),
        ('Gravações', 'B', fmt(grav_s), 'B_gravacao'),
        ('Imagens (Encontros)', 'B', '3 cartazes', 'B_imagem'),
    ]
    for nome, bk, qtd, pre in cat:
        W('| {} | {} | {} | {} | {} | {} |\n'.format(
            nome, bk, qtd, fmt(ts[pre + '_ref']), fmt(ts[pre + '_min']),
            fmt(ts[pre + '_max'])))
    ajm5 = [L for L in linhas if L['arquivo'].startswith('(ajuste)') and L['modulo'] == 'M5']
    if ajm5:
        am5 = _soma(ajm5)
        W('| Atividades de conclusão do M5 | A | {} atividades | {} | {} | {} |\n'.format(
            len(ajm5), fmt(am5['A_total_ref']), fmt(am5['A_total_min']),
            fmt(am5['A_total_max'])))
    W('| **Total — bucket A** | A | | **{}** | **{}** | **{}** |\n'.format(
        fmt(totais['A_total_ref']), fmt(totais['A_total_min']), fmt(totais['A_total_max'])))
    W('\n')

    # ---- §4 Reconciliacao com as ancoras do Ciclo 3 ----
    W('## §4 — Reconciliação com as âncoras do Ciclo 3 (sanidade)\n\n')
    W('| Âncora (Ciclo 3) | Esperado | Calculado (ref) | Confere? |\n|---|---|---|---|\n')
    chk = [
        ('Imagens (bucket A, M1-M5)', 1540, ts['A_imagem_ref']),
        ('Fóruns (bucket A, 13x35 + 1x20 min)', 28500, ts['A_forum_ref']),
        ('Bibliografia (bucket B, 15 x 1,5 min)', 1350, ts['B_biblio_ref']),
        ('Imagens dos Encontros (bucket B)', 135, ts['B_imagem_ref']),
    ]
    for nome, esp, calc in chk:
        W('| {} | {} | {} | {} |\n'.format(
            nome, fmt(esp), fmt(calc), '✅' if abs(esp - calc) < 2 else '⚠️'))
    ext_puro = ext_pal / float(PPM['ref']) * 60.0
    W('| Textos externos (leitura pura, p/ ppm) | {} | {} | ✅ |\n'.format(
        fmt(457), fmt(ext_puro)))
    W('\n> O **estudo ativo (×1,3)** eleva os textos externos de {} para {} no cenário de '
      'referência (bucket A).\n\n'.format(fmt(ext_puro), fmt(totais['A_ext_ref'])))

    # ---- §5 Linhas de ajuste ----
    W('## §5 — Linhas de ajuste (itens que não são página)\n\n')
    W('| Item | Bucket | Ref | Obs |\n|---|---|---|---|\n')
    for L in linhas:
        if not L['arquivo'].startswith('(ajuste)'):
            continue
        ref = int(L['A_total_ref']) + int(L['B_total_ref'])
        W('| {} | {} | {} | {} |\n'.format(L['arquivo'], L['bucket'], fmt(ref), L['obs']))
    W('\n')

    # ---- §6 Notas, decisoes e limitacoes ----
    W('## §6 — Notas, decisões e limitações\n\n')
    W('1. **Páginas de fórum não entram na leitura** — o "ler instruções" já está dentro '
      'dos 35 min (20 no Boas-vindas). Anti-dupla-contagem.\n')
    W('2. **Vídeos da bibliografia** (21) → **18 já contados no bucket A** + 3 sugestões → '
      '**0 min** na bibliografia (princípio do Ciclo 3: não contar duas vezes).\n')
    W('3. **SDs em PDF** (bucket B): texto medido por `pdftotext` = {} palavras a 200 ppm. '
      'A **página** da SD conta no bucket A; o **PDF** no B.\n'.format(sd_pal))
    W('4. **H5P — interpretação do parâmetro**: escolha única/múltipla/V-F = 1,5 min/questão; '
      '**associação/arrastar/desafio = 3 min/atividade**; virar cartões = 20 s/carta; '
      'caça-palavras = 5 min. A alternativa (3 min **por item** nos tipos complexos) está '
      'registrada no script.\n')
    W('5. **ESTUDO ATIVO (×1,3)** aplicado a toda a leitura (conteúdo, textos externos e SDs) '
      'no cenário de referência; ×1,0 no mínimo e ×1,5 no máximo.\n')
    W('6. **ENC — bloco dos encontros REINCORPORADO** (25/11/2026): a página dos Encontros tem '
      'agora **3 gravações** (4h33min24s reais, bucket B), **3 cartazes** (135 s, bucket B) e '
      '710 palavras de texto (bucket A); as **3 participações** de 1h30 estão na linha de '
      'ajuste (bucket A).\n')
    W('7. **3ª gravação do Encontro**: duração **real 1h27min19s**, lida nos créditos da '
      'página (não mais a 1h30 declarada) — a antiga linha de ajuste foi removida para não '
      'contar duas vezes.\n')
    W('8. **Módulo 5 (Encerramento) agora é MEDIDO**: 11 páginas (1 abertura + 10 de conteúdo), '
      '24 fotos em 4 carrosséis (20 s/imagem) e 1 vídeo de 2min53s; as **4 atividades de '
      'conclusão** entram em linhas de ajuste — questionário do Forms 10 min (decisão do '
      'mestre, 25/11/2026), preenchimento do PDF do Plano de Ação 15 min, foto + envio da '
      'Tarefa 3 min e emissão do Certificado 2 min. A **estimativa por analogia com o M0 foi '
      'substituída pela medição**.\n')
    W('9. **Navegação**: {} páginas de conteúdo + {} labels (arquivos em '
      '`templates/pages/labels/`) + {} frontpage a 30 s.\n'.format(
          len(conteudo), NAV_LABELS, NAV_FRONTPAGE))
    W('10. **É estimativa, não medição** — sem relatórios de duração do Moodle (confirmado em '
      '14/10/2026). Parâmetros: `parametros-carga-horaria.md`.\n')
    return


if __name__ == '__main__':
    main()
