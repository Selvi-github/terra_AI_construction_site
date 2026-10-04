# build_exact_reference_pdf.py
# Recreates the academic report for "CONSTRUCTION SITE VIABILITY AND LIFESPAN PREDICTION SYSTEM"
# precisely matching the visual design, cover page geometry, full-bleed top/bottom navy bands,
# gold accent lines, centered serif typography, rounded project details box, and interior layout of srm_report-3 -godwin.pdf.

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_borders(cell, color_hex="C5A059", sz="6"):
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)

# ─────────────────────────────────────────────────────────────────────────────
# 1. COLOR PALETTE (EXACT DIGITAL SAMPLING FROM REFERENCE PDF)
# ─────────────────────────────────────────────────────────────────────────────

NAVY_BAND = colors.HexColor("#0B2341")        # Edge-to-edge top and bottom cover bands
NAVY_TITLE = colors.HexColor("#0D3B66")       # Cover title & major chapter headings
BLUE_SUB = colors.HexColor("#2563EB")         # Italic subtitle & subsection headings
GOLD_ACCENT = colors.HexColor("#C5A059")      # Gold separator rules and box borders
BG_BOX = colors.HexColor("#FBFBFA")           # Subtle off-white/grey callout box fill
BORDER_GREY = colors.HexColor("#CBD5E1")      # Hairline running header/footer rules
TEXT_DARK = colors.HexColor("#1E293B")        # High-contrast readable body text
TEXT_MUTED = colors.HexColor("#64748B")       # Figure captions & secondary metadata

PROJECT_TITLE = "Construction Site Viability and\nLifespan Prediction System"
PROJECT_SUBTITLE = "A Multi-Source Geospatial Machine Learning Platform for Foundation Engineering,\nHazard Risk Assessment, and Environmental Impact Evaluation"

TEAM_MEMBERS = [
    "Vaira Selvi S",
    "Vishali S",
    "Mohana Priya K"
]
DEPARTMENT = "Department of Computer Science and Engineering"
INSTITUTION = "Kamaraj College of Engineering and Technology"
ACADEMIC_YEAR = "2025–2026"

from report_content import SECTIONS_CONTENT

def sanitize_text(text):
    text = text.replace("Proposed TerraAI System", "Proposed Platform Architecture and Methodology")
    text = text.replace("Proposed TERRA·AI System", "Proposed Platform Architecture and Methodology")
    text = text.replace("The TerraAI platform", "The platform")
    text = text.replace("The TerraAI dashboard", "The system dashboard")
    text = text.replace("The TerraAI system", "The system")
    text = text.replace("TerraAI", "the platform")
    text = text.replace("TERRA·AI", "the platform")
    text = text.replace("TERRA AI", "the platform")
    text = text.replace("Terra-AI", "the platform")
    text = text.replace("Terra AI", "the platform")
    text = text.replace("Autonomous Geotechnical & Environmental Intelligence Platform", "Construction Site Viability and Lifespan Prediction Platform")
    text = text.replace("Security Rounds Management System", "Construction Site Viability and Lifespan Prediction System")
    text = text.replace("Security Rounds", "Construction Site Viability")
    text = text.replace("Godwin", "")
    text = text.replace("Sakthi vel", "")
    text = text.replace("Manikandan", "")
    return text

# ─────────────────────────────────────────────────────────────────────────────
# 2. EXACT CANVAS ENGINE (FULL-BLEED BANDS & RUNNING HEADERS)
# ─────────────────────────────────────────────────────────────────────────────

PAGE_W, PAGE_H = A4 # 595.276 x 841.89

class ExactReferenceCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(ExactReferenceCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(ExactReferenceCanvas, self).showPage()
        super(ExactReferenceCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()

        # ── COVER PAGE (PAGE 1): FULL-BLEED BANDS & GEOMETRY ──
        if self._pageNumber == 1:
            # Top Full-Bleed Navy Band (x=0 to 595.28, y=765 to 841.89)
            self.setFillColor(NAVY_BAND)
            self.rect(0, 765, PAGE_W, 76.89, fill=1, stroke=0)
            
            # Top Gold Accent Line (y=761 to 764, height 3pt)
            self.setFillColor(GOLD_ACCENT)
            self.rect(0, 761, PAGE_W, 3.5, fill=1, stroke=0)

            # Bottom Gold Accent Line (y=66 to 69, height 3pt)
            self.setFillColor(GOLD_ACCENT)
            self.rect(0, 66, PAGE_W, 3.5, fill=1, stroke=0)

            # Bottom Full-Bleed Navy Band (x=0 to 595.28, y=0 to 65)
            self.setFillColor(NAVY_BAND)
            self.rect(0, 0, PAGE_W, 65, fill=1, stroke=0)

            self.restoreState()
            return

        # ── INTERIOR PAGES (PAGE 2 ONWARDS) ──
        # Running Header
        self.setFont("Times-Roman", 9)
        self.setFillColor(NAVY_TITLE)
        header_title = "Construction Site Viability and Lifespan Prediction System Project Report"
        self.drawString(54, 804, header_title)

        # Hairline rule below running header
        self.setStrokeColor(BORDER_GREY)
        self.setLineWidth(0.6)
        self.line(54, 796, 541, 796)

        # Running Footer
        self.line(54, 46, 541, 46)
        self.setFont("Times-Roman", 9)
        self.setFillColor(NAVY_TITLE)

        if self._pageNumber in [2, 3, 4]:
            # Front matter roman numerals
            roman_pages = {2: "i", 3: "ii", 4: "iii"}
            self.drawRightString(541, 32, roman_pages.get(self._pageNumber, "i"))
        elif self._pageNumber == 5:
            # Acknowledgement page unnumbered in template
            pass
        else:
            # Main Report Arabic numerals starting from 1
            body_page = self._pageNumber - 5
            self.drawRightString(541, 32, str(body_page))

        self.restoreState()

def create_rounded_callout(title, content_paras, styles, width=400):
    """Creates a rounded-corner academic callout box with gold border matching reference."""
    table_content = []
    if title:
        table_content.append([Paragraph(f"<b><font color='#0D3B66'>{title}</font></b>", styles['BoxTitle'])])
    
    for p in content_paras:
        table_content.append([Paragraph(p, styles['BoxBody'])])

    tbl = Table(table_content, colWidths=[width])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_BOX),
        ('BOX', (0, 0), (-1, -1), 0.8, GOLD_ACCENT),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    return tbl

# ─────────────────────────────────────────────────────────────────────────────
# 3. PDF GENERATION PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

def build_pdf_document():
    pdf_path = "d:/construction_site_selection/construction_site_selection/TERRA_AI_PROJECT_REPORT.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Cover Typography (Exact match to reference)
    cover_title_style = ParagraphStyle(
        'ExactCoverTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=24,
        leading=28,
        textColor=NAVY_TITLE,
        alignment=TA_CENTER,
        spaceAfter=14
    )
    cover_sub_style = ParagraphStyle(
        'ExactCoverSub',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=12,
        leading=16,
        textColor=BLUE_SUB,
        alignment=TA_CENTER,
        spaceAfter=40
    )

    # Interior Typography
    h1_style = ParagraphStyle(
        'ExactH1',
        parent=styles['Heading1'],
        fontName='Times-Bold',
        fontSize=13,
        leading=17,
        textColor=NAVY_TITLE,
        spaceBefore=14,
        spaceAfter=4,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'ExactH2',
        parent=styles['Heading2'],
        fontName='Times-Bold',
        fontSize=10.5,
        leading=14,
        textColor=BLUE_SUB,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'ExactBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY,
        spaceAfter=5
    )
    caption_style = ParagraphStyle(
        'ExactCaption',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=9.5,
        leading=13,
        textColor=NAVY_TITLE,
        spaceBefore=6,
        spaceAfter=2
    )
    desc_style = ParagraphStyle(
        'ExactDesc',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9,
        leading=12.5,
        textColor=TEXT_MUTED,
        spaceAfter=8
    )
    box_title_style = ParagraphStyle(
        'BoxTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11,
        leading=15,
        textColor=NAVY_TITLE,
        alignment=TA_CENTER,
        spaceAfter=6
    )
    box_body_style = ParagraphStyle(
        'BoxBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=14,
        textColor=TEXT_DARK,
        alignment=TA_CENTER
    )

    custom_styles = {
        'BoxTitle': box_title_style,
        'BoxBody': box_body_style
    }

    story = []

    # ─────────────────────────────────────────────────────────────
    # PAGE 1: COVER PAGE (CENTERED TITLE & ROUNDED PROJECT DETAILS)
    # ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 130)) # Space below top full-bleed band
    story.append(Paragraph("Construction Site Viability and<br/>Lifespan Prediction System", cover_title_style))
    story.append(Paragraph("A Multi-Source Geospatial Machine Learning Platform for Foundation Engineering,<br/>Hazard Risk Assessment, and Environmental Impact Evaluation", cover_sub_style))
    story.append(Spacer(1, 24))

    # Centered Rounded Project Details Box (Exact match to reference page 1)
    meta_lines = [
        "<b>Submitted by:</b> Vaira Selvi S, Vishali S and Mohana Priya K",
        "<b>Department:</b> Department of Computer Science and Engineering",
        "<b>Institution:</b> Kamaraj College of Engineering and Technology",
        "<b>Academic Year:</b> 2025–2026"
    ]
    tbl_project_box = create_rounded_callout("Project Details", meta_lines, custom_styles, width=380)
    
    # Center the table in layout
    story.append(Table([[tbl_project_box]], colWidths=[487], style=[('ALIGN', (0,0), (-1,-1), 'CENTER')]))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 2–4: TABLE OF CONTENTS (EXACT DOTTED LEADERS & NUMBERS)
    # ─────────────────────────────────────────────────────────────
    story.append(Paragraph("<b>Contents</b>", ParagraphStyle('TOCTitle', fontName='Times-Bold', fontSize=14, leading=18, textColor=NAVY_TITLE, spaceAfter=8)))
    story.append(HRFlowable(width="100%", thickness=0.8, color=GOLD_ACCENT, spaceAfter=8))

    full_toc = []
    for num, title, _ in SECTIONS_CONTENT:
        full_toc.append((num, sanitize_text(title)))
    full_toc.append((50, "Certificate of Completion / Project Certificates"))
    full_toc.append((51, "Project Photographs"))
    full_toc.append((52, "GEOTAGGED PHOTOGRAPHS"))

    p1_items = full_toc[:20]
    p2_items = full_toc[20:40]
    p3_items = full_toc[40:]

    def render_toc_page(items, start_page_num):
        t_data = []
        for idx, (sec_n, sec_t) in enumerate(items):
            p_num = idx + start_page_num
            t_data.append([
                Paragraph(f"<b><font color='#0D3B66'>{sec_n}</font></b>", body_style),
                Paragraph(f"{sec_t} <font color='#94A3B8'>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</font>", body_style),
                Paragraph(f"<b><font color='#0D3B66'>{p_num}</font></b>", ParagraphStyle('R', parent=body_style, alignment=TA_RIGHT))
            ])
        tbl = Table(t_data, colWidths=[25, 420, 42])
        tbl.setStyle(TableStyle([
            ('PADDING', (0, 0), (-1, -1), 2.2),
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#F1F5F9")),
        ]))
        return tbl

    story.append(render_toc_page(p1_items, 1))
    story.append(PageBreak())
    story.append(render_toc_page(p2_items, 21))
    story.append(PageBreak())
    story.append(render_toc_page(p3_items, 41))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 5: ACKNOWLEDGEMENT (DEDICATED ACADEMIC PAGE)
    # ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>ACKNOWLEDGEMENT</b>", ParagraphStyle('AckH', fontName='Times-Bold', fontSize=14, leading=18, textColor=NAVY_TITLE, alignment=TA_CENTER, spaceAfter=14)))
    story.append(HRFlowable(width="100%", thickness=0.8, color=GOLD_ACCENT, spaceAfter=20))

    ack_paragraphs = [
        "We express our sincere gratitude to our esteemed institution, <b>Kamaraj College of Engineering and Technology</b>, and the <b>Department of Computer Science and Engineering</b> for providing the computational resources, laboratory facilities, and supportive academic environment to execute this project successfully.",
        "We extend our heartfelt thanks to our faculty guides, mentors, and academic reviewers for their constructive feedback, technical insights, and continuous encouragement throughout the design, mathematical formulation, and implementation of the <b>Construction Site Viability and Lifespan Prediction System</b>.",
        "We also acknowledge the organizers of <b>TANCAM's Hackathon (TNWISE 2026)</b>—Tamil Nadu Centre of Excellence for Advanced Manufacturing, Dassault Systèmes, TIDCO, and Kumaraguru College of Technology—for recognizing our project with the prestigious <b>Special Mention Award</b>.",
        "Finally, we express our deep appreciation to our families and friends for their enduring encouragement throughout this endeavor."
    ]
    ack_box = create_rounded_callout("Institutional Acknowledgement", ack_paragraphs, custom_styles, width=440)
    story.append(Table([[ack_box]], colWidths=[487], style=[('ALIGN', (0,0), (-1,-1), 'CENTER')]))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 6 ONWARDS: MAIN REPORT (SECTIONS 1 TO 52)
    # ─────────────────────────────────────────────────────────────
    img_cert_path = "tnwise_extracted/page_4_img_2_X2.jpg"
    img_stage_path = "tnwise_extracted/page_3_img_2_X2.jpg"
    img_team_path = "tnwise_extracted/page_1_img_2_X2.jpg"
    img_demo_path = "tnwise_extracted/page_2_img_2_X2.jpg"

    callouts_content = {
        1: ("Design Note", ["The system executes all data ingestion and inference pipelines asynchronously, maintaining sub-3-second total latency while maintaining compliance with Indian Standards."]),
        2: ("Why This Matters", ["Early-stage multi-criteria site evaluation prevents multimillion-rupee foundation failure risks and ensures adherence to statutory eco-sensitive buffer regulations."]),
        11: ("Proposed Workflow", ["User coordinate selection triggers parallel satellite API queries, constructing a 64-feature vector for Stacking Machine Learning regression and 5-method EIA calculation."]),
        15: ("Implementation Note: Stacking Model", ["The stacking ensemble combines Random Forest (0.40), XGBoost (0.35), and Extra Trees (0.25) through a Ridge Meta-Regressor, achieving R² = 0.9123 on 5-fold cross-validation."]),
        16: ("Mathematical Normalization Rule", ["Leopold Index is computed as: Index = 100 * (1 - (|Net Adverse Impact| / 190)), guaranteeing reproducible non-arbitrary scoring."]),
        25: ("Standards Compliance Note", ["All safe bearing capacity thresholds strictly conform to IS 1904:1986, while dynamic shear calculations follow IS 1893 (Part 1): 2016."]),
        39: ("Case Study Interpretation: Coastal Beach Site", ["High flood exposure lowers feasibility to 58.88% (Medium Risk / Zone S-2), but strong bearing capacity (120 kN/m²) permits isolated footings with plinth elevation (+1.2m)."])
    }

    for sec_num, sec_title, sec_body in SECTIONS_CONTENT:
        sec_title_san = sanitize_text(sec_title)
        sec_body_san = sanitize_text(sec_body)

        story.append(Paragraph(f"<b><font color='#0D3B66'>{sec_num}</font> <font color='#0D3B66'>{sec_title_san}</font></b>", h1_style))
        story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD_ACCENT, spaceAfter=5))

        paragraphs = sec_body_san.strip().split('\n\n')
        for p_text in paragraphs:
            if p_text.strip():
                lines = p_text.strip().split('\n')
                if len(lines) > 1 and lines[0].strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '19.', '20.', '27.', '29.', '32.', '33.', '43.', '47.')):
                    story.append(Paragraph(f"<b><font color='#2563EB'>{lines[0]}</font></b>", h2_style))
                    body_rem = '<br/>'.join(lines[1:])
                    story.append(Paragraph(body_rem, body_style))
                else:
                    formatted = p_text.strip().replace('\n', '<br/>')
                    story.append(Paragraph(formatted, body_style))
                story.append(Spacer(1, 2))

        # Insert callout box where defined
        if sec_num in callouts_content:
            c_title, c_paras = callouts_content[sec_num]
            story.append(Spacer(1, 4))
            c_box = create_rounded_callout(c_title, c_paras, custom_styles, width=460)
            story.append(Table([[c_box]], colWidths=[487], style=[('ALIGN', (0,0), (-1,-1), 'CENTER')]))
            story.append(Spacer(1, 4))

        story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # END SECTIONS: CERTIFICATES & PHOTOGRAPHS (50, 51, 52)
    # ─────────────────────────────────────────────────────────────

    # 50. Project Certificates
    story.append(Paragraph("<b><font color='#0D3B66'>50</font> <font color='#0D3B66'>Certificate of Completion / Project Certificates</font></b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD_ACCENT, spaceAfter=6))
    story.append(Paragraph("This section presents the official certificate of appreciation and competitive recognition awarded to the project team.", body_style))
    story.append(Spacer(1, 4))

    if os.path.exists(img_cert_path):
        story.append(Paragraph("<b><font color='#0D3B66'>Figure 1: TNWISE 2026 Special Mention Award Certificate</font></b>", caption_style))
        story.append(Paragraph("<b>Description:</b> Official Certificate of Appreciation awarded to Vaira Selvi S & Team from Kamaraj College of Engineering and Technology for achieving the Special Mention Award in TANCAM's Hackathon for Tamil Nadu Women in Science and Engineering (TNWISE 2026) conducted by Tamil Nadu Centre of Excellence for Advanced Manufacturing (TANCAM), Chennai in association with Dassault Systèmes, TIDCO, and Kumaraguru College of Technology, Coimbatore on 12th March 2026.", desc_style))
        story.append(Spacer(1, 4))
        story.append(Image(img_cert_path, width=475, height=325))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # 51. Project Photographs
    story.append(Paragraph("<b><font color='#0D3B66'>51</font> <font color='#0D3B66'>Project Photographs</font></b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD_ACCENT, spaceAfter=6))
    story.append(Paragraph("This section presents photographic documentation of the stage award felicitation and institutional review sessions.", body_style))
    story.append(Spacer(1, 4))

    if os.path.exists(img_stage_path) and os.path.exists(img_team_path):
        story.append(Paragraph("<b><font color='#0D3B66'>Figure 2: Award Felicitation on Main Stage &nbsp;|&nbsp; Figure 3: Institutional Review</font></b>", caption_style))
        story.append(Paragraph("<b>Description:</b> (Left) Team members Vaira Selvi S, Vishali S, and Mohana Priya K receiving the Special Mention Award on the main stage at Kumaraguru College of Technology from dignitaries representing TANCAM, TIDCO, and Dassault Systèmes. (Right) Project team presenting the award certificate and demonstrating the software system to the Principal and faculty at Kamaraj College of Engineering and Technology.", desc_style))
        story.append(Spacer(1, 4))
        
        img_table = Table([[
            Image(img_stage_path, width=230, height=275),
            Image(img_team_path, width=230, height=275)
        ]], colWidths=[238, 238])
        img_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('PADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(img_table)
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # 52. GEOTAGGED PHOTOGRAPHS
    story.append(Paragraph("<b><font color='#0D3B66'>52</font> <font color='#0D3B66'>GEOTAGGED PHOTOGRAPHS</font></b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD_ACCENT, spaceAfter=6))
    story.append(Paragraph("This section presents geotagged photographic documentation verifying project demonstration and live evaluation during the hackathon.", body_style))
    story.append(Spacer(1, 4))

    if os.path.exists(img_demo_path):
        story.append(Paragraph("<b><font color='#0D3B66'>Figure 4: Live Jury Demonstration and Software Evaluation (Geotagged)</font></b>", caption_style))
        story.append(Paragraph("<b>Description:</b> Geotagged photograph documenting live project demonstration to the evaluation jury during the hackathon (Location: Kamaraj College of Engineering and Technology / Hackathon Venue, Tamil Nadu, India — Lat: 9.672813° N, Long: 77.96493° E).", desc_style))
        story.append(Spacer(1, 2))
        story.append(Image(img_demo_path, width=475, height=335))
        story.append(Spacer(1, 10))

    doc.build(story, canvasmaker=ExactReferenceCanvas)
    print(f"SUCCESS: Generated Exact Reference-Matched PDF document -> {pdf_path}")
    return pdf_path

# ─────────────────────────────────────────────────────────────────────────────
# 4. MICROSOFT WORD (.DOCX) BUILDER (MATCHING CENTERED COVER & CALLOUTS)
# ─────────────────────────────────────────────────────────────────────────────

def build_docx_document():
    docx_path = "d:/construction_site_selection/construction_site_selection/TERRA_AI_PROJECT_REPORT.docx"
    doc = docx.Document()

    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)

        header = s.header
        hp = header.paragraphs[0]
        hp.text = "Construction Site Viability and Lifespan Prediction System Project Report"
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        hp.style.font.name = 'Times New Roman'
        hp.style.font.size = Pt(8.5)
        hp.style.font.bold = True
        hp.style.font.color.rgb = RGBColor(13, 59, 102)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(30, 41, 59)

    # ── COVER PAGE ──
    p_t = doc.add_paragraph()
    p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t.paragraph_format.space_before = Pt(80)
    p_t.paragraph_format.space_after = Pt(12)
    run_t = p_t.add_run("Construction Site Viability and\nLifespan Prediction System")
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(24)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(13, 59, 102)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(60)
    run_sub = p_sub.add_run("A Multi-Source Geospatial Machine Learning Platform for Foundation Engineering,\nHazard Risk Assessment, and Environmental Impact Evaluation")
    run_sub.font.name = 'Times New Roman'
    run_sub.font.italic = True
    run_sub.font.size = Pt(12)
    run_sub.font.color.rgb = RGBColor(37, 99, 235)

    # Project Details Box
    tbl_box = doc.add_table(rows=5, cols=1)
    tbl_box.alignment = WD_TABLE_ALIGNMENT.CENTER
    box_lines = [
        ("Project Details", True, RGBColor(13, 59, 102)),
        ("Submitted by: Vaira Selvi S, Vishali S and Mohana Priya K", True, RGBColor(30, 41, 59)),
        ("Department: Department of Computer Science and Engineering", False, RGBColor(30, 41, 59)),
        ("Institution: Kamaraj College of Engineering and Technology", False, RGBColor(30, 41, 59)),
        ("Academic Year: 2025–2026", False, RGBColor(30, 41, 59))
    ]
    for idx, (txt, is_b, col) in enumerate(box_lines):
        cell = tbl_box.cell(idx, 0)
        set_cell_background(cell, "FBFBFA")
        set_cell_borders(cell, color_hex="C5A059", sz="6")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(txt)
        r.bold = is_b
        r.font.color.rgb = col
        r.font.size = Pt(10)

    doc.add_page_break()

    # ── TABLE OF CONTENTS ──
    h_toc = doc.add_heading("Contents", level=1)
    h_toc.paragraph_format.space_after = Pt(10)

    full_toc = [(num, sanitize_text(title)) for num, title, _ in SECTIONS_CONTENT]
    full_toc.append((50, "Certificate of Completion / Project Certificates"))
    full_toc.append((51, "Project Photographs"))
    full_toc.append((52, "GEOTAGGED PHOTOGRAPHS"))

    tbl_toc = doc.add_table(rows=len(full_toc), cols=3)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (sec_no, sec_title) in enumerate(full_toc):
        c0 = tbl_toc.cell(idx, 0)
        c1 = tbl_toc.cell(idx, 1)
        c2 = tbl_toc.cell(idx, 2)
        c0.paragraphs[0].add_run(str(sec_no)).bold = True
        c0.paragraphs[0].runs[0].font.color.rgb = RGBColor(13, 59, 102)
        c1.paragraphs[0].add_run(sec_title)
        c2.paragraphs[0].add_run(str(idx + 2))
        c2.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

    doc.add_page_break()

    # ── ACKNOWLEDGEMENT ──
    h_ack = doc.add_heading("ACKNOWLEDGEMENT", level=1)
    h_ack.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h_ack.paragraph_format.space_before = Pt(60)
    h_ack.paragraph_format.space_after = Pt(20)

    p_ack = doc.add_paragraph()
    p_ack.paragraph_format.line_spacing = 1.2
    p_ack.add_run(
        "We express our sincere gratitude to our esteemed institution, Kamaraj College of Engineering and Technology, "
        "and the Department of Computer Science and Engineering for providing the computational resources, laboratory facilities, "
        "and supportive academic environment to execute this project successfully.\n\n"
        "We extend our heartfelt thanks to our faculty guides, mentors, and academic reviewers for their constructive feedback, "
        "technical insights, and continuous encouragement throughout the design, mathematical formulation, and implementation of the "
        "Construction Site Viability and Lifespan Prediction System.\n\n"
        "We also acknowledge the organizers of TANCAM's Hackathon (TNWISE 2026)—Tamil Nadu Centre of Excellence for Advanced Manufacturing, "
        "Dassault Systèmes, TIDCO, and Kumaraguru College of Technology—for recognizing our project with the Special Mention Award.\n\n"
        "Finally, we express our deep appreciation to our families and friends for their enduring support."
    )

    doc.add_page_break()

    # ── ALL 52 SECTIONS ──
    img_cert_path = "tnwise_extracted/page_4_img_2_X2.jpg"
    img_stage_path = "tnwise_extracted/page_3_img_2_X2.jpg"
    img_team_path = "tnwise_extracted/page_1_img_2_X2.jpg"
    img_demo_path = "tnwise_extracted/page_2_img_2_X2.jpg"

    for sec_num, sec_title, sec_body in SECTIONS_CONTENT:
        sec_title_san = sanitize_text(sec_title)
        sec_body_san = sanitize_text(sec_body)

        h = doc.add_heading(f"{sec_num} {sec_title_san}", level=1)
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(5)
        h.runs[0].font.name = 'Times New Roman'
        h.runs[0].font.color.rgb = RGBColor(13, 59, 102)

        for para_text in sec_body_san.strip().split('\n\n'):
            if para_text.strip():
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(5)
                p.paragraph_format.line_spacing = 1.15

                lines = para_text.strip().split('\n')
                if len(lines) > 1 and lines[0].strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '19.', '20.', '27.', '29.', '32.', '33.', '43.', '47.')):
                    r_sub = p.add_run(lines[0] + '\n')
                    r_sub.bold = True
                    r_sub.font.size = Pt(11)
                    r_sub.font.color.rgb = RGBColor(37, 99, 235)
                    body_rem = '\n'.join(lines[1:])
                    if body_rem.strip():
                        p.add_run(body_rem)
                else:
                    p.add_run(para_text.strip())

    # End Sections
    # 50. Certificates
    h50 = doc.add_heading("50 Certificate of Completion / Project Certificates", level=1)
    h50.runs[0].font.color.rgb = RGBColor(13, 59, 102)
    p50 = doc.add_paragraph()
    p50.add_run("Figure 1: TNWISE 2026 Special Mention Award Certificate\n").bold = True
    p50.add_run("Description: Official Certificate of Appreciation awarded to Vaira Selvi S & Team from Kamaraj College of Engineering and Technology for achieving the Special Mention Award in TANCAM's Hackathon for Tamil Nadu Women in Science and Engineering (TNWISE 2026).")
    if os.path.exists(img_cert_path):
        doc.add_picture(img_cert_path, width=Inches(5.8))
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    doc.add_page_break()

    # 51. Photographs
    h51 = doc.add_heading("51 Project Photographs", level=1)
    h51.runs[0].font.color.rgb = RGBColor(13, 59, 102)
    if os.path.exists(img_stage_path):
        p51a = doc.add_paragraph()
        p51a.add_run("Figure 2: Award Felicitation on Main Stage at TNWISE 2026 Hackathon\n").bold = True
        p51a.add_run("Description: Team members Vaira Selvi S, Vishali S, and Mohana Priya K receiving the Special Mention Award on the main stage at Kumaraguru College of Technology.")
        doc.add_picture(img_stage_path, width=Inches(5.6))
        doc.add_paragraph().paragraph_format.space_after = Pt(8)

    if os.path.exists(img_team_path):
        p51b = doc.add_paragraph()
        p51b.add_run("Figure 3: Institutional Review and Certificate Presentation\n").bold = True
        p51b.add_run("Description: Project team presenting the award certificate and demonstrating the software system to the Principal and faculty at Kamaraj College of Engineering and Technology.")
        doc.add_picture(img_team_path, width=Inches(5.6))
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    doc.add_page_break()

    # 52. Geotagged Photographs
    h52 = doc.add_heading("52 GEOTAGGED PHOTOGRAPHS", level=1)
    h52.runs[0].font.color.rgb = RGBColor(13, 59, 102)
    p52 = doc.add_paragraph()
    p52.add_run("Figure 4: Live Jury Demonstration and Software Evaluation (Geotagged)\n").bold = True
    p52.add_run("Description: Geotagged photograph documenting live project demonstration to the evaluation jury during the hackathon (Location: Kamaraj College of Engineering and Technology / Hackathon Venue, Tamil Nadu, India — Lat: 9.672813° N, Long: 77.96493° E).")
    if os.path.exists(img_demo_path):
        doc.add_picture(img_demo_path, width=Inches(5.8))
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    doc.save(docx_path)
    print(f"SUCCESS: Generated Exact Reference-Matched Word document -> {docx_path}")
    return docx_path

if __name__ == "__main__":
    build_pdf_document()
    build_docx_document()
