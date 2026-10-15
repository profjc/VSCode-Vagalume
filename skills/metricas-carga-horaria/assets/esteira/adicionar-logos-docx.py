#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ADICIONA OS LOGOS AO TOPO DO DOCX (Relatorio de Carga Horaria)
# O pandoc nao inclui logos; este pos-processador insere uma linha com os logos
# Vaga Lume + Fundacao Van Leer no inicio do corpo (area de cabecalho).
#
# Uso:
#   python3 scripts/adicionar-logos-docx.py <arquivo.docx>

import os, shutil, sys, tempfile, zipfile
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGOS = [('assets/images/logos/vagalume-pdf.png', 0.55, 1),
         ('assets/images/logos/vanleer-pdf.png', 0.62, 2)]

DRAW = ('<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
        '<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{i}" name="logo{i}"/>'
        '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic><pic:nvPicPr><pic:cNvPr id="{i}" name="logo{i}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
        '<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
        '</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')


def dims(path, alt_pol):
    w, h = Image.open(path).size
    cy = int(alt_pol * 914400)
    cx = int(cy * w / float(h))
    return cx, cy


def main():
    if len(sys.argv) < 2:
        print('Uso: python3 scripts/adicionar-logos-docx.py <arquivo.docx>')
        sys.exit(1)
    docx = sys.argv[1]
    tmp = tempfile.mkdtemp()
    x = os.path.join(tmp, 'x')
    with zipfile.ZipFile(docx) as z:
        z.extractall(x)

    media = os.path.join(x, 'word', 'media')
    os.makedirs(media, exist_ok=True)
    rels_p = os.path.join(x, 'word', '_rels', 'document.xml.rels')
    rels = open(rels_p, encoding='utf-8').read()

    runs = []
    for k, (rel, alt, i) in enumerate(LOGOS):
        rid = 'rId{}'.format(100 + k)
        nome = 'logo-{}'.format(os.path.basename(rel))
        shutil.copyfile(os.path.join(ROOT, rel), os.path.join(media, nome))
        rels = rels.replace('</Relationships>',
                            '<Relationship Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
                            'Id="{}" Target="media/{}"/></Relationships>'.format(rid, nome))
        cx, cy = dims(os.path.join(ROOT, rel), alt)
        runs.append(DRAW.format(cx=cx, cy=cy, i=i, rid=rid))

    open(rels_p, 'w', encoding='utf-8').write(rels)

    dp = os.path.join(x, 'word', 'document.xml')
    s = open(dp, encoding='utf-8').read()
    par = '<w:p><w:pPr><w:jc w:val="right"/></w:pPr>' + ''.join(runs) + '</w:p>'
    s = s.replace('<w:body>', '<w:body>' + par, 1)
    open(dp, 'w', encoding='utf-8').write(s)

    with zipfile.ZipFile(docx, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(x):
            for fn in files:
                full = os.path.join(root, fn)
                zf.write(full, os.path.relpath(full, x))
    shutil.rmtree(tmp, ignore_errors=True)
    print('OK — logos adicionados:', docx)


if __name__ == '__main__':
    main()
