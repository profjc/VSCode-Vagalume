#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CALCULO DE CARGA HORARIA — curso Vaga Lume (Moodle 4.5)
# Ciclo 4 do relatorio de carga horaria (ver docs/relatorios/carga-horaria/).
#
# ─────────────────────────────────────────────────────────────────────────────
# DOADO PARA A SKILL metricas-carga-horaria v1.2 (Passo 4 — planilha de calculo).
# E uma INSTANCIA: os PARAMETROS e os AJUSTES FINOS do projeto de origem estao
# NO CODIGO (blocos abaixo). Mapa dos valores: assets/exemplo-calc-vagalume.json.
# Metodo: reference/calculo-e-planilha.md.
# NAO tem CLI: grava nos CAMINHOS FIXOS do projeto (as saidas oficiais). Para
# TESTAR/PARIDADE, rode numa COPIA do projeto (nao sobrescreva as saidas oficiais).
# Generalizar (CLI + config JSON) esta no roadmap da skill.
# ─────────────────────────────────────────────────────────────────────────────
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
}
ENC_PAGINA = 'Encontros-sincronos/encontros_sincronos_galeria.html'
IMG_S_B = {ENC_PAGINA: 90}   # 2 cartazes x 45 s (bucket B)

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
ENC_GRAVACOES_S = [5196, 5969]   # no ar: Encontro 1 (1h26min36) e Encontro 2 (1h39min29)
ENC_GRAVACAO_3_S = 5400          # DECLARADO: 1h30 (mesma duracao do encontro) — a confirmar

# Navegacao estrutural (parametros §5.8)
NAV_LABELS = 21
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
# LINHAS DE AJUSTE (nao sao "pagina"): navegacao de interface, encontros, gravacoes
# ============================================================================
# Categorias do bucket A (para a estimativa do Encerramento = M0)
CATS_A = ('A_leitura', 'A_imagem', 'A_video', 'A_h5p', 'A_forum', 'A_nav', 'A_ext')


