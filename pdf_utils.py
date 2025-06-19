import fitz  # PyMuPDF

def clean_text(text):
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return ' '.join(lines)

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return clean_text(text)

def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
