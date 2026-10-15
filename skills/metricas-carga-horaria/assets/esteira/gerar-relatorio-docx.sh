#!/usr/bin/env bash
#
# Gera o DOCX (editavel) e a planilha XLSX do Relatorio de Carga Horaria.
#
# Uso:
#   scripts/gerar-relatorio-docx.sh
#
# Entradas:
#   docs/relatorios/carga-horaria/Relatorio-carga-horaria.md
#   assets/documentos/referencia-relatorio.docx   (gerado por scripts/gerar-reference-docx.py)
#   docs/relatorios/carga-horaria/calculo-carga-horaria.csv
#
# Saidas:
#   docs/relatorios/carga-horaria/Relatorio-carga-horaria-vagalume.docx
#   docs/relatorios/carga-horaria/calculo-carga-horaria.xlsx
#
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MD="$RAIZ/docs/relatorios/carga-horaria/Relatorio-carga-horaria.md"
REF="$RAIZ/assets/documentos/referencia-relatorio.docx"
DOCX="$RAIZ/docs/relatorios/carga-horaria/Relatorio-carga-horaria-vagalume.docx"
CSV="$RAIZ/docs/relatorios/carga-horaria/calculo-carga-horaria.csv"
XLSX="$RAIZ/docs/relatorios/carga-horaria/calculo-carga-horaria.xlsx"

[ -f "$MD" ] || { echo "ERRO: markdown nao encontrado: $MD" >&2; exit 1; }

# 1) reference-docx com os estilos da marca (fonte + cores dos titulos)
python3 "$RAIZ/scripts/gerar-reference-docx.py"

# 2) DOCX editavel (mesma fonte .md; imagens relativas a raiz do projeto)
cd "$RAIZ"
pandoc "$MD" --reference-doc="$REF" -o "$DOCX"

# 2b) Corrige as tabelas (o pandoc emite <w:tblGrid /> vazio -> colunas colapsam)
python3 "$RAIZ/scripts/ajustar-tabelas-docx.py" "$DOCX"

# 2c) Insere os logos (Vaga Lume + Van Leer) no topo do DOCX
python3 "$RAIZ/scripts/adicionar-logos-docx.py" "$DOCX"

# 3) Planilha formatada (XLSX) a partir do CSV do calculo
PERFIL="$(mktemp -d)"
soffice --headless "-env:UserInstallation=file://$PERFIL" --convert-to xlsx \
  --outdir "$RAIZ/docs/relatorios/carga-horaria" "$CSV" >/dev/null 2>&1 || true
rm -rf "$PERFIL"

[ -s "$DOCX" ] || { echo "ERRO: falha ao gerar o DOCX ($DOCX)" >&2; exit 1; }
echo "DOCX gerado: $DOCX ($(stat -c%s "$DOCX") bytes)"
[ -s "$XLSX" ] && echo "XLSX gerado: $XLSX ($(stat -c%s "$XLSX") bytes)" || echo "AVISO: XLSX nao gerado"
