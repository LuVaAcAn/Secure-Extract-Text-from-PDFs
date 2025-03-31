# Secure-Extract-Text-from-PDFs
## 🛡️ PDFshield - Secure & Extract Text from PDFs

PDFshield is a Python tool that extracts text from scanned PDFs using **OCR (Tesseract)** and allows saving it in multiple formats (`.txt`, `.pdf`, `.docx`, `.html`). Additionally, it creates a **password-protected** version of the original PDF.  

## 🚀 Features  
- 🔍 **Extract text** from scanned PDFs using OCR (Tesseract).  
- 📄 Save extracted text as **TXT, PDF, DOCX, or HTML**.  
- 🔐 Generate a **password-protected PDF** version.  
- ⚡ User-friendly **CLI to select output formats**.  

## 🛠️ Technologies Used  
- `PyPDF2` - PDF handling (reading, writing, encrypting).  
- `pdf2image` - Convert PDFs to images.  
- `pytesseract` - OCR for text extraction.  
- `reportlab` - Create PDFs from text.  
- `python-docx` - Generate DOCX files.  

## 📦 Installation  
```bash```
- git clone https://github.com/yourusername/PDFshield.git
- cd PDFshield
- pip install -r requirements.txt.

## ▶️ Usage
- 1️⃣ Place your PDF in the project folder.
- 2️⃣ Run the script: python pdfshield.py
