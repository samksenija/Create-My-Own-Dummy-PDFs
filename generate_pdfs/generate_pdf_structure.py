from fpdf import FPDF

def generate_pdf(transaction_data):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Transaction Report", ln=True, align="C")
    pdf.ln(10)

    # Transaction details
    pdf.set_font("Arial", size=12)

    # Account Description
    pdf.cell(200, 10, txt=f"Account Description: {transaction_data['account_description']}", ln=True)

    # Credit
    pdf.cell(200, 10, txt=f"Credit: {transaction_data['credit']:.2f}", ln=True)

    # Debit
    pdf.cell(200, 10, txt=f"Debit: {transaction_data['debit']:.2f}", ln=True)

    # Date
    pdf.cell(200, 10, txt=f"Date: {transaction_data['date']}", ln=True)

    # Reference
    pdf.cell(200, 10, txt=f"Reference: {transaction_data['reference']}", ln=True)

    # Output the PDF, define your own path
    pdf.output(f"C:/Users/User/Desktop/dummy_pdfs/Create-My-Own-Dummy-PDFs/generate_pdfs/pdfs/transaction_{transaction_data['reference']}.pdf")