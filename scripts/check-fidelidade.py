#!/usr/bin/env python3
#
# check-fidelidade.py — confere a fidelidade de uma página HTML do curso Vaga Lume
# contra o trecho correspondente do DI (o .md convertido do .docx do autor).
#
# O que faz: extrai TODOS os blocos visíveis (<p> e <li>) da página e verifica se cada
# linha útil do intervalo informado do DI aparece idêntica na página. A comparação ignora
# tags HTML, o negrito do markdown (**texto**), os marcadores de lista ("- ") e a
# numeração dos títulos de passo ("1. ", "2. " …) — que na página fica nos badges laranja.
#
# Uso:
#   python3 scripts/check-fidelidade.py <pagina.html> <DI.md> <linha_ini> <linha_fim>
#
# Exemplo:
#   python3 scripts/check-fidelidade.py \
#     templates/pages/M4/Parte3/Licao4/M4P3L4p5.html \
#     content/M4/Módulo_IV_Versão_para_DI.md 1688 1769
#
# Saída: bloco visível contados, intervalo conferido e a lista de divergências (linha do DI
# + texto que não foi encontrado na página).
# Código de saída: 0 = nenhuma divergência · 1 = há divergências · 2 = uso incorreto.
#
import html
import re
import sys

USO = 'Uso: python3 scripts/check-fidelidade.py <pagina.html> <DI.md> <linha_ini> <linha_fim>'


def norm(s):
    """Normaliza um trecho: nbsp -> espaço, tira negrito markdown, tags HTML e espaços múltiplos."""
    s = s.replace('\u00a0', ' ').replace('**', '').replace('*', '')
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    return ' '.join(s.split())


def prep(t):
    """Remove o marcador de lista ("- ") e a numeração de passo ("1. ") do texto do DI."""
    t = t.strip()
    if t.startswith('- '):
        t = t[2:].strip()
    m = re.match(r'^(\d)\.\s+(.*)$', t)
    if m:
        t = m.group(2).strip()
    return t


def main():
    if len(sys.argv) != 5:
        print(USO, file=sys.stderr)
        return 2

    pagina, di_path = sys.argv[1], sys.argv[2]
    try:
        ini, fim = int(sys.argv[3]), int(sys.argv[4])
    except ValueError:
        print(USO, file=sys.stderr)
        return 2

    with open(pagina, encoding='utf-8') as fh:
        pag = fh.read()
    with open(di_path, encoding='utf-8') as fh:
        di = fh.read().split('\n')

    vis = [norm(x) for x in re.findall(r'<p[^>]*>(.*?)</p>', pag, re.S)]
    vis += [norm(x) for x in re.findall(r'<li[^>]*>([^<]*)</li>', pag)]

    falhas = []
    for i in range(ini, fim + 1):
        if i > len(di):
            break
        t = prep(norm(di[i - 1]))
        if not t:
            continue
        # Meta-instruções do DI (não são conteúdo): marcadores "\> INÍCIO/FIM DA LIÇÃO",
        # blocos entre [ ... ], a linha "TÍTULO: ..." da lição e o rótulo "Sequência Didática N".
        if (t.startswith('\\') or t.startswith('[') or t.startswith('TÍTULO:')
                or t.startswith('> INÍCIO') or t.startswith('> FIM')
                or t.startswith('Sequência Didática ')):
            continue
        if t not in vis:
            falhas.append((i, t))

    print('Página:  %s' % pagina)
    print('DI:      %s (l. %d a %d)' % (di_path, ini, fim))
    print('Blocos visíveis na página: %d' % len(vis))
    if falhas:
        print('DIVERGÊNCIAS (%d):' % len(falhas))
        for linha, texto in falhas:
            print('  l. %d: %s' % (linha, texto))
        return 1
    print('FALHAS: nenhuma — texto fiel ao DI')
    return 0


if __name__ == '__main__':
    sys.exit(main())
