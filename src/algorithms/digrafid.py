import string

class DigrafidCipher:
    def __init__(self, key):
        self.alphabet = string.ascii_uppercase.replace('J', '')
        self.key = self.__generate_matrix(key)
    
    def __generate_matrix(self, key):
        # Remove duplicates from key and create matrix for cipher
        unique_key = ''.join(sorted(set(key), key=key.index))
        remaining_chars = [ch for ch in self.alphabet if ch not in unique_key]
        combined = unique_key + ''.join(remaining_chars)
        matrix = [list(combined[i:i+5]) for i in range(0, len(combined), 5)]
        return matrix
    
    def __find_position(self, char):
        # Find the row and column of a character in the cipher matrix
        for i, row in enumerate(self.key):
            if char in row:
                return i, row.index(char)
        return None
    
    def __process_pair(self, char1, char2, encrypt=True):
        # Encrypt or decrypt a pair of letters based on the cipher matrix
        row1, col1 = self.__find_position(char1)
        row2, col2 = self.__find_position(char2)
        
        if row1 == row2:
            # Same row: shift columns
            col1 = (col1 + 1) % 5 if encrypt else (col1 - 1) % 5
            col2 = (col2 + 1) % 5 if encrypt else (col2 - 1) % 5
        elif col1 == col2:
            # Same column: shift rows
            row1 = (row1 + 1) % 5 if encrypt else (row1 - 1) % 5
            row2 = (row2 + 1) % 5 if encrypt else (row2 - 1) % 5
        else:
            # Rectangle: swap columns
            col1, col2 = col2, col1
        
        return self.key[row1][col1] + self.key[row2][col2]
    
    def preprocess_text(self, text):
        # Preprocess the input by formatting into pairs and replacing 'J' with 'I'
        text = text.upper().replace('J', 'I')
        formatted_text = ''
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] != text[i + 1]:
                formatted_text += text[i] + text[i + 1]
                i += 2
            else:
                formatted_text += text[i] + 'X'
                i += 1
        if len(formatted_text) % 2 != 0:
            formatted_text += 'X'
        return formatted_text

    def encrypt(self, plaintext):
        # Encrypt text
        plaintext = self.preprocess_text(plaintext)
        ciphertext = ''
        for i in range(0, len(plaintext), 2):
            ciphertext += self.__process_pair(plaintext[i], plaintext[i+1])
        return ciphertext
    
    def decrypt(self, ciphertext):
        # Decrypt text
        plaintext = ''
        for i in range(0, len(ciphertext), 2):
            plaintext += self.__process_pair(ciphertext[i], ciphertext[i+1], encrypt=False)
        return plaintext
