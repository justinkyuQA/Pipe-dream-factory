from pathlib import Path
from reportlab.lib.pagesizes import inch
from reportlab.lib.units import inch as INCH
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import re

PAGE_SIZE = (6 * inch, 9 * inch)

def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(3 * inch, 0.45 * inch, str(doc.page))
    canvas.restoreState()

def md_blocks(text):
    in_code = False
    code = []

    for line in text.splitlines():
        if line.strip().startswith("```"):
            if not in_code:
                in_code = True
                code = []
            else:
                in_code = False
                yield ("code", "\n".join(code))
            continue

        if in_code:
            code.append(line)
            continue

        if line.strip() == "\\pagebreak":
            yield ("break", "")
        elif line.startswith("# "):
            yield ("h1", line[2:].strip())
        elif line.startswith("## "):
            yield ("h2", line[3:].strip())
        elif line.strip():
            yield ("p", line.strip())

def export_pdf(md_path, pdf_path, editor=False):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="BodyBook", parent=styles["BodyText"], fontSize=10.5, leading=14, spaceAfter=7))
    styles.add(ParagraphStyle(name="BodyEditor", parent=styles["BodyText"], fontSize=11.5, leading=18, spaceAfter=10))

    if editor:
        body = styles["BodyEditor"]
        margins = dict(leftMargin=.85*INCH, rightMargin=.85*INCH, topMargin=.85*INCH, bottomMargin=.85*INCH)
    else:
        body = styles["BodyBook"]
        margins = dict(leftMargin=.75*INCH, rightMargin=.55*INCH, topMargin=.70*INCH, bottomMargin=.70*INCH)

    doc = SimpleDocTemplate(str(pdf_path), pagesize=PAGE_SIZE, **margins)
    story = []

    for kind, text in md_blocks(Path(md_path).read_text(encoding="utf-8")):
        safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        if kind == "break":
            story.append(PageBreak())
        elif kind == "h1":
            story.append(PageBreak())
            story.append(Paragraph(safe, styles["Heading1"]))
        elif kind == "h2":
            story.append(Paragraph(safe, styles["Heading2"]))
        elif kind == "code":
            story.append(Preformatted(text, styles["Code"]))
            story.append(Spacer(1, 8))
        else:
            story.append(Paragraph(safe, body))

    doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
    print(f"PDF exported: {pdf_path}")

Path("exports").mkdir(exist_ok=True)

for md in sorted(Path("vault_books").glob("*.md")):
    export_pdf(md, Path("exports") / f"{md.stem}_EDITOR.pdf", editor=True)
    export_pdf(md, Path("exports") / f"{md.stem}_PRINT_6x9.pdf", editor=False)
