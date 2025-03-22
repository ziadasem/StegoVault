class TextCodec:
    def __init__(self):
        pass
    

    def encode_word(self, key_text, word):
        """
        Encodes a word by shifting each letter forward according to the corresponding number or ASCII value.
        
        :param word: The input word to encode.
        :param numbers: A string of numbers/characters determining how much to shift each letter.
        :return: The encoded word.
        """
        shift_values = self._convert_to_shift_values(key_text)
        result = ""

        for i, char in enumerate(word):
            shift = shift_values[i % len(shift_values)]  # Use cyclic shift values
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) if char.islower() else \
                    chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) if char.isupper() else char
            result += new_char

        return result


    def decode_word(self, key_text, encoded_word):
        """
        Decodes a word by shifting each letter backward according to the corresponding number or ASCII value.
        
        :param encoded_word: The scrambled word to decode.
        :param numbers: A string of numbers/characters used during encoding.
        :return: The original word.
        """
        shift_values = self._convert_to_shift_values(key_text)
        result = ""

        for i, char in enumerate(encoded_word):
            shift = shift_values[i % len(shift_values)]  # Use cyclic shift values
            new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a')) if char.islower() else \
                    chr(((ord(char) - ord('A') - shift) % 26) + ord('A')) if char.isupper() else char
            result += new_char

        return result
    
    def _convert_to_shift_values(self, numbers):
        """ Convert a mix of digits and letters into a list of shift values. """
        return [int(c) if c.isdigit() else ord(c) for c in numbers]

