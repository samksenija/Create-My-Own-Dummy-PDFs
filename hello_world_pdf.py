from fpdf import FPDF

# Create a PDF object with default parameters (Portrait, mm, A4)
pdf = FPDF()

# Add a page
pdf.add_page()

# Set the font: Arial, Bold, size 12
pdf.set_font("Arial", size=12)

# Add a cell (a block of text)
# Arguments: width, height, text, border (0=no border), line positioning (1=next line), alignment ('C'=center)
pdf.cell(0, 10, txt="Hello World!", ln=True, align="C")

# Output the PDF to a file named 'hello_world.pdf'
pdf.output("hello_world.pdf")
