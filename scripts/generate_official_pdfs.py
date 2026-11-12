import os
import json
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_DIR = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\curriculum_pdf"
os.makedirs(PDF_DIR, exist_ok=True)

MASTER_JSON = r"E:\PYQ_Wovrix_Portal\competitive-exams-portal\database\competitive_syllabus_master.json"
with open(MASTER_JSON, "r", encoding="utf-8") as f:
    master_data = json.load(f)

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
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        # Header
        self.drawString(36, 810, "LEARNOSHA.IN • OFFICIAL NATIONAL CURRICULUM & WEIGHTAGE ARCHIVE")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 804, 559, 804)
        # Footer
        self.line(36, 38, 559, 38)
        self.drawString(36, 26, "Official Academic Attribution: National Medical Commission (NMC) / National Testing Agency (NTA)")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(559, 26, page_text)
        self.restoreState()

def build_neet_pdf():
    pdf_path = os.path.join(PDF_DIR, "NEET_UG_Official_Curriculum_and_Weightage.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=8
    )
    meta_box_style = ParagraphStyle(
        'MetaBox',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155')
    )
    sec_heading = ParagraphStyle(
        'SecHead',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=10,
        spaceAfter=6
    )
    th_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#ffffff')
    )
    td_ch = ParagraphStyle(
        'TDCh',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#0f172a')
    )
    td_sub = ParagraphStyle(
        'TDSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#64748b')
    )
    td_cell = ParagraphStyle(
        'TDCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#1e293b')
    )
    td_tier = ParagraphStyle(
        'TDTier',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#b91c1c')
    )
    td_topics = ParagraphStyle(
        'TDTopics',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#334155')
    )

    story = []
    story.append(Paragraph("NEET (UG) Official Syllabus & Statutory Chapter Weightage", title_style))
    story.append(Paragraph("ISSUED BY NATIONAL MEDICAL COMMISSION (NMC) & NATIONAL TESTING AGENCY (NTA)", subtitle_style))

    meta_text = (
        "<b>Examination Standard:</b> Total Marks: 720 | Total Questions: 200 (180 to Attempt) | Duration: 200 Minutes<br/>"
        "<b>Marking Scheme:</b> +4 for Correct Response, -1 for Incorrect, 0 for Unattempted.<br/>"
        "<b>Statutory Section Allocation:</b> Physics: 45 Qs (180 M) • Chemistry: 45 Qs (180 M) • Botany: 45 Qs (180 M) • Zoology: 45 Qs (180 M).<br/>"
        "<b>Official Curriculum Notice:</b> Strictly verified against latest NMC Under Graduate Medical Education Board guidelines including rationalized and added topics."
    )
    meta_table = Table([[Paragraph(meta_text, meta_box_style)]], colWidths=[523])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    neet_items = [x for x in master_data if x.get("exam_name") == "NEET UG"]
    subjects = ["Physics", "Chemistry", "Biology (Botany)", "Biology (Zoology)"]

    for subj in subjects:
        subj_items = [x for x in neet_items if x.get("subject") == subj]
        story.append(Paragraph(f"Subject: {subj} ({len(subj_items)} Official Units/Chapters)", sec_heading))

        table_data = [[
            Paragraph("Chapter / Unit", th_style),
            Paragraph("Class", th_style),
            Paragraph("Official Status", th_style),
            Paragraph("Qs & Marks", th_style),
            Paragraph("Priority Tier", th_style),
            Paragraph("Prescribed Authorized Topics (NMC/NTA)", th_style)
        ]]

        for item in subj_items:
            ch_p = Paragraph(f"<b>{item.get('chapter', '')}</b><br/><font color='#64748b'>{item.get('unit_name', '')}</font>", td_ch)
            cls_p = Paragraph(f"Class {item.get('class_level', '')}", td_cell)
            status_p = Paragraph(item.get("official_status", "Active"), td_cell)
            qs_p = Paragraph(f"<b>{item.get('question_count_avg', '')}</b><br/>{item.get('mark_weightage_range', '')}", td_cell)
            tier_p = Paragraph(item.get("priority_tier", "Guaranteed Core"), td_tier)
            topics_p = Paragraph(item.get("official_topics", ""), td_topics)

            table_data.append([ch_p, cls_p, status_p, qs_p, tier_p, topics_p])

        col_widths = [115, 42, 70, 52, 64, 180]
        t = Table(table_data, colWidths=col_widths, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
            ('ALIGN', (1, 0), (3, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#ffffff'), colors.HexColor('#f8fafc')]),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(t)
        story.append(Spacer(1, 12))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("NEET UG PDF generated:", pdf_path, "Size:", os.path.getsize(pdf_path))

def build_jee_pdf():
    pdf_path = os.path.join(PDF_DIR, "JEE_Main_Official_Curriculum_and_Weightage.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=8
    )
    meta_box_style = ParagraphStyle(
        'MetaBox',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155')
    )
    sec_heading = ParagraphStyle(
        'SecHead',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=10,
        spaceAfter=6
    )
    th_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#ffffff')
    )
    td_ch = ParagraphStyle(
        'TDCh',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#0f172a')
    )
    td_cell = ParagraphStyle(
        'TDCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#1e293b')
    )
    td_tier = ParagraphStyle(
        'TDTier',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#b91c1c')
    )
    td_topics = ParagraphStyle(
        'TDTopics',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#334155')
    )

    story = []
    story.append(Paragraph("JEE (Main) Official Syllabus & Empirical Chapter Weightage", title_style))
    story.append(Paragraph("ISSUED BY NATIONAL TESTING AGENCY (NTA) • APEX BOARD FOR ENGINEERING ADMISSIONS", subtitle_style))

    meta_text = (
        "<b>Examination Standard:</b> Total Marks: 300 | Total Questions: 90 (75 to Attempt) | Duration: 180 Minutes<br/>"
        "<b>Section Architecture:</b> 25 Questions per Subject (20 Section A MCQs + 5 out of 10 Section B Numerical Value Questions).<br/>"
        "<b>Marking Scheme:</b> +4 for Correct, -1 for Incorrect (both MCQs & NVQs), 0 for Unattempted.<br/>"
        "<b>Empirical Weightage Basis:</b> Derived across 186 official computer-based shifts and verified against latest NTA Information Bulletin."
    )
    meta_table = Table([[Paragraph(meta_text, meta_box_style)]], colWidths=[523])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    jee_items = [x for x in master_data if x.get("exam_name") == "JEE Main"]
    subjects = ["Physics", "Chemistry", "Mathematics"]

    for subj in subjects:
        subj_items = [x for x in jee_items if x.get("subject") == subj]
        story.append(Paragraph(f"Subject: {subj} ({len(subj_items)} Official Units/Chapters)", sec_heading))

        table_data = [[
            Paragraph("Chapter / Unit", th_style),
            Paragraph("Class", th_style),
            Paragraph("Official Status", th_style),
            Paragraph("Qs & Marks", th_style),
            Paragraph("Priority Tier", th_style),
            Paragraph("Prescribed Authorized Topics (NTA)", th_style)
        ]]

        for item in subj_items:
            ch_p = Paragraph(f"<b>{item.get('chapter', '')}</b><br/><font color='#64748b'>{item.get('unit_name', '')}</font>", td_ch)
            cls_p = Paragraph(f"Class {item.get('class_level', '')}", td_cell)
            status_p = Paragraph(item.get("official_status", "Active"), td_cell)
            qs_p = Paragraph(f"<b>{item.get('question_count_avg', '')}</b><br/>{item.get('mark_weightage_range', '')}", td_cell)
            tier_p = Paragraph(item.get("priority_tier", "Guaranteed Core"), td_tier)
            topics_p = Paragraph(item.get("official_topics", ""), td_topics)

            table_data.append([ch_p, cls_p, status_p, qs_p, tier_p, topics_p])

        col_widths = [115, 42, 70, 52, 64, 180]
        t = Table(table_data, colWidths=col_widths, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
            ('ALIGN', (1, 0), (3, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#ffffff'), colors.HexColor('#f8fafc')]),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(t)
        story.append(Spacer(1, 12))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("JEE Main PDF generated:", pdf_path, "Size:", os.path.getsize(pdf_path))

if __name__ == "__main__":
    build_neet_pdf()
    build_jee_pdf()
