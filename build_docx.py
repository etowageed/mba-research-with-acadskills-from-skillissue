#!/usr/bin/env python3
"""
Convert paper.md + figures/*.png into a UEL-SG-7002 compliant MS Word (.docx)
Formatting: Times New Roman, 12pt, double-spaced, numbered pages, [Student Number] footer.
"""

import re
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn


def add_page_number_to_run(run):
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)


def set_run_font(run, size=12, bold=False, italic=False, color=None):
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color


def add_formatted_runs(p, text, size=12, base_italic=False):
    # Parse **bold**, *italic*, and `code` inline markdown
    tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*|`.*?`)', text)
    for tok in tokens:
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            r = p.add_run(tok[2:-2])
            set_run_font(r, size=size, bold=True, italic=base_italic)
        elif tok.startswith("*") and tok.endswith("*"):
            r = p.add_run(tok[1:-1])
            set_run_font(r, size=size, italic=True)
        elif tok.startswith("`") and tok.endswith("`"):
            r = p.add_run(tok[1:-1])
            set_run_font(r, size=size, italic=base_italic)
        else:
            r = p.add_run(tok)
            set_run_font(r, size=size, italic=base_italic)


def main():
    doc = Document()

    # Page setup: A4, 1-inch margins
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

        # Header: Page number right-aligned
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr = hp.add_run()
        set_run_font(hr, size=11)
        add_page_number_to_run(hr)

        # Footer: Student Number: [Insert Student ID] on every page
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        fr = fp.add_run("Student Number: [Insert Student ID]")
        set_run_font(fr, size=11)

    # Normal style: Times New Roman, 12pt, double-spaced
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 2.0
    style.paragraph_format.space_after = Pt(6)

    lines = Path("paper.md").read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line or line == "---":
            i += 1
            continue

        # Headings
        if line.startswith("# "):
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 2.0
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(12)
            r = p.add_run(line[2:].strip())
            set_run_font(r, size=14, bold=True)
            i += 1
            continue

        if line.startswith("## "):
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 2.0
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run(line[3:].strip())
            set_run_font(r, size=13, bold=True)
            i += 1
            continue

        if line.startswith("### "):
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 2.0
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run(line[4:].strip())
            set_run_font(r, size=12, bold=True)
            i += 1
            continue

        # Image: ![alt](path)
        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', line)
        if img_match:
            img_path = Path(img_match.group(2))
            if img_path.exists():
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.15
                p.add_run().add_picture(str(img_path), width=Inches(6.0))
            i += 1
            continue

        # Markdown Table
        if line.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            # Filter out separator row (---|---)
            rows_data = []
            for idx, tline in enumerate(table_lines):
                if idx == 1 and re.match(r'^[\|\s:\-]+$', tline):
                    continue
                cells = [c.strip() for c in tline.strip("|").split("|")]
                rows_data.append(cells)

            if rows_data:
                ncols = len(rows_data[0])
                table = doc.add_table(rows=len(rows_data), cols=ncols)
                table.style = "Table Grid"
                for r_idx, row in enumerate(rows_data):
                    for c_idx in range(min(ncols, len(row))):
                        cell_p = table.cell(r_idx, c_idx).paragraphs[0]
                        cell_p.paragraph_format.line_spacing = 1.15
                        cell_p.paragraph_format.space_after = Pt(2)
                        add_formatted_runs(cell_p, row[c_idx], size=10.5)
                        if r_idx == 0:
                            for run in cell_p.runs:
                                run.bold = True
            continue

        # Bullet / Numbered list
        if line.startswith("* ") or re.match(r'^\d+\.\s+', line):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.35)
            p.paragraph_format.line_spacing = 2.0
            clean_line = "• " + line[2:] if line.startswith("* ") else line
            add_formatted_runs(p, clean_line, size=12)
            i += 1
            continue

        # Italic figure caption line
        if line.startswith("*Figure ") and line.endswith("*"):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.5
            add_formatted_runs(p, line.strip("*"), size=10.5, base_italic=True)
            i += 1
            continue

        # Standard paragraph
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 2.0
        add_formatted_runs(p, line, size=12)
        i += 1

    out_path = "UEL-SG-7002_Applied_Business_Project.docx"
    doc.save(out_path)
    print(f"Successfully generated {out_path}")


if __name__ == "__main__":
    main()
