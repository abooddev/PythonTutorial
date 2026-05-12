"""Genere le devoir de mathematiques de 7eme annee et son corrige en PDF (francais)."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
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
# SUJET
# ─────────────────────────────────────────────────────────────────────────────


def build_exam():
    story = []
    story.append(Paragraph("Devoir de Mathématiques — 7<super>ème</super> année", TITLE))
    story.append(
        Paragraph(
            "Nom : ________________________ &nbsp;&nbsp; Date : ____________ "
            "<br/>Durée : 60 minutes &nbsp;&nbsp;|&nbsp;&nbsp; Total : 60 points "
            "<br/><i>Toutes les étapes du calcul doivent être justifiées. "
            "Calculatrice non autorisée.</i>",
            META,
        )
    )

    # ── Partie A
    story.append(Paragraph(
        "Partie A — Proportionnalité &amp; coefficient de proportionnalité (20 pts)", H2,
    ))

    story.append(Paragraph(
        "<b>Exercice 1.</b> (4 pts) Le tableau ci-dessous donne la distance "
        "parcourue par une voiture à vitesse constante.", Q,
    ))
    story.append(table_block(
        [["Temps (h)", "2", "3", "5", "7"],
         ["Distance (km)", "70", "105", "175", "245"]],
        col_widths=[3.5 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))
    story.append(Paragraph(
        "a) S'agit-il d'une situation de proportionnalité ? Justifier.", SUB,
    ))
    story.append(Paragraph(
        "b) Déterminer le <b>coefficient de proportionnalité</b> <i>k</i>.", SUB,
    ))
    story.append(Paragraph(
        "c) Donner une formule reliant la distance <i>d</i> au temps <i>t</i>.", SUB,
    ))

    story.append(Paragraph(
        "<b>Exercice 2.</b> (4 pts) Le tableau ci-dessous représente une "
        "situation de proportionnalité de coefficient <i>k</i> = 3. Compléter "
        "les cases manquantes :", Q,
    ))
    story.append(table_block(
        [["x", "2", "4", "?", "10"],
         ["y", "6", "?", "21", "?"]],
        col_widths=[2 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))

    story.append(Paragraph(
        "<b>Exercice 3.</b> (4 pts) Résoudre l'équation suivante en utilisant "
        "le <b>produit en croix</b> : &nbsp;&nbsp; 4 / 10 = x / 25.", Q,
    ))

    story.append(Paragraph(
        "<b>Exercice 4.</b> (4 pts) Pour préparer <b>4 biscuits</b>, une "
        "recette utilise <b>150 g de farine</b>. Quelle quantité de farine "
        "faut-il pour <b>18 biscuits</b> ?", Q,
    ))

    story.append(Paragraph(
        "<b>Exercice 5.</b> (4 pts) Pour chacun des tableaux suivants, "
        "indiquer s'il représente une situation de proportionnalité. Justifier.", Q,
    ))
    story.append(Paragraph("Tableau a)", SUB))
    story.append(table_block(
        [["x", "1", "2", "3", "4"], ["y", "3", "6", "9", "12"]],
        col_widths=[2 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))
    story.append(Paragraph("Tableau b)", SUB))
    story.append(table_block(
        [["x", "1", "2", "3", "4"], ["y", "3", "4", "5", "6"]],
        col_widths=[2 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))

    story.append(PageBreak())

    # ── Partie B
    story.append(Paragraph("Partie B — Pourcentages (20 pts)", H2))
    story.append(Paragraph(
        "<b>Exercice 6.</b> (3 pts) Calculer <b>25 % de 80</b>.", Q,
    ))
    story.append(Paragraph(
        "<b>Exercice 7.</b> (4 pts) Dans une classe de 60 élèves, 15 portent "
        "des lunettes. Quel <b>pourcentage</b> de la classe porte des lunettes ?", Q,
    ))
    story.append(Paragraph(
        "<b>Exercice 8.</b> (5 pts) Un vélo coûte <b>200 €</b>. Son prix "
        "augmente de <b>12 %</b>. Quel est le nouveau prix ?", Q,
    ))
    story.append(Paragraph(
        "<b>Exercice 9.</b> (4 pts) Une chemise coûte <b>50 €</b>. Elle est "
        "soldée à <b>−20 %</b>. Quel est le prix final ?", Q,
    ))
    story.append(Paragraph(
        "<b>Exercice 10.</b> (4 pts) Sur 250 élèves d'une école, <b>30 %</b> "
        "pratiquent un instrument de musique. Combien d'élèves pratiquent "
        "un instrument ?", Q,
    ))

    # ── Partie C
    story.append(Paragraph("Partie C — Expressions algébriques (20 pts)", H2))

    story.append(Paragraph(
        "<b>Exercice 11.</b> (3 pts) Parmi les monômes suivants, regrouper "
        "ceux qui sont <b>semblables</b> :", Q,
    ))
    story.append(Paragraph(
        "3x² &nbsp;;&nbsp; −2x &nbsp;;&nbsp; 5x² &nbsp;;&nbsp; 7 "
        "&nbsp;;&nbsp; −4x &nbsp;;&nbsp; 2x² &nbsp;;&nbsp; −1", BOX,
    ))

    story.append(Paragraph(
        "<b>Exercice 12.</b> (4 pts) Réduire l'expression algébrique "
        "suivante : <br/>&nbsp;&nbsp;&nbsp;&nbsp; "
        "A = 5x + 3 − 2x + 7 − x + 4.", Q,
    ))

    story.append(Paragraph(
        "<b>Exercice 13.</b> (4 pts) On donne &nbsp; E = 4x + 7 &nbsp; et "
        "&nbsp; F = 3x − 2. Calculer la <b>somme</b> E + F.", Q,
    ))

    story.append(Paragraph(
        "<b>Exercice 14.</b> (3 pts) Développer le produit : 3 × (2x + 5).", Q,
    ))
    story.append(Paragraph(
        "<b>Exercice 15.</b> (3 pts) Développer le produit : (x + 3)(x + 2).", Q,
    ))
    story.append(Paragraph(
        "<b>Exercice 16.</b> (3 pts) Calculer la valeur de l'expression "
        "E(x) = 2x² + 3x − 1 &nbsp; pour &nbsp; x = 2.", Q,
    ))

    # ── Bonus
    story.append(Paragraph("Bonus (+3 pts)", H2))
    story.append(Paragraph(
        "Un manteau coûte <b>80 €</b>. Il est d'abord soldé à <b>−25 %</b>, "
        "puis le prix soldé est augmenté de <b>25 %</b>. Le prix final est-il "
        "égal à <b>80 €</b> ? Justifier par un calcul.", Q,
    ))

    doc = SimpleDocTemplate(
        "exam_7th_grade_math.pdf", pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="Devoir de Maths 7eme",
    )
    doc.build(story)


# ─────────────────────────────────────────────────────────────────────────────
# CORRIGE
# ─────────────────────────────────────────────────────────────────────────────


def build_solutions():
    s = []
    s.append(Paragraph(
        "Devoir de Mathématiques — 7<super>ème</super> année · Corrigé détaillé",
        TITLE,
    ))
    s.append(Paragraph(
        "Tous les résultats numériques ci-dessous ont été vérifiés "
        "symboliquement avec SymPy via la compétence <i>math</i> fournie.",
        META,
    ))

    s.append(Paragraph(
        "Partie A — Proportionnalité &amp; coefficient de proportionnalité", H2,
    ))

    s.append(Paragraph("<b>Exercice 1.</b>", Q))
    s.append(Paragraph(
        "a) On calcule chaque rapport distance / temps : 70/2 = 35, "
        "105/3 = 35, 175/5 = 35, 245/7 = 35. Tous égaux → "
        "<b>il y a proportionnalité</b>.", SUB,
    ))
    s.append(Paragraph(
        "b) Coefficient de proportionnalité <b>k = 35</b> (km/h).", SUB,
    ))
    s.append(Paragraph("c) Formule : <b>d = 35 × t</b>.", ANS))

    s.append(Paragraph("<b>Exercice 2.</b> Avec k = 3, on a y = 3x.", Q))
    s.append(Paragraph(
        "x = 4 → y = 12 &nbsp;|&nbsp; y = 21 → x = 21 / 3 = 7 "
        "&nbsp;|&nbsp; x = 10 → y = 30.", SUB,
    ))
    s.append(table_block(
        [["x", "2", "4", "7", "10"], ["y", "6", "12", "21", "30"]],
        col_widths=[2 * cm, 2 * cm, 2 * cm, 2 * cm, 2 * cm],
    ))

    s.append(Paragraph(
        "<b>Exercice 3.</b> Produit en croix sur 4/10 = x/25 :", Q,
    ))
    s.append(Paragraph(
        "10 × x = 4 × 25 = 100 &nbsp;⇒&nbsp; <b>x = 10</b>.", ANS,
    ))

    s.append(Paragraph(
        "<b>Exercice 4.</b> Coefficient = 150 / 4 = 37,5 g par biscuit.", Q,
    ))
    s.append(Paragraph(
        "Pour 18 biscuits : 18 × 37,5 = <b>675 g</b>. "
        "(Vérification : 18 × 150 / 4 = 2700 / 4 = 675.)", ANS,
    ))

    s.append(Paragraph("<b>Exercice 5.</b>", Q))
    s.append(Paragraph(
        "Tableau a) rapports 3/1 = 6/2 = 9/3 = 12/4 = 3 → "
        "<b>proportionnel</b>, k = 3.", SUB,
    ))
    s.append(Paragraph(
        "Tableau b) rapports 3, 2, 5/3 ≈ 1,67, 1,5 → "
        "<b>non proportionnel</b>. (En réalité y = x + 2, "
        "relation additive et non multiplicative.)", SUB,
    ))

    s.append(PageBreak())
    s.append(Paragraph("Partie B — Pourcentages", H2))

    s.append(Paragraph(
        "<b>Exercice 6.</b> 25 % de 80 = (25 / 100) × 80 = <b>20</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Exercice 7.</b> 15 / 60 = 1/4 = 25/100 = <b>25 %</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Exercice 8.</b> Coefficient multiplicateur : 1 + 12/100 = 1,12. "
        "Nouveau prix = 200 × 1,12 = <b>224 €</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Exercice 9.</b> Coefficient multiplicateur : 1 − 20/100 = 0,80. "
        "Prix final = 50 × 0,80 = <b>40 €</b>.", Q,
    ))
    s.append(Paragraph(
        "<b>Exercice 10.</b> 30 % de 250 = (30 / 100) × 250 = (3 / 10) × 250 "
        "= <b>75 élèves</b>.", Q,
    ))

    s.append(Paragraph("Partie C — Expressions algébriques", H2))

    s.append(Paragraph(
        "<b>Exercice 11.</b> Regroupement des monômes semblables :", Q,
    ))
    s.append(Paragraph(
        "• Monômes en x² : <b>3x², 5x², 2x²</b><br/>"
        "• Monômes en x : <b>−2x, −4x</b><br/>"
        "• Termes constants : <b>7, −1</b>", SUB,
    ))

    s.append(Paragraph(
        "<b>Exercice 12.</b> On regroupe les termes semblables :", Q,
    ))
    s.append(Paragraph(
        "A = (5x − 2x − x) + (3 + 7 + 4) = 2x + 14. "
        "<br/>Donc &nbsp; <b>A = 2x + 14</b>.", ANS,
    ))

    s.append(Paragraph(
        "<b>Exercice 13.</b> E + F = (4x + 7) + (3x − 2) "
        "= (4x + 3x) + (7 − 2) = <b>7x + 5</b>.", Q,
    ))

    s.append(Paragraph(
        "<b>Exercice 14.</b> Distributivité simple : "
        "3 × (2x + 5) = 3 × 2x + 3 × 5 = <b>6x + 15</b>.", Q,
    ))

    s.append(Paragraph(
        "<b>Exercice 15.</b> Double distributivité : "
        "(x + 3)(x + 2) = x × x + x × 2 + 3 × x + 3 × 2 "
        "= x² + 2x + 3x + 6 = <b>x² + 5x + 6</b>.", Q,
    ))

    s.append(Paragraph(
        "<b>Exercice 16.</b> Pour x = 2 : "
        "E(2) = 2 × (2)² + 3 × 2 − 1 = 2 × 4 + 6 − 1 "
        "= 8 + 6 − 1 = <b>13</b>.", Q,
    ))

    s.append(Paragraph("Bonus", H2))
    s.append(Paragraph(
        "Étape 1 : 80 × (1 − 25/100) = 80 × 0,75 = <b>60 €</b>. "
        "Étape 2 : 60 × (1 + 25/100) = 60 × 1,25 = <b>75 €</b>.", Q,
    ))
    s.append(Paragraph(
        "Prix final = 75 €, <b>différent</b> de 80 €. "
        "Le coefficient global est 0,75 × 1,25 = 0,9375 &lt; 1, soit une "
        "<b>perte nette de 6,25 %</b>. Deux variations de même pourcentage "
        "en sens opposés ne se compensent pas, car elles s'appliquent à "
        "des bases différentes.", BOX,
    ))

    doc = SimpleDocTemplate(
        "exam_7th_grade_math_solutions.pdf", pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="Devoir de Maths 7eme — Corrige",
    )
    doc.build(s)


if __name__ == "__main__":
    build_exam()
    build_solutions()
    print("Générés : exam_7th_grade_math.pdf, exam_7th_grade_math_solutions.pdf")
