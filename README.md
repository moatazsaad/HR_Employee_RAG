# HR Employee RAG

A Retrieval-Augmented Generation (RAG) system for HR employee insights using OpenAI, LangChain, and Chroma.

## Overview

This project converts HR employee data from a CSV file into individual Markdown files, creates embeddings with OpenAI, and stores them in a Chroma vector database. Users can interact with the data via a conversational interface (Gradio) to get summaries or insights about employees.

## Features

- Converts CSV employee data into structured Markdown documents.
- Splits documents into chunks for optimal RAG performance.
- Generates embeddings with OpenAI and stores them in a Chroma vector store.
- Provides a conversational interface to query employee data.
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
* Example query: `"Give me a summary of employee 1"`

## File Structure

```
HR_Employee_RAG/
├─ hr_employee_rag.py       # Main script for RAG pipeline and Gradio interface
├─ hr_data/
│  └─ employees/           # Markdown files for each employee
├─ requirements.txt        # Project dependencies
└─ README.md
```
