import streamlit as st
from pdf_template import generate_pdf
from datetime import date

def download_pdf(data, file_name):
    buffer = generate_pdf(data)
    st.download_button(
        label="Download PDF",
        data=buffer,
        file_name=file_name,
        mime="application/pdf"
    )

def main():
    st.title("Generator")
    
    # Dropdown to select the template
    template = st.selectbox("Select Template", ["VAT Registration", "Service Agreement", "Invoice"])
    
    # Create a form based on the selected template
    with st.form(key='document_form'):
        email = st.text_input("Email")
        client_name = st.text_input("Client Name")
        commercial_registration = st.text_input("Commercial Registration Number")
        service_provider_name = st.text_input("Service Provider Name")
        date_of_agreement = st.date_input("Date of Agreement", value=date.today())
        
        # Additional fields based on the selected template
        if template == "VAT Registration":
            vat_fee = st.text_input("VAT Registration Fee")
            consultancy_fee = st.text_input("Consultancy Fee")
        elif template == "Service Agreement":
            service_details = st.text_area("Service Details")
            terms = st.text_area("Terms & Conditions")
        elif template == "Invoice":
            invoice_number = st.text_input("Invoice Number")
            amount = st.text_input("Amount")
            due_date = st.date_input("Due Date", value=date.today())
        
        # Submit button to generate PDF
        submit_button = st.form_submit_button(label="Generate PDF")
    
    # Process the form data only after submission
    if submit_button:
        data = {
            'email': email,
            'client_name': client_name,
            'commercial_registration': commercial_registration,
            'service_provider_name': service_provider_name,
            'date_of_agreement': str(date_of_agreement)
        }
        
        if template == "VAT Registration":
            data.update({'vat_fee': vat_fee, 'consultancy_fee': consultancy_fee})
            file_name = "vat_registration.pdf"
        elif template == "Service Agreement":
            data.update({'service_details': service_details, 'terms': terms})
            file_name = "service_agreement.pdf"
        elif template == "Invoice":
            data.update({'invoice_number': invoice_number, 'amount': amount, 'due_date': str(due_date)})
            file_name = "invoice.pdf"
        
        download_pdf(data, file_name)

if __name__ == "__main__":
    main()
