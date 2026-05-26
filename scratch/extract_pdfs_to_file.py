import os
import fitz # PyMuPDF

base_dir = r"c:\git\Portfolio\ポートフォリオ"
output_file = r"c:\git\Portfolio\scratch\pdf_texts.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                out.write(f"\n\n--- {pdf_path} ---\n")
                try:
                    doc = fitz.open(pdf_path)
                    text = ""
                    for page in doc[:2]:
                        text += page.get_text()
                    out.write(text[:2000])
                except Exception as e:
                    out.write(f"Error reading {file}: {e}")
