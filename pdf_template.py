from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(data):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    c.drawString(100, 750, "Generated Document")
    c.drawString(100, 730, "This document is generated based on user inputs.")

    # Common fields for all templates
    c.drawString(100, 710, f"Client Name: {data.get('client_name', 'N/A')}")
    c.drawString(100, 690, f"Email: {data.get('email', 'N/A')}")
    c.drawString(100, 670, f"Commercial Registration Number: {data.get('commercial_registration', 'N/A')}")
    c.drawString(100, 650, f"Service Provider Name: {data.get('service_provider_name', 'N/A')}")
    c.drawString(100, 630, f"Date of Agreement: {data.get('date_of_agreement', 'N/A')}")

    # Template-specific fields
    if 'vat_fee' in data or 'consultancy_fee' in data:
        c.drawString(100, 610, "VAT Registration Details:")
        c.drawString(120, 590, f"VAT Registration Fee: {data.get('vat_fee', 'N/A')}")
        c.drawString(120, 570, f"Consultancy Fee: {data.get('consultancy_fee', 'N/A')}")
    
    if 'service_details' in data or 'terms' in data:
        c.drawString(100, 610, "Service Agreement Details:")
        c.drawString(120, 590, f"Service Details: {data.get('service_details', 'N/A')}")
        c.drawString(120, 570, f"Terms & Conditions: {data.get('terms', 'N/A')}")

    if 'invoice_number' in data or 'amount' in data:
        c.drawString(100, 610, "Invoice Details:")
        c.drawString(120, 590, f"Invoice Number: {data.get('invoice_number', 'N/A')}")
        c.drawString(120, 570, f"Amount: {data.get('amount', 'N/A')}")
        c.drawString(120, 550, f"Due Date: {data.get('due_date', 'N/A')}")

    c.save()
    buffer.seek(0)
    return buffer