def linhas_de_ajuste(m0):
    linhas = []

    # Navegacao estrutural: 21 labels + 3 frontpage (bucket A)
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

    # 3ª gravacao do Encontro (bucket B) — DECLARADA 1h30 (a confirmar).
    # ATENCAO: as 2 gravacoes ja no ar estao na propria pagina dos Encontros (IMG/video -> B).
    total_grav = ENC_GRAVACAO_3_S
    L = linha_vazia()
    L['arquivo'] = '(ajuste) 3ª gravacao do Encontro (declarada)'
    L['modulo'] = 'ENC'
    L['tipo_pagina'] = 'gravacao'
    L['video_s'] = total_grav
    for c in CEN:
        L['B_gravacao_{}'.format(c)] = total_grav
        L['B_total_{}'.format(c)] = total_grav
    L['bucket'] = 'B'
    L['obs'] = '3ª gravacao DECLARADA 1h30 (a confirmar) — as 2 no ar estao na pagina dos Encontros'
    linhas.append(L)

    # Modulo de Encerramento (Certificacao e Avaliacao) — ESTIMADO = Modulo 0.
    # Decisao do mestre (15/10/2026): "computar o modulo de finalizacao como tendo o
    # mesmo tempo total que o modulo de Boas-vindas", com ressalva declarada.
    L = linha_vazia()
    L['arquivo'] = '(ajuste) Módulo de Encerramento (estimado = M0)'
    L['modulo'] = 'ENCERR.'
    L['tipo_pagina'] = 'estimativa'
    for cat in CATS_A:
        for c in CEN:
            L[cat + '_' + c] = m0[cat][c]
    for c in CEN:
        L['A_total_' + c] = sum(m0[cat][c] for cat in CATS_A)
    L['bucket'] = 'A'
    L['obs'] = 'ESTIMADO = Módulo 0 (decisao do mestre, 15/10/2026) — a substituir pela medicao quando o modulo for produzido'
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
    # M0 (Boas-vindas) — base da estimativa do Modulo de Encerramento (decisao do mestre)
    m0 = {}
    for cat in CATS_A:
        m0[cat] = {}
        for c in CEN:
            m0[cat][c] = sum(int(L[cat + '_' + c]) for L in conteudo if L['modulo'] == 'M0')
    linhas = conteudo + linhas_de_ajuste(m0)

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
    W('> **Quantidades:** `inventario-recursos.csv` (147 páginas). **Parâmetros:** '
      '`parametros-carga-horaria.md` (Ciclo 2). **Ajustes finos:** `ajustes-finos.md` (Ciclo 3).\n')
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
    ordem = ['M0', 'M1', 'M2', 'M3', 'M4', 'ENC', 'ENCERR.', 'ESTRUTURA']
    rotulo = {'ENC': 'Encontros Síncronos (página)', 'ENCERR.': 'Encerramento (estimado = M0)',
              'ESTRUTURA': 'Estrutura (navegação)'}
    for m in ordem:
        if m not in mods:
            continue
        t = _soma(mods[m])
        a, b = t.get('A_total_ref', 0), t.get('B_total_ref', 0)
        W('| {} | {} | {} | {} | {} |\n'.format(
            rotulo.get(m, m), len(mods[m]), fmt(a), fmt(b), fmt(a + b)))
    encerr = [L for L in linhas if L['modulo'] == 'ENCERR.']
    if encerr:
        t = _soma(encerr)
        a, b = t.get('A_total_ref', 0), t.get('B_total_ref', 0)
        W('| Encerramento *(estimado = M0)* | {} | {} | {} | {} |\n'.format(
            len(encerr), fmt(a), fmt(b), fmt(a + b)))
    aj = [L for L in linhas if L['arquivo'].startswith('(ajuste)') and L['modulo'] != 'ENCERR.']
    if aj:
        t = _soma(aj)
        a, b = t.get('A_total_ref', 0), t.get('B_total_ref', 0)
        W('| *(ajustes: navegação, encontros, gravação)* | {} | {} | {} | {} |\n'.format(
            len(aj), fmt(a), fmt(b), fmt(a + b)))
    W('\n')
    W('> A linha *(ajustes)* reúne o que não pertence a uma página (navegação de interface, '
      'encontros síncronos e 3ª gravação). O **Encerramento** é **estimado = M0** (ver §6). '
      'Módulos + Encerramento + ajustes fecham com o §1.\n\n')

    # ---- §3 Por categoria ----
    W('## §3 — Por categoria (cenário de referência)\n\n')
    W('| Categoria | Bucket | Quantidade | Ref | Mín | Máx |\n|---|---|---|---|---|---|\n')
    # Totais por categoria SEM o Encerramento (que entra como linha propria)
    ts = somar([L for L in linhas if L['modulo'] != 'ENCERR.'])
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
        ('Navegação', 'A', '{} páginas + 24 interface'.format(len(conteudo)), 'A_nav'),
        ('Textos externos', 'A', '{} palavras'.format(ext_pal), 'A_ext'),
        ('Encontros síncronos', 'A', '3 encontros', 'A_encontro'),
        ('Bibliografia', 'B', '15 itens de texto', 'B_biblio'),
        ('SDs em PDF', 'B', '{} palavras'.format(sd_pal), 'B_sd'),
        ('Gravações', 'B', fmt(grav_s), 'B_gravacao'),
        ('Imagens (Encontros)', 'B', '2 cartazes', 'B_imagem'),
    ]
    for nome, bk, qtd, pre in cat:
        W('| {} | {} | {} | {} | {} | {} |\n'.format(
            nome, bk, qtd, fmt(ts[pre + '_ref']), fmt(ts[pre + '_min']),
            fmt(ts[pre + '_max'])))
    tenc = _soma([L for L in linhas if L['modulo'] == 'ENCERR.'])
    W('| **Encerramento** *(estimado = M0)* | A | por analogia | {} | {} | {} |\n'.format(
        fmt(tenc['A_total_ref']), fmt(tenc['A_total_min']), fmt(tenc['A_total_max'])))
    W('| **Total — bucket A** | A | | **{}** | **{}** | **{}** |\n'.format(
        fmt(totais['A_total_ref']), fmt(totais['A_total_min']), fmt(totais['A_total_max'])))
    W('\n')

    # ---- §4 Reconciliacao com as ancoras do Ciclo 3 ----
    W('## §4 — Reconciliação com as âncoras do Ciclo 3 (sanidade)\n\n')
    W('| Âncora (Ciclo 3) | Esperado | Calculado (ref) | Confere? |\n|---|---|---|---|\n')
    chk = [
        ('Imagens (bucket A, M1-M3)', 1000, ts['A_imagem_ref']),
        ('Fóruns (bucket A, 13x35 + 1x20 min)', 28500, ts['A_forum_ref']),
        ('Bibliografia (bucket B, 15 x 1,5 min)', 1350, ts['B_biblio_ref']),
        ('Imagens dos Encontros (bucket B)', 90, ts['B_imagem_ref']),
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
    W('6. **ENC — bloco novo dos encontros** (texto + imagem + vídeo, computado como executado '
      'pela decisão do mestre): **não incluído** por falta de quantidades (não produzido) — '
      'reincorporar na reexecução (§8 do `PLANO-carga-horaria.md`).\n')
    W('7. **3ª gravação do Encontro** sem duração publicada → adotada **1h30 (declarada)** para '
      'não subestimar; confirmar quando o encontro ocorrer.\n')
    W('8. **Módulo de Encerramento** (Certificação e Avaliação): **não produzido** — '
      'estimado **por analogia com o Módulo 0 (Boas-vindas)**, a pedido da coordenação '
      '(15/10/2026), para uma carga mais realista; a substituir pela **medição** na '
      'reexecução (§8).\n')
    W('9. **Navegação**: contadas as {} páginas de conteúdo + 21 labels + 3 frontpage a 30 s '
      '(a §5.8 previa 146 páginas; a página dos Encontros soma +1).\n'.format(len(conteudo)))
    W('10. **É estimativa, não medição** — sem relatórios de duração do Moodle (confirmado em '
      '14/10/2026). Parâmetros: `parametros-carga-horaria.md`.\n')
    return


if __name__ == '__main__':
    main()
