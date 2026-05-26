import os
import fitz # PyMuPDF

base_dir = r"c:\git\Portfolio\ポートフォリオ"

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.pdf'):
            pdf_path = os.path.join(root, file)
            print(f"--- {pdf_path} ---")
            try:
                doc = fitz.open(pdf_path)
                text = ""
                for page in doc[:2]: # Extract up to 2 pages
                    text += page.get_text()
                print(text[:1000]) # First 1000 characters
                print("\n")
            except Exception as e:
                print(f"Error reading {file}: {e}")
