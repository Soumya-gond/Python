from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C+"
    elif marks >= 40:
        return "C"
    else:
        return "F"

# Function to generate marks card
def generate_marks_card(name,fname,mname,dob,medium,gender, marks_data, output_filename):
    c = canvas.Canvas(output_filename, pagesize=A4)
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 800, "Karnataka Secondary Education Examination Board")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(300, 780, "S.S.L.C. Examination - 2025")

    # Student Information
    c.setFont("Helvetica", 12)
    c.drawString(50, 740,f"Student Name: {name}")
    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Father Name: {fname}")
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"Mother Name: {mname}")
    c.setFont("Helvetica", 12)
    c.drawString(50, 680, f"Date Of Birth: {dob}")
    c.setFont("Helvetica", 12)
    c.drawString(50, 660, f"Medium Of Instruction: {medium}")
    c.setFont("Helvetica", 12)
    c.drawString(50, 640, f"Gender: {gender}") 

   # subjects = ["Kannada", "English", "Hindi", "Mathematics", "Science", "Social Science"]
    total_obtained_marks = 0
    total_max_marks=0
    data = [["Subject","Max Marks","External","Assesment", "Marks Obtained", "Grade"]]

    for subject, mark in marks_data.items():
        max_marks, external, assessment = marks_data[subject]
        total_marks = external + assessment 
        grade = calculate_grade(total_marks)
        total_obtained_marks += total_marks
        total_max_marks+= max_marks
        data.append([subject, max_marks, external, assessment, total_marks, grade])

    percentage = round((total_obtained_marks / total_max_marks) * 100, 2)
    final_grade = calculate_grade(percentage)

    # Table for Marks
    table = Table(data, colWidths=[120, 80,80,80,100,80])
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('GRID', (0, 0), (-1, -1), 1, 'black'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically center text
        ('LEADING', (0, 0), (-1, -1), 20),  # Increase line spacing inside cells
        ('ROWHEIGHT', (0, 0), (-1, -1), 30)
    ]))

    table.wrapOn(c, 50, 400)
    table.drawOn(c, 50, 400)

    # Final percentage
    c.drawString(50, 350,f"Total Marks: {total_obtained_marks} / {total_max_marks}")
    c.drawString(50, 330,f"Percentage: {percentage}%")
    c.drawString(50, 310,f"Final Grade: {final_grade}")

    # Save PDF
    c.save()
    print(f"Marks card generated: {output_filename}")

# Taking input from user
name = input("Enter Student Name: ")
fname = input("Enter Father's Name: ")
mname = input("Enter Mother's Name: ")
dob = input("Date of birth: ")
medium = input("Medium of Instruction: ")
gender = input("Gender: ")


subjects = ["Kannada", "English", "Hindi", "Mathematics", "Science", "Social Science"]
marks_data = {}
for subject in subjects:
    max_marks = 100  # Assuming all subjects have max marks of 100
    external = int(input(f"Enter External Marks for {subject} (out of 80): "))
    assessment = int(input(f"Enter Assessment Marks for {subject} (out of 20): "))  # Assuming assessment is out of 20

    
    if external > 80 or assessment > 20:
        print("Error: Marks exceed allowed maximum! Please enter again.")
        exit()
    marks_data[subject] = (max_marks, external, assessment)
# Generate the marks card
generate_marks_card(name,fname,mname,dob,medium,gender, marks_data, f"{name}_marks_card.pdf")
