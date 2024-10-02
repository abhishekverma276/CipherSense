import string

class FoursquareCipher:
    def __init__(self, key1, key2):
        self.alphabet = string.ascii_uppercase.replace('J', '')
        self.grid1 = self.__generate_matrix(self.alphabet)
        self.grid2 = self.__generate_matrix(key1)
        self.grid3 = self.__generate_matrix(key2)
        self.grid4 = self.__generate_matrix(self.alphabet)
    
    def __generate_matrix(self, key):
        # Create a 5x5 matrix for the cipher grid
        unique_key = ''.join(sorted(set(key), key=key.index))
        remaining_chars = [ch for ch in self.alphabet if ch not in unique_key]
        combined = unique_key + ''.join(remaining_chars)
        matrix = [list(combined[i:i+5]) for i in range(0, len(combined), 5)]
        return matrix

    def __find_position(self, char, grid):
        # Find the row and column of a character in a given cipher grid
        for i, row in enumerate(grid):
            if char in row:
                return i, row.index(char)
        return None

    def encrypt(self, plaintext):
        # Encrypt using Foursquare cipher logic
        plaintext = plaintext.upper().replace('J', 'I')
        ciphertext = ''
        for i in range(0, len(plaintext), 2):
            if i + 1 < len(plaintext):
                char1, char2 = plaintext[i], plaintext[i + 1]
                row1, col1 = self.__find_position(char1, self.grid1)
                row2, col2 = self.__find_position(char2, self.grid4)

                # Swap positions and form the new ciphertext pair
                ciphertext += self.grid2[row1][col2] + self.grid3[row2][col1]
            else:
                ciphertext += plaintext[i]  # For odd-length plaintext, leave last char as is
        return ciphertext

    def decrypt(self, ciphertext):
        # Decrypt Foursquare cipher
        plaintext = ''
        for i in range(0, len(ciphertext), 2):
            char1, char2 = ciphertext[i], ciphertext[i + 1]
            row1, col1 = self.__find_position(char1, self.grid2)
            row2, col2 = self.__find_position(char2, self.grid3)

            # Swap back positions
            plaintext += self.grid1[row1][col2] + self.grid4[row2][col1]
        return plaintext
