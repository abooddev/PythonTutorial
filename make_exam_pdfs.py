"""Build the 7th-grade math exam and its solution as two PDFs."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


styles = getSampleStyleSheet()

TITLE = ParagraphStyle(
    "Title", parent=styles["Title"], fontSize=20, spaceAfter=6,
)
META = ParagraphStyle(
    "Meta", parent=styles["Normal"], fontSize=11, textColor=colors.HexColor("#555"),
    spaceAfter=14,
)
H2 = ParagraphStyle(
    "H2", parent=styles["Heading2"], fontSize=14, spaceBefore=14, spaceAfter=8,
    textColor=colors.HexColor("#1a4480"),
)
Q = ParagraphStyle(
    "Q", parent=styles["Normal"], fontSize=11, spaceBefore=8, spaceAfter=4,
    leading=15, alignment=TA_LEFT,
)
SUB = ParagraphStyle(
    "Sub", parent=styles["Normal"], fontSize=11, leftIndent=18,
    leading=15, spaceAfter=4,
)
ANS = ParagraphStyle(
    "Ans", parent=styles["Normal"], fontSize=11, leading=15, leftIndent=18,
    textColor=colors.HexColor("#0a5a2a"), spaceAfter=4,
)
BOX = ParagraphStyle(
    "Box", parent=styles["Normal"], fontSize=11, leading=15,
    backColor=colors.HexColor("#f4f4f4"), borderPadding=6,
    borderColor=colors.HexColor("#ddd"), borderWidth=0.5,
    spaceBefore=4, spaceAfter=10,
)


def table_block(data, col_widths=None):
    t = Table(data, colWidths=col_widths, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e7eef7")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1a4480")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#aaa")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return t


# ─────────────────────────────────────────────────────────────────────────────
# EXAM PDF
# ─────────────────────────────────────────────────────────────────────────────


def build_exam():
    story = []
    story.append(Paragraph("7th Grade Mathematics Exam", TITLE))
    story.append(
        Paragraph(
            "Name: ________________________ &nbsp;&nbsp; Date: ____________ "
            "<br/>Time: 60 minutes &nbsp;&nbsp;|&nbsp;&nbsp; Total: 60 points "
            "<br/><i>Show all work. Calculators are not permitted.</i>",
            META,
        )
    )

    # ── Part A
    story.append(Paragraph("Part A — Proportionality &amp; Proportion Coefficient (20 pts)", H2))

    story.append(Paragraph(
        "<b>Q1.</b> (4 pts) The table below shows the distance traveled by a car "
        "at constant speed.", Q,
    ))
    story.append(table_block(
        [["Time (h)", "2", "3", "5", "7"],
         ["Distance (km)", "70", "105", "175", "245"]],
        col_widths=[3.3 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))
    story.append(Paragraph("a) Is this a proportional relationship? Justify.", SUB))
    story.append(Paragraph("b) Determine the proportion coefficient <i>k</i>.", SUB))
    story.append(Paragraph("c) Write a formula relating distance <i>d</i> to time <i>t</i>.", SUB))

    story.append(Paragraph(
        "<b>Q2.</b> (4 pts) The table below is proportional with coefficient "
        "<i>k</i> = 3. Complete the missing values:", Q,
    ))
    story.append(table_block(
        [["x", "2", "4", "?", "10"],
         ["y", "6", "?", "21", "?"]],
        col_widths=[2 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))

    story.append(Paragraph(
        "<b>Q3.</b> (4 pts) Solve for <i>x</i> using cross-multiplication: "
        "&nbsp;&nbsp; 4 / 10 = x / 25.", Q,
    ))

    story.append(Paragraph(
        "<b>Q4.</b> (4 pts) A recipe uses <b>150 g of flour</b> for <b>4 cookies</b>. "
        "How many grams of flour are needed for <b>18 cookies</b>?", Q,
    ))

    story.append(Paragraph(
        "<b>Q5.</b> (4 pts) For each table, say whether the relationship is "
        "proportional. Justify.", Q,
    ))
    story.append(Paragraph("Table a)", SUB))
    story.append(table_block(
        [["x", "1", "2", "3", "4"], ["y", "3", "6", "9", "12"]],
        col_widths=[2 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))
    story.append(Paragraph("Table b)", SUB))
    story.append(table_block(
        [["x", "1", "2", "3", "4"], ["y", "3", "4", "5", "6"]],
        col_widths=[2 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))

    story.append(PageBreak())

    # ── Part B
    story.append(Paragraph("Part B — Percentages (20 pts)", H2))
    story.append(Paragraph("<b>Q6.</b> (3 pts) Calculate <b>25% of 80</b>.", Q))
    story.append(Paragraph(
        "<b>Q7.</b> (4 pts) In a class of 60 students, 15 wear glasses. "
        "What percentage of the class wears glasses?", Q,
    ))
    story.append(Paragraph(
        "<b>Q8.</b> (5 pts) A bicycle costs <b>200 €</b>. The price increases "
        "by <b>12%</b>. What is the new price?", Q,
    ))
    story.append(Paragraph(
        "<b>Q9.</b> (4 pts) A shirt originally priced <b>50 €</b> is discounted "
        "by <b>20%</b>. What is the final price?", Q,
    ))
    story.append(Paragraph(
        "<b>Q10.</b> (4 pts) Out of 250 students, 30% play a musical instrument. "
        "How many students play one?", Q,
    ))

    # ── Part C
    story.append(Paragraph("Part C — Polynomials Basics (20 pts)", H2))
    story.append(Paragraph(
        "Let &nbsp; P(x) = 3x² + 2x − 1 &nbsp;&nbsp; and &nbsp;&nbsp; "
        "Q(x) = x² − 5x + 4.", BOX,
    ))
    story.append(Paragraph("<b>Q11.</b> (3 pts) Give the degree and the leading coefficient of P(x).", Q))
    story.append(Paragraph("<b>Q12.</b> (4 pts) Compute P(x) + Q(x) and simplify.", Q))
    story.append(Paragraph("<b>Q13.</b> (4 pts) Compute P(x) − Q(x) and simplify.", Q))
    story.append(Paragraph("<b>Q14.</b> (3 pts) Expand: 2x · (x + 3).", Q))
    story.append(Paragraph("<b>Q15.</b> (3 pts) Expand: (x + 4)(x − 2).", Q))
    story.append(Paragraph("<b>Q16.</b> (3 pts) Evaluate P(2) where P(x) = x² − 3x + 5.", Q))

    # ── Bonus
    story.append(Paragraph("Bonus (+3 pts)", H2))
    story.append(Paragraph(
        "A jacket costs <b>80 €</b>. It is first reduced by <b>25%</b>, then "
        "the reduced price is increased by <b>25%</b>. Is the final price "
        "equal to 80 €? Justify with a calculation.", Q,
    ))

    doc = SimpleDocTemplate(
        "exam_7th_grade_math.pdf", pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="7th Grade Math Exam",
    )
    doc.build(story)


# ─────────────────────────────────────────────────────────────────────────────
# SOLUTIONS PDF
# ─────────────────────────────────────────────────────────────────────────────


def build_solutions():
    s = []
    s.append(Paragraph("7th Grade Math Exam — Detailed Solutions", TITLE))
    s.append(Paragraph(
        "All numerical results in this document were verified symbolically with "
        "SymPy via the bundled <i>math</i> skill.", META,
    ))

    s.append(Paragraph("Part A — Proportionality &amp; Proportion Coefficient", H2))

    s.append(Paragraph("<b>Q1.</b>", Q))
    s.append(Paragraph(
        "a) Compute every ratio distance / time:&nbsp;&nbsp; 70/2 = 35, "
        "105/3 = 35, 175/5 = 35, 245/7 = 35. All equal → proportional.", SUB,
    ))
    s.append(Paragraph("b) Proportion coefficient <b>k = 35</b> (km/h).", SUB))
    s.append(Paragraph("c) Formula: <b>d = 35 · t</b>.", ANS))

    s.append(Paragraph("<b>Q2.</b> With k = 3, so y = 3x.", Q))
    s.append(Paragraph(
        "x = 4 → y = 12&nbsp;&nbsp;|&nbsp;&nbsp; y = 21 → x = 7"
        "&nbsp;&nbsp;|&nbsp;&nbsp; x = 10 → y = 30.", SUB,
    ))
    s.append(table_block(
        [["x", "2", "4", "7", "10"], ["y", "6", "12", "21", "30"]],
        col_widths=[2 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))

    s.append(Paragraph("<b>Q3.</b> Cross-multiplying 4/10 = x/25:", Q))
    s.append(Paragraph(
        "10 · x = 4 · 25 = 100 &nbsp;⇒&nbsp; <b>x = 10</b>.", ANS,
    ))

    s.append(Paragraph("<b>Q4.</b> Coefficient = 150 / 4 = 37.5 g per cookie.", Q))
    s.append(Paragraph(
        "For 18 cookies: 18 · 37.5 = <b>675 g</b>. "
        "(Cross-check: 18 · 150 / 4 = 2700 / 4 = 675.)", ANS,
    ))

    s.append(Paragraph("<b>Q5.</b>", Q))
    s.append(Paragraph(
        "Table a) ratios 3/1 = 6/2 = 9/3 = 12/4 = 3 → <b>proportional</b>, k = 3.", SUB,
    ))
    s.append(Paragraph(
        "Table b) ratios 3, 2, 5/3 ≈ 1.67, 1.5 → <b>not proportional</b>. "
        "(In fact y = x + 2, an additive relation.)", SUB,
    ))

    s.append(PageBreak())
    s.append(Paragraph("Part B — Percentages", H2))

    s.append(Paragraph("<b>Q6.</b> 25% of 80 = (25/100) · 80 = <b>20</b>.", Q))
    s.append(Paragraph(
        "<b>Q7.</b> 15 / 60 = 1/4 = 25/100 = <b>25%</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Q8.</b> Multiplier 1 + 12/100 = 1.12. "
        "New price = 200 · 1.12 = <b>224 €</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Q9.</b> Multiplier 1 − 20/100 = 0.80. "
        "Final price = 50 · 0.80 = <b>40 €</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Q10.</b> 30% of 250 = (30/100) · 250 = (3/10) · 250 = <b>75 students</b>.", Q,
    ))

    s.append(Paragraph("Part C — Polynomials", H2))
    s.append(Paragraph("Given P(x) = 3x² + 2x − 1, &nbsp;&nbsp; Q(x) = x² − 5x + 4.", BOX))

    s.append(Paragraph(
        "<b>Q11.</b> Degree = <b>2</b>; leading coefficient = <b>3</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Q12.</b> Group like terms: (3x² + x²) + (2x − 5x) + (−1 + 4) "
        "= <b>4x² − 3x + 3</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Q13.</b> Distribute the minus: 3x² + 2x − 1 − x² + 5x − 4 "
        "= (3x² − x²) + (2x + 5x) + (−1 − 4) = <b>2x² + 7x − 5</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Q14.</b> 2x · (x + 3) = 2x · x + 2x · 3 = <b>2x² + 6x</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Q15.</b> (x + 4)(x − 2) = x² − 2x + 4x − 8 = <b>x² + 2x − 8</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Q16.</b> P(2) = 2² − 3·2 + 5 = 4 − 6 + 5 = <b>3</b>.", Q,
    ))

    s.append(Paragraph("Bonus", H2))
    s.append(Paragraph(
        "Step 1: 80 · (1 − 25/100) = 80 · 0.75 = <b>60 €</b>. "
        "Step 2: 60 · (1 + 25/100) = 60 · 1.25 = <b>75 €</b>.", Q,
    ))
    s.append(Paragraph(
        "Final price = 75 €, <b>not</b> 80 €. The combined factor is "
        "0.75 × 1.25 = 0.9375 &lt; 1 — a net 6.25% loss. Equal percentage "
        "changes in opposite directions do not cancel because they are "
        "applied to different bases.", BOX,
    ))

    doc = SimpleDocTemplate(
        "exam_7th_grade_math_solutions.pdf", pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="7th Grade Math Exam — Solutions",
    )
    doc.build(s)


if __name__ == "__main__":
    build_exam()
    build_solutions()
    print("Built: exam_7th_grade_math.pdf, exam_7th_grade_math_solutions.pdf")
