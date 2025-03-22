from image_codec import ImageCodec
from pdf_txt_extractor import PDFTextExtractor


class TextInImageSteganographer:
    def __init__(self):
        self.pdf_txt_extractor = PDFTextExtractor()
        self.image_codec = ImageCodec()
    
    def hide_text_in_image(self, key_text,image_path, pdf_path = None, input_text = None, output_path= None):
        text = ""
        if pdf_path is not None:
            text = self.pdf_txt_extractor.extract_text(pdf_path)
        elif text is not None:
            text = input_text
        else:
            raise ValueError("Either a PDF file or input text must be provided")
            
        
        new_image = self.image_codec.encode_string_to_image(key_text, text, image_path)
        
        if output_path is not None:
            self.image_codec.save_image(new_image, output_path)
            
        return new_image
    
    def extract_text_from_image(self, key_text, image_path, pdf_path=None):
        decoded_text = self.image_codec.decode_string_from_image(key_text, image_path = image_path)
        if pdf_path is not None:
            self.pdf_txt_extractor.save_text_to_pdf(decoded_text, pdf_path)
        return decoded_text
