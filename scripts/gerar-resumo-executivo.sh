#!/usr/bin/env bash
#
# Gera o PDF (2 paginas A4) do RESUMO EXECUTIVO DE CARGA HORARIA
# a partir do markdown + espelho templates/documentos/espelho-resumo-executivo.html
# + Google Chrome headless. Identidade do relatorio (Ciclo 5), sem a capa inteira.
#
# Uso:
#   scripts/gerar-resumo-executivo.sh
#
# Entradas:
#   docs/relatorios/carga-horaria/Resumo-executivo-carga-horaria.md
#   templates/documentos/espelho-resumo-executivo.html
#   assets/images/relatorios/grafico-modulos.png   (gerado por scripts/gerar-graficos-relatorio.py — NAO e regerado aqui)
#
# Saida:
#   docs/relatorios/carga-horaria/Resumo-executivo-carga-horaria-vagalume.pdf
#
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MD="$RAIZ/docs/relatorios/carga-horaria/Resumo-executivo-carga-horaria.md"
ESPELHO="$RAIZ/templates/documentos/espelho-resumo-executivo.html"
GRAFICO="$RAIZ/assets/images/relatorios/grafico-modulos.png"
SAIDA="$RAIZ/docs/relatorios/carga-horaria/Resumo-executivo-carga-horaria-vagalume.pdf"
TMP="$RAIZ/temp/documentos"
mkdir -p "$TMP"

[ -f "$MD" ] || { echo "ERRO: markdown nao encontrado: $MD" >&2; exit 1; }
[ -f "$ESPELHO" ] || { echo "ERRO: espelho nao encontrado: $ESPELHO" >&2; exit 1; }
[ -f "$GRAFICO" ] || { echo "ERRO: grafico nao encontrado: $GRAFICO (rodar scripts/gerar-graficos-relatorio.py)" >&2; exit 1; }

# 1) MD -> fragmento HTML e ajuste dos caminhos das imagens para a profundidade do espelho
CORPO="$TMP/Resumo-executivo.corpo.html"
pandoc "$MD" -t html5 -o "$CORPO"
sed -i 's|src="assets/|src="../../assets/|g' "$CORPO"

# 2) Documento = espelho com o corpo injetado no marcador
DOC="$TMP/Resumo-executivo.html"
awk -v corpo="$CORPO" '
  /<!-- CONTEUDO -->/ { while ((getline linha < corpo) > 0) print linha; close(corpo); next }
  { print }
' "$ESPELHO" > "$DOC"

# 3) PDF via Google Chrome headless
PERFIL="$(mktemp -d)"
google-chrome --headless=new --disable-gpu --no-sandbox --user-data-dir="$PERFIL" \
  --no-pdf-header-footer --run-all-compositor-stages-before-draw --virtual-time-budget=15000 \
  --print-to-pdf="$SAIDA" "file://$DOC" >/dev/null 2>&1 || true
rm -rf "$PERFIL"

[ -s "$SAIDA" ] || { echo "ERRO: falha ao gerar o PDF ($SAIDA)" >&2; exit 1; }
echo "PDF gerado: $SAIDA ($(stat -c%s "$SAIDA") bytes) | paginas: $(pdfinfo "$SAIDA" | awk '/^Pages:/{print $2}') | doc intermediario: $DOC"
