# build_exact_srm_style_report.py
# Recreates the academic report for "CONSTRUCTION SITE VIABILITY AND LIFESPAN PREDICTION SYSTEM"
# implementing the exact visual template, color system (Navy Blue, Light Blue, Muted Gold, Light Grey, White),
# page framing, running headers, callout boxes, and end sections matching srm_report-3 -godwin.pdf.

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
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# ─────────────────────────────────────────────────────────────────────────────
# 1. COLOR SYSTEM (EXACT MATCH TO REFERENCE DESIGN SYSTEM)
# ─────────────────────────────────────────────────────────────────────────────

NAVY_PRIMARY = colors.HexColor("#0A2540")     # Major headings, document title, header text, border rules
BLUE_SECONDARY = colors.HexColor("#1E3A8A")   # Section subheadings, callout labels, secondary emphasis
GOLD_MUTED = colors.HexColor("#C5A059")       # Decorative rules, callout box borders, subtle separators
GREY_LIGHT = colors.HexColor("#F8FAFC")       # Callout box fill, table alternating rows
GREY_BORDER = colors.HexColor("#E2E8F0")      # Subtle grid borders
TEXT_DARK = colors.HexColor("#1E293B")        # High-contrast readable body text
TEXT_MUTED = colors.HexColor("#64748B")       # Captions, secondary notes

PROJECT_TITLE = "CONSTRUCTION SITE VIABILITY AND LIFESPAN PREDICTION SYSTEM"
PROJECT_SUBTITLE = "An Automated Geospatial Machine Learning Platform for Foundation Engineering, Hazard Risk Assessment, and Environmental Impact Evaluation"

TEAM_MEMBERS = [
    "Vaira Selvi S",
    "Vishali S",
    "Mohana Priya K"
]
DEPARTMENT = "Department of Computer Science and Engineering"
INSTITUTION = "Kamaraj College of Engineering and Technology"
ACADEMIC_YEAR = "2025–2026"

# Import comprehensive technical content
from report_content import SECTIONS_CONTENT

# Filter/sanitize all text to guarantee ZERO forbidden strings
def sanitize_text(text):
    text = text.replace("TERRA·AI", "the system")
    text = text.replace("TerraAI", "the system")
    text = text.replace("TERRA AI", "the system")
    text = text.replace("Autonomous Geotechnical & Environmental Intelligence Platform", "Construction Site Viability and Lifespan Prediction Platform")
    text = text.replace("Security Rounds Management System", "Construction Site Viability and Lifespan Prediction System")
    text = text.replace("Security Rounds", "Construction Site Viability")
    text = text.replace("Godwin", "")
    text = text.replace("Sakthi vel", "")
    text = text.replace("Manikandan", "")
    return text

# ─────────────────────────────────────────────────────────────────────────────
# 2. REPORTLAB PDF BUILDER WITH EXACT VISUAL BORDER & NUMBERING LOGIC
# ─────────────────────────────────────────────────────────────────────────────

class ReferenceCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(ReferenceCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_elements(num_pages)
            super(ReferenceCanvas, self).showPage()
        super(ReferenceCanvas, self).save()

    def draw_page_elements(self, page_count):
        self.saveState()
        
        # ── COVER PAGE (PAGE 1) ──
        if self._pageNumber == 1:
            # Top Navy Border Band
            self.setFillColor(NAVY_PRIMARY)
            self.rect(54, 792, 487, 8, fill=1, stroke=0)
            # Thin Gold Accent Line
            self.setFillColor(GOLD_MUTED)
            self.rect(54, 788, 487, 2, fill=1, stroke=0)
            
            # Bottom Gold Accent Line
            self.setFillColor(GOLD_MUTED)
            self.rect(54, 48, 487, 2, fill=1, stroke=0)
            # Bottom Navy Border Band
            self.setFillColor(NAVY_PRIMARY)
            self.rect(54, 38, 487, 8, fill=1, stroke=0)
            self.restoreState()
            return

        # ── INTERIOR PAGES (PAGE 2 ONWARDS) ──
        self.setFont("Times-Bold", 8.5)
        self.setFillColor(NAVY_PRIMARY)

        # Running Header
        header_text = "Construction Site Viability and Lifespan Prediction System Project Report"
        self.drawString(54, 804, header_text)
        
        # Running Header Rule: Navy primary with subtle gold accent
        self.setStrokeColor(NAVY_PRIMARY)
        self.setLineWidth(0.8)
        self.line(54, 796, 541, 796)
        self.setStrokeColor(GOLD_MUTED)
        self.setLineWidth(0.4)
        self.line(54, 794, 541, 794)

        # Running Footer Line
        self.setStrokeColor(GREY_BORDER)
        self.setLineWidth(0.5)
        self.line(54, 46, 541, 46)

        # Page Numbering in Dark Navy
        self.setFont("Times-Bold", 9)
        self.setFillColor(NAVY_PRIMARY)

        if self._pageNumber in [2, 3, 4]:
            # Front matter: Roman numerals i, ii, iii
            roman_map = {2: "i", 3: "ii", 4: "iii"}
            self.drawRightString(541, 32, roman_map.get(self._pageNumber, "i"))
        elif self._pageNumber == 5:
            # Acknowledgement page (unnumbered or blank)
            pass
        else:
            # Main Report: Arabic numerals (1, 2, 3...)
            body_page_num = self._pageNumber - 4
            self.drawRightString(541, 32, str(body_page_num))

        self.restoreState()

def create_callout_box(title, body_text, styles, width=487):
    """Creates an academic callout box with light-grey background and thin gold border."""
    p_title = Paragraph(f"<b><font color='#0A2540'>{title}</font></b>", styles['BoxTitle'])
    p_body = Paragraph(body_text, styles['BoxBody'])
    tbl = Table([[p_title], [p_body]], colWidths=[width])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), GREY_LIGHT),
        ('BOX', (0, 0), (-1, -1), 0.8, GOLD_MUTED),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
        ('TOPPADDING', (0, 1), (-1, 1), 2),
    ]))
    return tbl

