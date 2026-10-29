
import streamlit as st
from backend import read_resume

st.set_page_config(
    page_title="AI Based Resume Analyser",
    page_icon="📄",
    layout="wide"
)

# Keep uploaded file and extracted text across Streamlit reruns
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "resume_filename" not in st.session_state:
    st.session_state.resume_filename = ""

st.markdown("""
<style>
.main {
    background-color: #f7f8fc;
}
.block-container {
    padding-top: 2rem;
    max-width: 1000px;
}
h1 {
    color: #4936a8;
}
</style>
""", unsafe_allow_html=True)

st.title("📄 AI Based Resume Analyser")
st.write(
    "Upload your resume and read its contents. "
    "More analysis features can be added later."
)

st.divider()

st.subheader("📤 Upload Your Resume")

# OPTION 1: Upload resume
uploaded_file = st.file_uploader(
    "Upload Resume — select a PDF or DOCX file",
    type=["pdf", "docx"],
    key="resume_upload"
)

if uploaded_file is not None:
    st.success("File selected: " + uploaded_file.name)
    st.caption(
        "File size: "
        + str(round(uploaded_file.size / 1024, 2))
        + " KB"
    )

st.divider()
st.subheader("Resume Tools")

# OPTION 2: Read resume file
if st.button("📖 Read Resume File", use_container_width=True):
    if uploaded_file is None:
        st.warning("Please select a resume file first.")
    else:
        try:
            with st.spinner("Reading your resume..."):
                extracted_text = read_resume(uploaded_file)

            st.session_state.resume_text = extracted_text
            st.session_state.resume_filename = uploaded_file.name

            st.success("Resume read successfully!")

        except Exception as error:
            st.error(str(error))

# OPTIONS 3–7: Intentionally inactive
st.button(
    "📊 Resume Score",
    disabled=True,
    use_container_width=True
)

st.button(
    "🎯 Find Matching Jobs",
    disabled=True,
    use_container_width=True
)

st.button(
    "🧠 Skill Analysis",
    disabled=True,
    use_container_width=True
)

st.button(
    "📑 View Full Analysis Report",
    disabled=True,
    use_container_width=True
)

st.button(
    "🔄 Clear/Reset",
    disabled=True,
    use_container_width=True
)

st.divider()
st.header("📋 Resume Output")

if st.session_state.resume_text:
    st.subheader("Extracted Resume Text")
    st.write("File: " + st.session_state.resume_filename)

    st.text_area(
        "Resume contents",
        value=st.session_state.resume_text,
        height=350,
        disabled=True
    )

    st.download_button(
        "Download Extracted Text",
        data=st.session_state.resume_text,
        file_name="extracted_resume.txt",
        mime="text/plain"
    )

else:
    st.info(
        "Your extracted resume text will appear here "
        "after you click Read Resume File."
    )

st.divider()
st.caption("AI Based Resume Analyser | Built with Python and Streamlit")
