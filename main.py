import streamlit as st
import tempfile

from pdf_merge import merge_pdfs
from pdf_extract import extract_pages

st.set_page_config(
    page_title="PDF Utility Tool",
    layout="centered"
)

st.title("📄 PDF Utility Tool")

option = st.radio(
    "Choose an option",
    ["Merge PDFs", "Take Pages from PDF"]
)

if option == "Merge PDFs":

    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Merge PDFs"):

        if len(uploaded_files) >= 2:

            temp_files = []

            for file in uploaded_files:

                temp = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                )

                temp.write(file.read())
                temp_files.append(temp.name)

            output_file = "merged.pdf"

            merge_pdfs(
                temp_files,
                output_file
            )

            with open(output_file, "rb") as f:

                st.download_button(
                    "Download Merged PDF",
                    f,
                    file_name="merged.pdf"
                )
if option == "Take Pages from PDF":

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    page_range = st.text_input(
        "Page Range (Example: 2-5)"
    )

    if st.button("Extract Pages"):

        if uploaded_file and page_range:

            start, end = map(
                int,
                page_range.split("-")
            )

            temp = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            )

            temp.write(uploaded_file.read())

            output_file = "extracted.pdf"

            extract_pages(
                temp.name,
                start,
                end,
                output_file
            )

            with open(output_file, "rb") as f:

                st.download_button(
                    "Download Extracted PDF",
                    f,
                    file_name="extracted.pdf"
                )
