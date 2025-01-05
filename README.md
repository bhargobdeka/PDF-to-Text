# PDF-to-Text Tools Comparison

This repository contains a comparative analysis of different text extraction tools from PDF files: PyMuPDF, PyPDF, and Unstract's LLM Whisperer. The comparison includes various document types to showcase each tool's capabilities in handling different PDF formats.

## 🎯 Purpose

To provide a practical comparison of popular text extraction tools from PDF files by processing:

- Scanned Documents (Invoices)
- Forms (IRS 1098-E)
- Complex Financial Documents (Uber 10-K)

## 📁 Repository Structure

- **pymupdf-notebooks/** - PyMuPDF implementation notebooks
  - `pymupdf_IRS.ipynb` - IRS form extraction
  - `pymupdf_scanned-doc.ipynb` - Scanned document processing
  - `pymupdf_uber10k.ipynb` - Uber 10-K analysis
- **pypdf-notebooks/** - PyPDF implementation notebooks
  - `pypdf_IRS.ipynb` - IRS form extraction
  - `pypdf_scanned-doc.ipynb` - Scanned document processing
  - `pypdf_uber10k.ipynb` - Uber 10-K analysis
- **unstract-notebooks/** - LLM Whisperer implementation notebooks
  - `llm-whisperer_IRS.ipynb` - IRS form extraction
  - `llm-whisperer_scanned-doc.ipynb` - Scanned document processing
  - `llm-whisperer_uber10k.ipynb` - Uber 10-K analysis
- **raw-docs/** - Original PDF files for testing
- **saved-docs/** - Extracted data in JSON format
- `requirements.txt` - Project dependencies
- `example.env` - save the environment variables in this file
- `README.md` - Project documentation

## PDF Processing Tools Comparison

| Feature          | PyPDF | PyMuPDF | LLM Whisperer | PDFMiner.six | PDFPlumber |
| ---------------- | ----- | ------- | ------------- | ------------ | ---------- |
| Ease of Setup    | ★★☆☆☆ | ★★★☆☆   | ★★★★★         | ★★☆☆☆        | ★★★★☆      |
| OCR Support      | No\*  | Yes     | Yes           | No           | No         |
| Table Detection  | No\*  | Yes     | Yes           | No           | Yes        |
| Cost             | Free  | Paid    | API-based     | Free         | Free       |
| Local Processing | Yes   | Yes     | No            | Yes          | Yes        |

\*With additional libraries
