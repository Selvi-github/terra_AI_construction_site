# generate_pdf_report.py
# Generates publication-ready PDF report matching the 49-section template and TNWISE award

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from report_content import SECTIONS_CONTENT

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return # Skip cover page
        
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header
        self.drawString(54, 800, "TERRA·AI — Autonomous Geotechnical & Environmental Intelligence Platform")
        self.drawRightString(541, 800, "Project Report")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 792, 541, 792)
        
        # Footer
        self.line(54, 45, 541, 45)
        self.drawString(54, 32, "Kamaraj College of Engineering and Technology | TNWISE 2026 Special Mention Award")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(541, 32, page_str)
        self.restoreState()

def build_full_pdf():
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
    
    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#0E7490"),
        alignment=1, # Center
        spaceAfter=10
    )
    sub_style = ParagraphStyle(
        'CoverSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#1E293B"),
        alignment=1,
        spaceAfter=12
    )
    desc_style = ParagraphStyle(
        'CoverDesc',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#64748B"),
        alignment=1,
        spaceAfter=20
    )
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#0E7490"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155"),
        spaceAfter=5
    )
    box_text = ParagraphStyle(
        'BoxText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#166534"),
        alignment=1
    )

    story = []

    # ── COVER PAGE ──
    story.append(Spacer(1, 30))
    story.append(Paragraph("TERRA·AI", title_style))
    story.append(Paragraph("Autonomous Geotechnical & Environmental Intelligence Platform<br/>for Construction Site Selection & Academic EIA", sub_style))
    story.append(Paragraph("An AI-Driven Multi-Source Geospatial Decision Support System Integrating<br/>5 Environmental Impact Assessment Methodologies, Stacking ML Regressors, and 3D Hazard Simulation", desc_style))
    story.append(Spacer(1, 10))

    # Award Banner Table
    award_p = Paragraph("<b>🏆 STATE-LEVEL HACKATHON AWARD RECOGNITION</b><br/>Winner of <b>SPECIAL MENTION AWARD</b> in TANCAM's Hackathon (TNWISE 2026)<br/>Organized by Tamil Nadu Centre of Excellence for Advanced Manufacturing (TANCAM),<br/>Dassault Systèmes, TIDCO & Kumaraguru College of Technology, Coimbatore", box_text)
    tbl_award = Table([[award_p]], colWidths=[487])
    tbl_award.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F0FDF4")),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#86EFAC")),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(tbl_award)
    story.append(Spacer(1, 40))

    # Project Details Table
    meta_data = [
        [Paragraph("<b>Project Details</b>", ParagraphStyle('W', fontName='Helvetica-Bold', textColor=colors.white, fontSize=10)), ""],
        [Paragraph("<b>Submitted by:</b>", body_style), Paragraph("Selvi. Vaira Selvi & Team", body_style)],
        [Paragraph("<b>Institution:</b>", body_style), Paragraph("Kamaraj College of Engineering and Technology, Tamil Nadu", body_style)],
        [Paragraph("<b>Department:</b>", body_style), Paragraph("Department of Computer Science and Engineering", body_style)],
        [Paragraph("<b>Academic Year:</b>", body_style), Paragraph("2025 – 2026", body_style)]
    ]
    tbl_meta = Table(meta_data, colWidths=[140, 347])
    tbl_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor("#0E7490")),
        ('SPAN', (0, 0), (1, 0)),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(tbl_meta)
    story.append(PageBreak())

    # ── CERTIFICATE & HACKATHON GALLERY PAGE ──
    story.append(Paragraph("TNWISE 2026 Hackathon Special Mention Award", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0E7490"), spaceAfter=10))
    story.append(Paragraph(
        "The TerraAI platform was presented and defended at the state-level TANCAM's Hackathon: <b>TNWISE 2026</b> "
        "(Exclusive for Tamil Nadu Women in Science and Engineering), organized by the <b>Tamil Nadu Centre of Excellence "
        "for Advanced Manufacturing (TANCAM)</b> in association with <b>Dassault Systèmes, TIDCO, and Kumaraguru College of Technology, Coimbatore</b> "
        "on 12th March 2026. The project won the prestigious <b>SPECIAL MENTION AWARD</b> for its novel integration of automated "
        "geospatial sensing, civil engineering Indian Standards (IS Codes), and machine learning stacking ensembles.",
        body_style
    ))
    story.append(Spacer(1, 8))

    img_cert_path = "tnwise_extracted/page_4_img_2_X2.jpg"
    if os.path.exists(img_cert_path):
        story.append(Paragraph("<b>Figure A: Official Certificate of Appreciation — TNWISE 2026 Special Mention Award</b>", h2_style))
        story.append(Image(img_cert_path, width=480, height=330))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    story.append(Paragraph("Hackathon Evaluation, Stage Felicitation & Institutional Demonstration", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0E7490"), spaceAfter=10))

    img_stage_path = "tnwise_extracted/page_3_img_2_X2.jpg"
    img_demo_path = "tnwise_extracted/page_2_img_2_X2.jpg"
    img_team_path = "tnwise_extracted/page_1_img_2_X2.jpg"

    gallery_data = []
    if os.path.exists(img_stage_path) and os.path.exists(img_demo_path):
        cell_stage = [Paragraph("<b>Award Ceremony on Main Stage:</b>", body_style), Image(img_stage_path, width=235, height=160)]
        cell_demo = [Paragraph("<b>Live Jury Demonstration (Geotagged):</b>", body_style), Image(img_demo_path, width=235, height=160)]
        gallery_data.append([cell_stage, cell_demo])

    if os.path.exists(img_team_path):
        cell_team = [Paragraph("<b>Institutional Presentation & Certificate:</b>", body_style), Image(img_team_path, width=235, height=160)]
        p_eval = Paragraph("<b>Hackathon Jury Review Highlights:</b><br/>"
                           "• Commended for automated multi-domain satellite ETL pipeline eliminating manual survey delays.<br/>"
                           "• Highly rated for mathematical consistency across 5 standard EIA methodologies.<br/>"
                           "• Praised for intuitive 3D WebGL structural hazard reaction simulations.", body_style)
        gallery_data.append([cell_team, p_eval])

    if gallery_data:
        tbl_gal = Table(gallery_data, colWidths=[240, 240])
        tbl_gal.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(tbl_gal)

    story.append(PageBreak())

    # ── TABLE OF CONTENTS ──
    story.append(Paragraph("Table of Contents", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0E7490"), spaceAfter=10))

    toc_table_data = []
    for num, title, _ in SECTIONS_CONTENT:
        toc_table_data.append([
            Paragraph(f"<b>{num}</b>", body_style),
            Paragraph(title, body_style),
            Paragraph(f"{num+1}", ParagraphStyle('R', parent=body_style, alignment=2))
        ])

    tbl_toc = Table(toc_table_data, colWidths=[35, 410, 42])
    tbl_toc.setStyle(TableStyle([
        ('PADDING', (0, 0), (-1, -1), 2.2),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#F1F5F9")),
    ]))
    story.append(tbl_toc)
    story.append(PageBreak())

    # ── ALL 49 SECTIONS ──
    for sec_num, sec_title, sec_body in SECTIONS_CONTENT:
        story.append(Paragraph(f"{sec_num}. {sec_title}", h1_style))
        story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#CBD5E1"), spaceAfter=6))
        
        paragraphs = sec_body.strip().split('\n\n')
        for p_text in paragraphs:
            if p_text.strip():
                lines = p_text.strip().split('\n')
                if len(lines) > 1 and lines[0].strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '19.', '20.', '27.', '29.', '32.', '33.', '43.', '47.')):
                    story.append(Paragraph(f"<b>{lines[0]}</b>", h2_style))
                    body_remainder = '<br/>'.join(lines[1:])
                    story.append(Paragraph(body_remainder, body_style))
                else:
                    formatted_text = p_text.strip().replace('\n', '<br/>')
                    story.append(Paragraph(formatted_text, body_style))
                story.append(Spacer(1, 3))
        story.append(Spacer(1, 6))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"SUCCESS: Generated PDF document -> {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    build_full_pdf()
