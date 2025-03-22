import imageio
import numpy as np

from text_codec import TextCodec


class ImageCodec():
    def __init__(self):
        self.text_codec = TextCodec()
    
    def encode_string_to_image(self, key_text,  text, image_path):
        image = imageio.imread(image_path)
        text = self.text_codec.encode_word(key_text, text)
        
        # Append an end-of-text marker (e.g., '\0\0\0\0') to indicate the end of the hidden message
        text += '\0\0\0\0'
        bit_length = (len(text) + 1) * 8  # Total bits needed
        # Convert the image into a NumPy array (if not already)
        new_image = np.array(image, dtype=np.uint8)

        # Flatten the image for easy manipulation
        flat_image = new_image.ravel()
        
        if bit_length > len(flat_image):
            raise ValueError("Image is too small to hold the text.")

        pixel_index = 0  # Track which pixel we're modifying

        # Outer loop: Iterate over each character in the text
        for char in text:
            char_binary = format(ord(char), '08b')  # Convert character to 8-bit binary string

            # Inner loop: Iterate over each bit in the character
            for bit in char_binary:
                flat_image[pixel_index] = (flat_image[pixel_index] & 0xFE) | int(bit)  # Modify LSB
                pixel_index += 1  # Move to the next pixel

        # Reshape back to original image dimensions
        new_image = flat_image.reshape(image.shape)

        return new_image
    
    def decode_string_from_image(self,key_text, input_image = None, image_path = None):
        if image_path is not None:
            image = imageio.imread(image_path)
        elif input_image is not None:
            image = input_image
        else:
            raise ValueError("Either an image path or an image array is required.")
        
        # Convert image to NumPy array if it's not already
        new_image = np.array(image, dtype=np.uint8)

        # Flatten the image for easy manipulation
        flat_image = new_image.ravel()

        binary_string = ""  # Store extracted binary bits
        decoded_text = ""  # Store decoded characters

        # Extract LSBs from the image
        for pixel in flat_image:
            binary_string += str(pixel & 1)  # Get the least significant bit (LSB)

            # Process each 8 bits (1 byte)
            if len(binary_string) == 8:
                char = chr(int(binary_string, 2))  # Convert binary to character
                decoded_text += char
                binary_string = ""  # Reset for the next character

                # Stop decoding when the end marker is found
                if decoded_text.endswith("\0\0\0\0"):
                    decoded_text= decoded_text[:-4]
                    decoded_text = self.text_codec.decode_word(key_text, decoded_text)
                    return decoded_text  # Remove the end marker and return the message
        
        return decoded_text  # Return whatever was decoded (failsafe)
    
    
    def save_image(self, image_array, output_path):
        imageio.imwrite(output_path, image_array.astype(np.uint8))
        print(f"Encoded image saved as {output_path}")


