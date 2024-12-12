import streamlit as st
import os
import csv  # Import csv module
from io import StringIO
from src.helper import llm_pipeline  # Assuming your helper functions are in src.helper


st.title("Interview Question Generator")
st.write("Upload a job description or interview material document (PDF or DOCX) to get interview questions to help you prepare.")

# File upload section
uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

# Process and generate questions/answers if a file is uploaded
if uploaded_file is not None:
    # Save the uploaded file temporarily
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    process_path = file_path

    # Call LLM pipeline to generate Q&A
    with st.spinner("Generating interview questions..."):
        try:
            answer_generation_chain, questions_list = llm_pipeline(process_path)
            
            st.subheader("Generated Interview Questions and Answers")
            output_csv = StringIO()
            writer = csv.writer(output_csv)
            writer.writerow(["Question", "Answer"])  # Write header
            
            # Display and write each Q&A pair
            for question in questions_list:
                answer = answer_generation_chain.run(question)
                st.write(f"**Question:** {question}")
                st.write(f"**Answer:** {answer}")
                st.write("---")  # Separator for readability
                writer.writerow([question, answer])  # Save Q&A to CSV

            # Download button for CSV
            st.download_button(
                label="Download Q&A as CSV",
                data=output_csv.getvalue(),
                file_name="interview_questions.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"An error occurred while generating questions: {e}")

    # Clean up the temporary file
    os.remove(file_path)

else:
    st.info("Please upload a PDF or DOCX file to generate interview questions.")
