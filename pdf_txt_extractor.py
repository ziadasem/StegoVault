import fitz  

class PDFTextExtractor:
    def __init__(self):
        pass

    def extract_text(self, pdf_path):
        """Extract text from the entire PDF and return it as a string."""
        text = ""
        try:
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    text += page.get_text("text") + "\n"
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None
        return text.strip()

    def save_text_to_file(self, output_txt):
        """Save extracted text to a .txt file."""
        text = self.extract_text()
        if text:
            with open(output_txt, "w", encoding="utf-8") as file:
                file.write(text)
            print(f"Text saved to {output_txt}")
        else:
            print("No text extracted.")

    def print_extracted_text(self):
        """Print the extracted text to the console."""
        text = self.extract_text()
        if text:
            print("Extracted Text:\n", text)
        else:
            print("No text extracted.")

    def save_text_as_pdf(self, text,  output_pdf):
        """Save the extracted text into a new PDF file."""
        if not text:
            print("No text extracted to save as PDF.")
            return

        try:
            doc = fitz.open()  # Create a new empty PDF
            page = doc.new_page()  # Add a new blank page
            page.insert_text((50, 50), text)  # Insert extracted text at position (50, 50)
            doc.save(output_pdf)  # Save to file
            doc.close()
            print(f"Extracted text saved as PDF: {output_pdf}")
        except Exception as e:
            print(f"Error saving text as PDF: {e}")

