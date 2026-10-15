#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# AJUSTE DAS TABELAS DO DOCX (Relatorio de Carga Horaria)
# O pandoc 2.9 emite <w:tblGrid /> VAZIO (colunas sem largura) e <w:tblW w:w="0.0" />,
# o que faz o LibreOffice (e alguns leitores) colapsarem as colunas numa so.
# Este pos-processador preenche o grid com larguras iguais e forca a tabela a 100%.
#
# Uso:
#   python3 scripts/ajustar-tabelas-docx.py <arquivo.docx>

import os, re, shutil, sys, tempfile, zipfile

TOTAL = 9360  # largura util em twips (aprox. 16,5 cm)


def main():
    if len(sys.argv) < 2:
        print('Uso: python3 scripts/ajustar-tabelas-docx.py <arquivo.docx>')
        sys.exit(1)
    docx = sys.argv[1]
    tmp = tempfile.mkdtemp()
    x = os.path.join(tmp, 'x')
    with zipfile.ZipFile(docx) as z:
        z.extractall(x)
    dp = os.path.join(x, 'word', 'document.xml')
    s = open(dp, encoding='utf-8').read()

    def fix(m):
        tbl = m.group(0)
        ini = tbl.find('<w:tr')
        if ini < 0:
            return tbl
        fim = tbl.find('</w:tr>', ini)
        n = tbl[ini:fim].count('<w:tc>')
        if n == 0:
            return tbl
        w = TOTAL // n
        grid = '<w:tblGrid>' + ('<w:gridCol w:w="%d"/>' % w) * n + '</w:tblGrid>'
        tbl = re.sub(r'<w:tblGrid\s*/>', grid, tbl, count=1)
        tbl = re.sub(r'<w:tblW w:type="pct" w:w="0\.0"\s*/>',
                     '<w:tblW w:type="pct" w:w="5000"/>', tbl, count=1)
        return tbl

    s = re.sub(r'<w:tbl>.*?</w:tbl>', fix, s, flags=re.S)
    with open(dp, 'w', encoding='utf-8') as f:
        f.write(s)

    with zipfile.ZipFile(docx, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(x):
            for fn in files:
                full = os.path.join(root, fn)
                zf.write(full, os.path.relpath(full, x))
    shutil.rmtree(tmp, ignore_errors=True)
    print('OK — tabelas ajustadas:', docx)


if __name__ == '__main__':
    main()
