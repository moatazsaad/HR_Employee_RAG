# HR Employee RAG

A Retrieval-Augmented Generation (RAG) system for HR employee insights using OpenAI, LangChain, and Chroma.

## Overview

This project converts HR employee data from a CSV file into individual Markdown files, creates embeddings with OpenAI, and stores them in a Chroma vector database. Users can interact with the data via a conversational interface (Gradio) to get summaries or insights about employees. It also supports **evaluation mode**, where answers are returned along with source documents for verification.

## Features

- Converts CSV employee data into structured Markdown documents.
- Splits documents into chunks for optimal RAG performance.
- Generates embeddings with OpenAI and stores them in a Chroma vector store.
- Provides a conversational interface to query employee data.
- **Evaluation mode**: Returns answers with supporting sources for transparency.
- Local Gradio interface with shareable link for easy access.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/moatazsaad/HR_Employee_RAG.git
cd HR_Employee_RAG
````

2. Create a Python environment and install dependencies:

```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

pip install -r requirements.txt
```

3. Set your OpenAI API key in a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the main script:

```bash
python hr_employee_rag.py
```

* A Gradio chat interface will launch locally and provide a shareable link.
* Example queries:

  * `"Give me a summary of employee 1"` (normal chat mode)
  * `"Give me a summary of employee 1"` in **evaluation mode** to get sources alongside the answer.

## File Structure

```
HR_Employee_RAG/
├─ hr_employee_rag.py       # Main script for RAG pipeline, Gradio interface, and evaluation mode
├─ hr_data/
│  └─ employees/           # Markdown files for each employee
├─ requirements.txt        # Project dependencies
└─ README.md


If you want, I can also **add a small usage snippet for `curl` or Python POST requests** for evaluation mode, so users can test it outside Gradio. Do you want me to do that?
```