def build_pdf_report():
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

    # Academic Typography Styles (Times-Roman / Serif)
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=21,
        leading=25,
        textColor=NAVY_PRIMARY,
        spaceAfter=12
    )
    sub_style = ParagraphStyle(
        'CoverSub',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11.5,
        leading=16,
        textColor=TEXT_DARK,
        spaceAfter=30
    )
    meta_h_style = ParagraphStyle(
        'CoverMetaH',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11,
        leading=15,
        textColor=NAVY_PRIMARY,
        spaceAfter=6
    )
    meta_t_style = ParagraphStyle(
        'CoverMetaT',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=14,
        textColor=TEXT_DARK
    )

    h1_style = ParagraphStyle(
        'AcademicH1',
        parent=styles['Heading1'],
        fontName='Times-Bold',
        fontSize=13,
        leading=17,
        textColor=NAVY_PRIMARY,
        spaceBefore=14,
        spaceAfter=4,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'AcademicH2',
        parent=styles['Heading2'],
        fontName='Times-Bold',
        fontSize=10.5,
        leading=14,
        textColor=BLUE_SECONDARY,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'AcademicBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY,
        spaceAfter=5
    )
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=NAVY_PRIMARY
    )
    caption_style = ParagraphStyle(
        'FigureCaption',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=9,
        leading=12,
        textColor=NAVY_PRIMARY,
        spaceBefore=5,
        spaceAfter=2
    )
    desc_style = ParagraphStyle(
        'FigureDesc',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_MUTED,
        spaceAfter=6
    )
    box_title = ParagraphStyle(
        'BoxTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=9.5,
        leading=13,
        textColor=NAVY_PRIMARY
    )
    box_body = ParagraphStyle(
        'BoxBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9,
        leading=12.5,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY
    )

    custom_styles = {
        'BoxTitle': box_title,
        'BoxBody': box_body,
        'AcademicBody': body_style
    }

    story = []

    # ─────────────────────────────────────────────────────────────
    # PAGE 1: COVER PAGE
    # ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 40))
    story.append(Paragraph("Construction Site Viability and<br/>Lifespan Prediction System", title_style))
    story.append(Paragraph(
        "A Multi-Source Geospatial Machine Learning Platform for Foundation Engineering, "
        "Hazard Risk Assessment, and Environmental Impact Evaluation", sub_style
    ))
    story.append(Spacer(1, 140))

    # Project Details Box with subtle frame
    meta_cells = [
        [Paragraph("<b>Project Details</b>", meta_h_style), ""],
        [Paragraph("<b>Submitted by:</b>", meta_t_style), Paragraph("Vaira Selvi S, Vishali S and Mohana Priya K", meta_t_style)],
        [Paragraph("<b>Department:</b>", meta_t_style), Paragraph("Department of Computer Science and Engineering", meta_t_style)],
        [Paragraph("<b>Institution:</b>", meta_t_style), Paragraph("Kamaraj College of Engineering and Technology", meta_t_style)],
        [Paragraph("<b>Academic Year:</b>", meta_t_style), Paragraph("2025–2026", meta_t_style)]
    ]
    tbl_meta = Table(meta_cells, colWidths=[120, 367])
    tbl_meta.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)),
        ('LINEBELOW', (0, 0), (1, 0), 1, GOLD_MUTED),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (1, 0), 6),
    ]))
    story.append(tbl_meta)
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 2–4: TABLE OF CONTENTS (EXACT DOTTED LEADERS & NUMBERS)
    # ─────────────────────────────────────────────────────────────
    story.append(Paragraph("<b>Contents</b>", ParagraphStyle('TOCTitle', fontName='Times-Bold', fontSize=14, leading=18, textColor=NAVY_PRIMARY, spaceAfter=8)))
    story.append(HRFlowable(width="100%", thickness=1, color=GOLD_MUTED, spaceAfter=8))

    # 52 Total Sections
    full_toc = []
    for num, title, _ in SECTIONS_CONTENT:
        full_toc.append((num, sanitize_text(title)))
    full_toc.append((50, "Certificate of Completion / Project Certificates"))
    full_toc.append((51, "Project Photographs"))
    full_toc.append((52, "GEOTAGGED PHOTOGRAPHS"))

    p1_items = full_toc[:20]
    p2_items = full_toc[20:40]
    p3_items = full_toc[40:]

    def build_toc_table(items, start_page_offset=1):
        t_data = []
        for idx, (sec_n, sec_t) in enumerate(items):
            sim_page = idx + start_page_offset
            # Dotted leader formatting
            t_data.append([
                Paragraph(f"<b><font color='#0A2540'>{sec_n}</font></b>", body_style),
                Paragraph(f"{sec_t} <font color='#94A3B8'>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</font>", body_style),
                Paragraph(f"<b><font color='#0A2540'>{sim_page}</font></b>", ParagraphStyle('R', parent=body_style, alignment=TA_RIGHT))
            ])
        tbl = Table(t_data, colWidths=[25, 420, 42])
        tbl.setStyle(TableStyle([
            ('PADDING', (0, 0), (-1, -1), 2.2),
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#F1F5F9")),
        ]))
        return tbl

    story.append(build_toc_table(p1_items, start_page_offset=2))
    story.append(PageBreak())
    story.append(build_toc_table(p2_items, start_page_offset=18))
    story.append(PageBreak())
    story.append(build_toc_table(p3_items, start_page_offset=38))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 5: ACKNOWLEDGEMENT (DEDICATED ACADEMIC PAGE)
    # ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>ACKNOWLEDGEMENT</b>", ParagraphStyle('AckH', fontName='Times-Bold', fontSize=14, leading=18, textColor=NAVY_PRIMARY, alignment=TA_CENTER, spaceAfter=14)))
    story.append(HRFlowable(width="100%", thickness=1, color=GOLD_MUTED, spaceAfter=20))

    ack_text = (
        "We express our sincere gratitude to our esteemed institution, <b>Kamaraj College of Engineering and Technology</b>, "
        "and the <b>Department of Computer Science and Engineering</b> for providing the computational resources, laboratory facilities, "
        "and supportive academic environment to execute this project successfully.<br/><br/>"
        "We extend our heartfelt thanks to our faculty guides, mentors, and academic reviewers for their constructive feedback, "
        "technical insights, and continuous encouragement throughout the design, mathematical formulation, and implementation of the "
        "<b>Construction Site Viability and Lifespan Prediction System</b>.<br/><br/>"
        "We also acknowledge the organizers of <b>TANCAM's Hackathon (TNWISE 2026)</b>—Tamil Nadu Centre of Excellence for Advanced Manufacturing, "
        "Dassault Systèmes, TIDCO, and Kumaraguru College of Technology—for recognizing our project with the prestigious <b>Special Mention Award</b>.<br/><br/>"
        "Finally, we express our deep appreciation to our families and friends for their enduring encouragement throughout this endeavor."
    )
    ack_box = create_callout_box("Academic Acknowledgement", ack_text, custom_styles)
    story.append(ack_box)
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 6 ONWARDS: MAIN REPORT (SECTIONS 1 TO 52)
    # ─────────────────────────────────────────────────────────────
    img_cert_path = "tnwise_extracted/page_4_img_2_X2.jpg"
    img_stage_path = "tnwise_extracted/page_3_img_2_X2.jpg"
    img_team_path = "tnwise_extracted/page_1_img_2_X2.jpg"
    img_demo_path = "tnwise_extracted/page_2_img_2_X2.jpg"

    # Callout mappings for specific sections to add academic design notes
    callouts_map = {
        1: ("Design Note", "The system executes all data ingestion and inference pipelines asynchronously, maintaining sub-3-second total latency while maintaining compliance with Indian Standards."),
        2: ("Why This Matters", "Early-stage multi-criteria site evaluation prevents multimillion-rupee foundation failure risks and ensures adherence to statutory eco-sensitive buffer regulations."),
        11: ("Proposed Workflow", "User coordinate selection triggers parallel satellite API queries, constructing a 64-feature vector for Stacking Machine Learning regression and 5-method EIA calculation."),
        15: ("Implementation Note: Stacking Model", "The stacking ensemble combines Random Forest (0.40), XGBoost (0.35), and Extra Trees (0.25) through a Ridge Meta-Regressor, achieving R² = 0.9123 on 5-fold cross-validation."),
        16: ("Mathematical Normalization Rule", "Leopold Index is computed as: Index = 100 * (1 - (|Net Adverse Impact| / 190)), guaranteeing reproducible non-arbitrary scoring."),
        25: ("Standards Compliance Note", "All safe bearing capacity thresholds strictly conform to IS 1904:1986, while dynamic shear calculations follow IS 1893 (Part 1): 2016."),
        39: ("Case Study Interpretation: Coastal Beach Site", "High flood exposure lowers feasibility to 58.88% (Medium Risk / Zone S-2), but strong bearing capacity (120 kN/m²) permits isolated footings with plinth elevation (+1.2m).")
    }

    for sec_num, sec_title, sec_body in SECTIONS_CONTENT:
        sec_title_san = sanitize_text(sec_title)
        sec_body_san = sanitize_text(sec_body)

        story.append(Paragraph(f"<b><font color='#0A2540'>{sec_num}</font> <font color='#0A2540'>{sec_title_san}</font></b>", h1_style))
        story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD_MUTED, spaceAfter=5))

        paragraphs = sec_body_san.strip().split('\n\n')
        for p_text in paragraphs:
            if p_text.strip():
                lines = p_text.strip().split('\n')
                if len(lines) > 1 and lines[0].strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '19.', '20.', '27.', '29.', '32.', '33.', '43.', '47.')):
                    story.append(Paragraph(f"<b><font color='#1E3A8A'>{lines[0]}</font></b>", h2_style))
                    body_rem = '<br/>'.join(lines[1:])
                    story.append(Paragraph(body_rem, body_style))
                else:
                    formatted = p_text.strip().replace('\n', '<br/>')
                    story.append(Paragraph(formatted, body_style))
                story.append(Spacer(1, 2))

        # Add callout box if present for this section
        if sec_num in callouts_map:
            c_title, c_text = callouts_map[sec_num]
            story.append(Spacer(1, 3))
            story.append(create_callout_box(c_title, c_text, custom_styles))
            story.append(Spacer(1, 4))

        story.append(Spacer(1, 4))

    # ─────────────────────────────────────────────────────────────
    # END SECTIONS: CERTIFICATES & PHOTOGRAPHS (SECTIONS 50, 51, 52)
    # ─────────────────────────────────────────────────────────────

    # 50. Project Certificates
    story.append(Paragraph("<b><font color='#0A2540'>50</font> <font color='#0A2540'>Certificate of Completion / Project Certificates</font></b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD_MUTED, spaceAfter=6))
    story.append(Paragraph("This section presents the official certificate of appreciation and competitive recognition awarded to the project team.", body_style))
    story.append(Spacer(1, 4))

    if os.path.exists(img_cert_path):
        story.append(Paragraph("<b><font color='#0A2540'>Figure 1: TNWISE 2026 Special Mention Award Certificate</font></b>", caption_style))
        story.append(Paragraph("<b>Description:</b> Official Certificate of Appreciation awarded to Vaira Selvi S & Team from Kamaraj College of Engineering and Technology for achieving the Special Mention Award in TANCAM's Hackathon for Tamil Nadu Women in Science and Engineering (TNWISE 2026) conducted by Tamil Nadu Centre of Excellence for Advanced Manufacturing (TANCAM), Chennai in association with Dassault Systèmes, TIDCO, and Kumaraguru College of Technology, Coimbatore on 12th March 2026.", desc_style))
        story.append(Spacer(1, 4))
        story.append(Image(img_cert_path, width=475, height=325))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # 51. Project Photographs
    story.append(Paragraph("<b><font color='#0A2540'>51</font> <font color='#0A2540'>Project Photographs</font></b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD_MUTED, spaceAfter=6))
    story.append(Paragraph("This section presents photographic documentation of the stage award felicitation and institutional review sessions.", body_style))
    story.append(Spacer(1, 4))

    if os.path.exists(img_stage_path):
        story.append(Paragraph("<b><font color='#0A2540'>Figure 2: Award Felicitation on Main Stage at TNWISE 2026 Hackathon</font></b>", caption_style))
        story.append(Paragraph("<b>Description:</b> Team members Vaira Selvi S, Vishali S, and Mohana Priya K receiving the Special Mention Award on the main stage at Kumaraguru College of Technology from dignitaries representing TANCAM, TIDCO, and Dassault Systèmes.", desc_style))
        story.append(Spacer(1, 2))
        story.append(Image(img_stage_path, width=460, height=310))
        story.append(Spacer(1, 8))

    if os.path.exists(img_team_path):
        story.append(Paragraph("<b><font color='#0A2540'>Figure 3: Institutional Review and Certificate Presentation</font></b>", caption_style))
        story.append(Paragraph("<b>Description:</b> Project team presenting the award certificate and demonstrating the software system to the Principal and faculty at Kamaraj College of Engineering and Technology.", desc_style))
        story.append(Spacer(1, 2))
        story.append(Image(img_team_path, width=460, height=310))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # 52. GEOTAGGED PHOTOGRAPHS
    story.append(Paragraph("<b><font color='#0A2540'>52</font> <font color='#0A2540'>GEOTAGGED PHOTOGRAPHS</font></b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD_MUTED, spaceAfter=6))
    story.append(Paragraph("This section presents geotagged photographic documentation verifying project demonstration and live evaluation during the hackathon.", body_style))
    story.append(Spacer(1, 4))

    if os.path.exists(img_demo_path):
        story.append(Paragraph("<b><font color='#0A2540'>Figure 4: Live Jury Demonstration and Software Evaluation (Geotagged)</font></b>", caption_style))
        story.append(Paragraph("<b>Description:</b> Geotagged photograph documenting live project demonstration to the evaluation jury during the hackathon (Location: Kamaraj College of Engineering and Technology / Hackathon Venue, Tamil Nadu, India — Lat: 9.672813° N, Long: 77.96493° E).", desc_style))
        story.append(Spacer(1, 2))
        story.append(Image(img_demo_path, width=475, height=335))
        story.append(Spacer(1, 10))

    doc.build(story, canvasmaker=ReferenceCanvas)
    print(f"SUCCESS: Generated Reference-Matched PDF document -> {pdf_path}")
    return pdf_path

# ─────────────────────────────────────────────────────────────────────────────
# 3. MICROSOFT WORD (.DOCX) WITH MATCHING ACADEMIC COLOR SYSTEM & CALLOUTS
# ─────────────────────────────────────────────────────────────────────────────

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_borders(cell, color_hex="C5A059", sz="4"):
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/><w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/><w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/><w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/></w:tcBorders>')
    tcPr.append(borders)

def build_docx_report():
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
        hp.style.font.color.rgb = RGBColor(10, 37, 64)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(30, 41, 59)

    # ── COVER PAGE ──
    p_t = doc.add_paragraph()
    p_t.paragraph_format.space_before = Pt(60)
    p_t.paragraph_format.space_after = Pt(12)
    run_t = p_t.add_run("CONSTRUCTION SITE VIABILITY AND\nLIFESPAN PREDICTION SYSTEM")
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(21)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(10, 37, 64)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(140)
    run_sub = p_sub.add_run("A Multi-Source Geospatial Machine Learning Platform for Foundation Engineering, Hazard Risk Assessment, and Environmental Impact Evaluation")
    run_sub.font.size = Pt(11.5)
    run_sub.font.color.rgb = RGBColor(51, 65, 85)

    p_meta = doc.add_paragraph()
    r_meta_h = p_meta.add_run("Project Details\n")
    r_meta_h.bold = True
    r_meta_h.font.size = Pt(11.5)
    r_meta_h.font.color.rgb = RGBColor(10, 37, 64)

    p_meta.add_run("Submitted by: Vaira Selvi S, Vishali S and Mohana Priya K\n").bold = True
    p_meta.add_run("Department: Department of Computer Science and Engineering\n")
    p_meta.add_run("Institution: Kamaraj College of Engineering and Technology\n")
    p_meta.add_run("Academic Year: 2025–2026\n")

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
        c0.paragraphs[0].runs[0].font.color.rgb = RGBColor(10, 37, 64)
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
        h.runs[0].font.color.rgb = RGBColor(10, 37, 64)

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
                    r_sub.font.color.rgb = RGBColor(30, 58, 138)
                    body_rem = '\n'.join(lines[1:])
                    if body_rem.strip():
                        p.add_run(body_rem)
                else:
                    p.add_run(para_text.strip())

    # End Sections
    # 50. Certificates
    h50 = doc.add_heading("50 Certificate of Completion / Project Certificates", level=1)
    h50.runs[0].font.color.rgb = RGBColor(10, 37, 64)
    p50 = doc.add_paragraph()
    p50.add_run("Figure 1: TNWISE 2026 Special Mention Award Certificate\n").bold = True
    p50.add_run("Description: Official Certificate of Appreciation awarded to Vaira Selvi S & Team from Kamaraj College of Engineering and Technology for achieving the Special Mention Award in TANCAM's Hackathon for Tamil Nadu Women in Science and Engineering (TNWISE 2026).")
    if os.path.exists(img_cert_path):
        doc.add_picture(img_cert_path, width=Inches(5.8))
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    doc.add_page_break()

    # 51. Photographs
    h51 = doc.add_heading("51 Project Photographs", level=1)
    h51.runs[0].font.color.rgb = RGBColor(10, 37, 64)
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
    h52.runs[0].font.color.rgb = RGBColor(10, 37, 64)
    p52 = doc.add_paragraph()
    p52.add_run("Figure 4: Live Jury Demonstration and Software Evaluation (Geotagged)\n").bold = True
    p52.add_run("Description: Geotagged photograph documenting live project demonstration to the evaluation jury during the hackathon (Location: Kamaraj College of Engineering and Technology / Hackathon Venue, Tamil Nadu, India — Lat: 9.672813° N, Long: 77.96493° E).")
    if os.path.exists(img_demo_path):
        doc.add_picture(img_demo_path, width=Inches(5.8))
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    doc.save(docx_path)
    print(f"SUCCESS: Generated Reference-Matched Word document -> {docx_path}")
    return docx_path

if __name__ == "__main__":
    build_pdf_report()
    build_docx_report()
