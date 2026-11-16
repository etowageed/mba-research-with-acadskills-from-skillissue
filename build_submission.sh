#!/usr/bin/env bash
set -euo pipefail

# 1. Ensure Python environment with matplotlib & numpy
PYTHON_BIN="python3"
if ! python3 -c "import matplotlib, numpy" 2>/dev/null; then
  if [ ! -d ".venv" ]; then
    echo "Creating .venv and installing matplotlib + numpy..."
    python3 -m venv .venv
  fi
  PYTHON_BIN=".venv/bin/python"
  "$PYTHON_BIN" -m pip install --quiet --upgrade pip matplotlib numpy
fi

# 2. Generate 300 DPI colorblind-safe figures
"$PYTHON_BIN" figures/generate_figures.py

# 3. Check exact core word count (Executive Summary through Chapter 6)
"$PYTHON_BIN" - << 'EOF'
text = open("paper.md", encoding="utf-8").read()
core = text.split("## References")[0]
print(f"Core body word count (incl. headers/tables): {len(core.split())}")
EOF

# 4. Compile MS Word (.docx) and PDF (.pdf) if pandoc is available
if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc is not installed. Install with: sudo apt install pandoc texlive-xetex"
  exit 1
fi

pandoc paper.md \
  -o UEL-SG-7002_Applied_Business_Project.docx \
  --from=markdown \
  --to=docx

echo "Created UEL-SG-7002_Applied_Business_Project.docx"

if command -v xelatex >/dev/null 2>&1; then
  pandoc paper.md \
    -o UEL-SG-7002_Applied_Business_Project.pdf \
    --pdf-engine=xelatex \
    -V mainfont="Times New Roman" \
    -V fontsize=12pt \
    -V linestretch=2.0 \
    -V geometry:margin=1in \
    -V header-includes="\usepackage{fancyhdr}\pagestyle{fancy}\fancyhf{}\rhead{\thepage}\lfoot{Student Number: [Insert Student ID]}\renewcommand{\headrulewidth}{0pt}"
  echo "Created UEL-SG-7002_Applied_Business_Project.pdf"
else
  echo "WARNING: xelatex not found; skipped PDF compilation. Install with: sudo apt install texlive-xetex"
fi
