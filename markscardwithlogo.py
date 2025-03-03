from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

def generate_marks_card(output_filename, logo_path):
    c = canvas.Canvas(output_filename, pagesize=A4)
    
    # Adding Logo (Top Left Corner)
    c.drawImage(logo_path, 50, 770, width=80, height=80)  # Adjust position & size
    
    # Title
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(300, 800, "Karnataka Secondary Education Examination Board")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(300, 780, "S.S.L.C. Examination - April 2015")
    
    # Student Information
    student_info = [
        ["Name:", "MAHADEV CHIKRAY"],
        ["Father's Name:", "MALLAPPA"],
        ["Mother's Name:", "YALLAVVA"],
        ["Date of Birth:", "05-06-1999"],
        ["Medium of Instruction:", "Kannada"],
        ["Candidate Type:", "CCE Regular Fresh"],
        ["Gender:", "Boy"]
    ]
    
    x, y = 50, 750
    c.setFont("Helvetica", 10)
    for info in student_info:
        c.drawString(x, y, f"{info[0]} {info[1]}")
        y -= 20

    # Marks Table
    data = [
        ["Subject", "Max Marks", "External", "Assessment", "Total", "Grade"],
        ["Kannada", "125", "100", "25", "125", "B+"],
        ["English", "100", "41", "17", "58", "C+"],
        ["Hindi", "100", "80", "20", "100", "B+"],
        ["Mathematics", "100", "24", "18", "42", "C"],
        ["Science", "100", "35", "17", "52", "C+"],
        ["Social Science", "100", "54", "17", "71", "B+"],
        ["Total", "625", "282", "109", "391", "B"]
    ]
    
    table = Table(data, colWidths=[120, 60, 60, 60, 60, 60])
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('GRID', (0, 0), (-1, -1), 1, 'black')
    ]))
    
    table.wrapOn(c, 50, 400)
    table.drawOn(c, 50, 400)
    
    # Final remarks
    c.drawString(50, 350, "Total Marks Obtained (in words): THREE HUNDRED NINETY ONE ONLY (62.56%)")
    
    # Save PDF
    c.save()

# Provide the path to the logo image
generate_marks_card("marks_card.pdf", "C:\Users\LENOVO\Downloads\download.jpg")  # Change "logo.png" to your actual logo file
