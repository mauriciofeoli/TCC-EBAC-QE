#!/usr/bin/env bash
# Gera o TCC, renderiza em PDF (LibreOffice em Docker), calcula as páginas do sumário e gera novamente.
# Uso (Git Bash, na raiz do repo): bash docs/gerador/renderizar.sh "<template.docx>" <pasta_saida>
set -e
TEMPLATE="$1"
SAIDA="${2:-$TMP/tcc-render}"
RAIZ="$(cd "$(dirname "$0")/../.." && pwd)"
mkdir -p "$SAIDA"


renderizar() {
  cp "$RAIZ/docs/TCC-EBAC-QE.docx" "$SAIDA/"
  rm -f "$SAIDA"/pg-*.jpg
  MSYS_NO_PATHCONV=1 docker run --rm -v "$(cygpath -w "$SAIDA" 2>/dev/null || echo "$SAIDA"):/data" tcc-lo-render sh -c \
    "cd /data && soffice --headless --convert-to pdf TCC-EBAC-QE.docx >/dev/null 2>&1 && pdftotext -layout TCC-EBAC-QE.pdf tcc.txt && pdftoppm -jpeg -r 60 TCC-EBAC-QE.pdf pg"
}

python "$RAIZ/docs/gerador/gerar_tcc.py" "$TEMPLATE"
renderizar
python "$RAIZ/docs/gerador/calcular_paginas.py" "$SAIDA/tcc.txt"
python "$RAIZ/docs/gerador/gerar_tcc.py" "$TEMPLATE"
renderizar
echo "PDF e páginas em: $SAIDA"
