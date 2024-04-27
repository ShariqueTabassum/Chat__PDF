# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import openai
import PyPDF2

# Set up OpenAI API
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

# Function to interact with OpenAI API
def chat_with_openai(query, context):
    response = openai.Completion.create(
        engine="davinci",
        prompt=context + "\nUser: " + query + "\nAI:",
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit App
def main():
    st.title("PDF Chatbot")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)

        st.write("PDF Contents:")
        st.text(pdf_text)

        context = "The contents of the PDF are as follows:\n" + pdf_text

        user_query = st.text_input("You: ")

        if user_query:
            bot_response = chat_with_openai(user_query, context)
            st.text_area("AI:", value=bot_response, height=200, max_chars=None)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
