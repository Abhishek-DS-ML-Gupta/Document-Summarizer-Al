# LegalDocSummerizer
LegalDocSummerizer is a Streamlit application that allows users to upload legal documents in PDF format and receive concise summaries. The app leverages OpenAI's language models to generate summaries, making it easier to understand complex legal texts.

## Features
- Upload PDF legal documents
- Extract and split text into manageable chunks
- Generate summaries using OpenAI's language models
- Store and retrieve document embeddings for efficient processing

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Abhishek-DS-ML-Gupta/Document-Summarizer-Al.git
   cd LegalDocSummerizer
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   - Obtain an API key from [OpenAI](https://platform.openai.com/account/api-keys).
   - Set the API key as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_api_key_here
     ```
   - Alternatively, create a `.env` file in the project root and add:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Upload a legal document in PDF format.
3. Click the "Summarize" button to generate a summary of the document.
