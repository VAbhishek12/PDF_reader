import streamlit as st
import base64

st.title("📄 PDF Upload, Preview & Download")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")

    pdf_display = f"""
        <embed src="data:application/pdf;base64,{base64_pdf}"
        width="100%" height="600" type="application/pdf">
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

    uploaded_file.seek(0)
    st.download_button("📥 Download PDF", uploaded_file, file_name=uploaded_file.name, mime="application/pdf")
