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

### PDF Processing Tools Comparison

#### PyPDF

Strengths:

- Free and open-source
- Good for basic PDF operations
- Flexible integration with other tools

Limitations:

- No built-in OCR (requires Tesseract)
- Requires multiple additional libraries
- More complex setup and maintenance

Best Used For:

- Basic PDF operations
- Projects where cost is primary concern
- Part of a larger processing pipeline

#### PyMuPDF

Strengths:

- Built-in OCR support via Tesseract
- Native table detection
- Simpler dependency management
- Consistent API for text/table extraction

Limitations:

- Commercial use requires license
- More complex API than PyPDF
- Still requires Tesseract for OCR

Best Used For:

- Projects requiring integrated PDF processing
- Applications needing both text and table extraction
- When minimizing external dependencies is important

#### LLM Whisperer V2

Strengths:

- Minimal code setup (2-3 lines for basic usage)
- Built-in OCR without additional setup
- Maintains document formatting automatically
- No local dependencies to manage

Limitations:

- Requires internet connection
- API key and usage costs
- Processing time depends on service availability
- Requires OpenAI API for advanced processing

Best Used For:

- Rapid implementation needs
- Projects prioritizing accuracy over cost
- When consistent formatting is critical
- Teams wanting to minimize infrastructure management

#### PDFMiner.six

Strengths:

- Precise text positioning
- Multiple encoding support
- Detailed layout analysis
- Pure Python implementation

Limitations:

- Complex low-level API
- No built-in table detection
- No OCR capabilities
- Slower processing

Best Used For:

- Precise text positioning needs
- PDF structure analysis
- Custom PDF tool development
- Multi-language documents

#### PDFPlumber

Strengths:

- User-friendly API
- Strong table extraction
- Visual debugging tools
- Good documentation

Limitations:

- Slower than PyMuPDF
- No OCR support
- Memory intensive
- Limited form field support

Best Used For:

- Table extraction
- Visual debugging needs
- Learning/educational use
- Small to medium PDFs

### Quick Decision Matrix

| Feature          | PyPDF | PyMuPDF | LLM Whisperer | PDFMiner.six | PDFPlumber |
| ---------------- | ----- | ------- | ------------- | ------------ | ---------- |
| Ease of Setup    | ★★☆☆☆ | ★★★☆☆   | ★★★★★         | ★★☆☆☆        | ★★★★☆      |
| OCR Support      | No\*  | Yes     | Yes           | No           | No         |
| Table Detection  | No\*  | Yes     | Yes           | No           | Yes        |
| Cost             | Free  | Paid    | API-based     | Free         | Free       |
| Local Processing | Yes   | Yes     | No            | Yes          | Yes        |

\*With additional libraries
