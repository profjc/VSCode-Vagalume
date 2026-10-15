#!/usr/bin/env bash
#
# Gera o DOCX (editavel) do RESUMO EXECUTIVO DE CARGA HORARIA.
#
# Uso:
#   scripts/gerar-resumo-executivo-docx.sh
#
# Entradas:
#   docs/relatorios/carga-horaria/Resumo-executivo-carga-horaria.md
#   assets/documentos/referencia-relatorio.docx   (gerado por scripts/gerar-reference-docx.py)
#   assets/images/logos/vagalume-pdf.png + vanleer-pdf.png   (logos inseridos no topo)
#
# Saida:
#   docs/relatorios/carga-horaria/Resumo-executivo-carga-horaria-vagalume.docx
#
# Nota: o DOCX flui naturalmente, SEM quebra de pagina forcada — decisao do mestre (15/10/2026).
#       A quebra da pagina 2 do PDF e feita, so no espelho HTML, pela classe .quebra-pagina.
#
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MD="$RAIZ/docs/relatorios/carga-horaria/Resumo-executivo-carga-horaria.md"
REF="$RAIZ/assets/documentos/referencia-relatorio.docx"
DOCX="$RAIZ/docs/relatorios/carga-horaria/Resumo-executivo-carga-horaria-vagalume.docx"

[ -f "$MD" ] || { echo "ERRO: markdown nao encontrado: $MD" >&2; exit 1; }

# 1) reference-docx com os estilos da marca (fonte Segoe UI + cores dos titulos)
python3 "$RAIZ/scripts/gerar-reference-docx.py"

# 2) DOCX editavel (mesma fonte .md; imagens relativas a raiz do projeto)
cd "$RAIZ"
pandoc "$MD" --reference-doc="$REF" -o "$DOCX"

# 2b) Corrige as tabelas (o pandoc 2.9 emite <w:tblGrid /> vazio -> colunas colapsam)
python3 "$RAIZ/scripts/ajustar-tabelas-docx.py" "$DOCX"

# 2c) Insere os logos (Vaga Lume + Van Leer) no topo do DOCX
python3 "$RAIZ/scripts/adicionar-logos-docx.py" "$DOCX"

[ -s "$DOCX" ] || { echo "ERRO: falha ao gerar o DOCX ($DOCX)" >&2; exit 1; }
echo "DOCX gerado: $DOCX ($(stat -c%s "$DOCX") bytes)"
