#!/usr/bin/env bash
#
# Gera o PDF (documento A4) do RELATORIO DE CARGA HORARIA
# a partir do markdown + espelho templates/documentos/espelho-relatorio.html + Google Chrome headless.
#
# Uso:
#   scripts/gerar-relatorio.sh
#
# Entradas:
#   docs/relatorios/carga-horaria/Relatorio-carga-horaria.md
#   templates/documentos/espelho-relatorio.html
#   assets/images/relatorios/*.png            (graficos; gerados por scripts/gerar-graficos-relatorio.py)
#
# Saida:
#   docs/relatorios/carga-horaria/Relatorio-carga-horaria-vagalume.pdf
#
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MD="$RAIZ/docs/relatorios/carga-horaria/Relatorio-carga-horaria.md"
ESPELHO="$RAIZ/templates/documentos/espelho-relatorio.html"
SAIDA="$RAIZ/docs/relatorios/carga-horaria/Relatorio-carga-horaria-vagalume.pdf"
TMP="$RAIZ/temp/documentos"
mkdir -p "$TMP"

[ -f "$MD" ] || { echo "ERRO: markdown nao encontrado: $MD" >&2; exit 1; }
[ -f "$ESPELHO" ] || { echo "ERRO: espelho nao encontrado: $ESPELHO" >&2; exit 1; }

# 1) Graficos (mantem os PNG em sincronia com o calculo)
if [ -f "$RAIZ/scripts/gerar-graficos-relatorio.py" ]; then
  python3 "$RAIZ/scripts/gerar-graficos-relatorio.py"
fi

# 2) MD -> fragmento HTML e ajuste dos caminhos das imagens para a profundidade do espelho
CORPO="$TMP/Relatorio.corpo.html"
pandoc "$MD" -t html5 -o "$CORPO"
sed -i 's|src="assets/|src="../../assets/|g' "$CORPO"

# 3) Documento = espelho com o corpo injetado no marcador
DOC="$TMP/Relatorio.html"
awk -v corpo="$CORPO" '
  /<!-- CONTEUDO -->/ { while ((getline linha < corpo) > 0) print linha; close(corpo); next }
  { print }
' "$ESPELHO" > "$DOC"

# 4) PDF via Google Chrome headless
PERFIL="$(mktemp -d)"
google-chrome --headless=new --disable-gpu --no-sandbox --user-data-dir="$PERFIL" \
  --no-pdf-header-footer --run-all-compositor-stages-before-draw --virtual-time-budget=15000 \
  --print-to-pdf="$SAIDA" "file://$DOC" >/dev/null 2>&1 || true
rm -rf "$PERFIL"

[ -s "$SAIDA" ] || { echo "ERRO: falha ao gerar o PDF ($SAIDA)" >&2; exit 1; }
echo "PDF gerado: $SAIDA ($(stat -c%s "$SAIDA") bytes) | doc intermediario: $DOC"
