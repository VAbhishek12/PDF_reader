import streamlit as st
import base64

st.title("📄 PDF Preview & Download")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Preview the PDF
    base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
    pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}"
        width="100%" height="800" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Reset file pointer for download
    uploaded_file.seek(0)

    # Download button
    st.download_button(
        label="📥 Download PDF",
        data=uploaded_file,
        file_name=uploaded_file.name,
        mime="application/pdf"
    )
