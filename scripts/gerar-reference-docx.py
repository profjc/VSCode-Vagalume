#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# REFERENCE-DOCX DO RELATORIO DE CARGA HORARIA — curso Vaga Lume
# Gera assets/documentos/referencia-relatorio.docx (fonte Segoe UI + cores da marca
# nos titulos) para o pandoc usar como --reference-doc na geracao do DOCX.
#
# Uso:
#   python3 scripts/gerar-reference-docx.py

import os, re, shutil, subprocess, tempfile, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'assets', 'documentos', 'referencia-relatorio.docx')
FONTE = 'Segoe UI'
COR_TITULO = {'Heading1': '5B3925', 'Heading2': 'D96F1A', 'Heading3': '5B3925',
              'Title': '5B3925', 'Subtitle': '5B3925'}


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tmp = tempfile.mkdtemp()
    ref = os.path.join(tmp, 'ref.docx')
    with open(ref, 'wb') as f:
        subprocess.run(['pandoc', '--print-default-data-file', 'reference.docx'],
                       stdout=f, check=True)
    x = os.path.join(tmp, 'x')
    with zipfile.ZipFile(ref) as z:
        z.extractall(x)
    sp = os.path.join(x, 'word', 'styles.xml')
    s = open(sp, encoding='utf-8').read()

    # 1) Fonte padrao: troca todas as referencias a fontes de tema por Segoe UI
    novo = '<w:rFonts w:ascii="{}" w:hAnsi="{}" w:cs="{}"/>'.format(FONTE, FONTE, FONTE)
    s = re.sub(r'<w:rFonts[^>]*(?:majorHAnsi|minorHAnsi)[^>]*/>', novo, s)

    # 2) Cor dos titulos (injeta <w:color> no rPr do estilo)
    for sid, cor in COR_TITULO.items():
        pat = r'(<w:style [^>]*w:styleId="' + sid + r'".*?<w:rPr>)(.*?)(</w:rPr>)'

        def repl(m, cor=cor):
            body = m.group(2)
            if re.search(r'<w:color[^>]*/>', body):
                body = re.sub(r'<w:color[^>]*/>', '<w:color w:val="%s"/>' % cor, body)
            else:
                body = '<w:color w:val="%s"/>' % cor + body
            return m.group(1) + body + m.group(3)

        s = re.sub(pat, repl, s, count=1, flags=re.S)

    with open(sp, 'w', encoding='utf-8') as f:
        f.write(s)

    if os.path.exists(OUT):
        os.remove(OUT)
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(x):
            for fn in files:
                full = os.path.join(root, fn)
                zf.write(full, os.path.relpath(full, x))

    shutil.rmtree(tmp, ignore_errors=True)
    print('OK — reference docx:', OUT)


if __name__ == '__main__':
    main()
