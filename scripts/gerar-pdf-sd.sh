#!/usr/bin/env bash
#
# Gera o PDF (documento A4) de uma Sequencia Didatica a partir da pagina HTML do Moodle.
# Usa o espelho templates/documentos/espelho-sequencia-didatica.html e o Google Chrome headless.
#
# Uso:
#   scripts/gerar-pdf-sd.sh <pagina.html> <saida.pdf>
# Exemplo:
#   scripts/gerar-pdf-sd.sh templates/pages/M4/Parte3/Licao2/M4P3L2p2.html assets/pdf/M4/M4P3L2p2.pdf
#
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PAGINA="${1:?Uso: $0 <pagina.html> <saida.pdf>}"
SAIDA="${2:?Uso: $0 <pagina.html> <saida.pdf>}"

ESPELHO="$RAIZ/templates/documentos/espelho-sequencia-didatica.html"
[ -f "$PAGINA" ] || { echo "ERRO: pagina nao encontrada: $PAGINA" >&2; exit 1; }
[ -f "$ESPELHO" ] || { echo "ERRO: espelho nao encontrado: $ESPELHO" >&2; exit 1; }

NOME="$(basename "${PAGINA%.html}")"
TMP_DIR="$RAIZ/temp/documentos"
DOC="$TMP_DIR/$NOME.html"
CORPO="$TMP_DIR/$NOME.corpo.html"
mkdir -p "$TMP_DIR" "$(dirname "$SAIDA")"

# 1) Cabecalho a partir do comentario da 1a linha ("Modulo 4 - Parte 3 - Licao 2 - Pagina 2 - Titulo")
CABECALHO="$(head -n1 "$PAGINA" | sed -E 's/^[[:space:]]*<!--(.*)-->[[:space:]]*$/\1/' | sed -E 's/^[[:space:]]+|[[:space:]]+$//g')"
TITULO="$(printf '%s' "$CABECALHO" | awk -F' - ' '{print $NF}')"
CONTEXTO="$(printf '%s' "$CABECALHO" | sed -E 's/ - [^-]+$//')"

# 2) Corpo: conteudo da pagina sem os comentarios de abertura/fechamento e sem o bloco do botao de download
grep -v -E '^[[:space:]]*<!--[[:space:]]*(Módulo|FIM:)' "$PAGINA" \
  | sed '/INICIO-BOTAO-PDF/,/FIM-BOTAO-PDF/d' \
  > "$CORPO"

# 3) Documento = espelho (com titulo/contexto preenchidos) + corpo injetado no marcador
sed -e "s|\[\[TITULO\]\]|$TITULO|g" -e "s|\[\[CONTEXTO\]\]|$CONTEXTO|g" "$ESPELHO" > "$DOC.tmp"
awk -v corpo="$CORPO" '
  /<!-- CONTEUDO-DA-SEQUENCIA -->/ { while ((getline linha < corpo) > 0) print linha; close(corpo); next }
  { print }
' "$DOC.tmp" > "$DOC"
rm -f "$DOC.tmp"

# 4) PDF via Google Chrome headless
PERFIL="$(mktemp -d)"
google-chrome --headless=new --disable-gpu --no-sandbox --user-data-dir="$PERFIL" \
  --no-pdf-header-footer --run-all-compositor-stages-before-draw --virtual-time-budget=10000 \
  --print-to-pdf="$SAIDA" "file://$DOC" >/dev/null 2>&1 || true
rm -rf "$PERFIL"

[ -s "$SAIDA" ] || { echo "ERRO: falha ao gerar o PDF ($SAIDA)" >&2; exit 1; }
echo "PDF gerado: $SAIDA ($(stat -c%s "$SAIDA") bytes) | doc intermediario: $DOC"
