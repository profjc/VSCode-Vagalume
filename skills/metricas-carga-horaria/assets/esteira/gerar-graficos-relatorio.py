#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GRAFICOS DO RELATORIO DE CARGA HORARIA — curso Vaga Lume
# Ciclo 5 do relatorio de carga horaria.
#
# Uso:
#   python3 scripts/gerar-graficos-relatorio.py
#
# Entrada:  docs/relatorios/carga-horaria/calculo-carga-horaria.csv  (Ciclo 4)
# Saidas:   assets/images/relatorios/grafico-modulos.png
#           assets/images/relatorios/grafico-categorias.png
#
# Cores da marca (style-guide.md). Nao altera nada do curso.

import csv, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALC = os.path.join(ROOT, 'docs', 'relatorios', 'carga-horaria', 'calculo-carga-horaria.csv')
OUT = os.path.join(ROOT, 'assets', 'images', 'relatorios')

LARANJA, MARROM, BEGE, DOURADO = '#D96F1A', '#5B3925', '#FAEBDD', '#F8B133'
CINZA = '#8a7a6d'

ROTULO = {
    'M0': 'Boas-vindas', 'M1': 'M1\nPrimeira Infância', 'M2': 'M2\nLeitura e 1ª Inf.',
    'M3': 'M3\nBibliotecas Com.', 'M4': 'M4\nMão na massa', 'ENC': 'Encontros\nsíncronos',
    'ENCERR.': 'Encerramento\n(est. = M0)', 'ESTRUTURA': 'Estrutura\n(navegação)',
}
CAT = {
    'A_leitura': 'Leitura de textos', 'A_imagem': 'Imagens', 'A_video': 'Vídeos',
    'A_h5p': 'Atividades (H5P)', 'A_forum': 'Fóruns', 'A_nav': 'Navegação',
    'A_ext': 'Textos externos', 'A_encontro': 'Encontros síncronos',
}


def carga(rows):
    mods = {}
    for r in rows:
        m = r['modulo'] or '?'
        d = mods.setdefault(m, {'min': 0, 'ref': 0, 'max': 0})
        for c in ('min', 'ref', 'max'):
            d[c] += int(r['A_total_' + c])
    return mods


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = list(csv.DictReader(open(CALC, encoding='utf-8'), delimiter=';'))

    # ---- Grafico 1: carga obrigatoria por modulo x cenarios ----
    mods = carga(rows)
    ordem = [m for m in ['M0', 'M1', 'M2', 'M3', 'M4', 'ENC', 'ENCERR.', 'ESTRUTURA'] if m in mods]
    labels = [ROTULO.get(m, m) for m in ordem]
    x = range(len(ordem))
    w = 0.26
    fig, ax = plt.subplots(figsize=(9.2, 4.1), dpi=150)
    ax.bar([i - w for i in x], [mods[m]['min'] / 3600 for m in ordem], w, label='Mínimo', color=BEGE, edgecolor=CINZA)
    ax.bar(list(x), [mods[m]['ref'] / 3600 for m in ordem], w, label='Referência', color=LARANJA)
    ax.bar([i + w for i in x], [mods[m]['max'] / 3600 for m in ordem], w, label='Máximo', color=MARROM)
    ax.set_ylabel('Horas (carga obrigatória)', color=MARROM, fontsize=9)
    ax.set_title('Carga horária obrigatória por módulo (cenários)', color=MARROM, fontsize=12, fontweight='bold')
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=8, color=MARROM)
    ax.tick_params(axis='y', labelsize=8, colors=MARROM)
    ax.legend(frameon=False, fontsize=8)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.spines['left'].set_color(CINZA)
    ax.spines['bottom'].set_color(CINZA)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'grafico-modulos.png'), facecolor='white')
    plt.close(fig)

    # ---- Grafico 2: carga obrigatoria por categoria (referencia) ----
    tot = {}
    for r in rows:
        for k in CAT:
            tot[k] = tot.get(k, 0) + int(r[k + '_ref'])
    itens = sorted(tot.items(), key=lambda kv: kv[1])
    nomes = [CAT[k] for k, _ in itens]
    vals = [v / 3600 for _, v in itens]
    fig, ax = plt.subplots(figsize=(9.2, 4.1), dpi=150)
    ax.barh(nomes, vals, color=LARANJA)
    ax.set_xlabel('Horas (carga obrigatória — cenário de referência)', color=MARROM, fontsize=9)
    ax.set_title('Carga obrigatória por categoria de recurso', color=MARROM, fontsize=12, fontweight='bold')
    ax.tick_params(labelsize=8, colors=MARROM)
    for i, v in enumerate(vals):
        ax.text(v + 0.05, i, '{:.1f} h'.format(v).replace('.', ','), va='center', fontsize=8, color=MARROM)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.spines['left'].set_color(CINZA)
    ax.spines['bottom'].set_color(CINZA)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'grafico-categorias.png'), facecolor='white')
    plt.close(fig)

    print('OK — graficos em', OUT)


if __name__ == '__main__':
    main()
