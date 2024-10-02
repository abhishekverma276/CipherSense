import pandas as pd
import random
from algorithms.digrafid import DigrafidCipher
from algorithms.foursquare import FoursquareCipher

# Load plaintexts from file
def load_plaintexts(file_path):
    with open(file_path, 'r') as file:
        plaintexts = file.read().splitlines()
    return plaintexts

# Function to generate ciphertexts using DIGRAFID and FOURSQUARE
def generate_ciphertexts(plaintexts, digrafid_key, foursquare_key1, foursquare_key2):
    # Initialize cipher objects
    digrafid_cipher = DigrafidCipher(digrafid_key)
    foursquare_cipher = FoursquareCipher(foursquare_key1, foursquare_key2)

    ciphertexts = []

    # Generate DIGRAFID ciphertexts
    for plaintext in plaintexts:
        if len(plaintext) >= 120 and len(plaintext) <= 220:
            ciphertext = digrafid_cipher.encrypt(plaintext)
            ciphertexts.append((ciphertext, 'DIGRAFID'))

    # Generate FOURSQUARE ciphertexts
    for plaintext in plaintexts:
        if len(plaintext) >= 50 and len(plaintext) <= 70:
            ciphertext = foursquare_cipher.encrypt(plaintext)
            ciphertexts.append((ciphertext, 'FOURSQUARE'))

    return ciphertexts

# Save the generated ciphertexts to CSV
def save_to_csv(ciphertexts, output_path):
    df = pd.DataFrame(ciphertexts, columns=['Ciphertext', 'Algorithm'])
    df.to_csv(output_path, index=False)

# Main function to generate and save ciphertext dataset
def main():
    # Load plaintexts (make sure your plaintexts are between 120-220 characters for DIGRAFID, and 50-70 for FOURSQUARE)
    plaintexts = load_plaintexts('../data/plaintexts.txt')

    # Keys for ciphers
    digrafid_key = 'KEYWORD'  # You can choose or randomize the key for Digrafid
    foursquare_key1 = 'EXAMPLEKEY1'  # Key for first square of Foursquare cipher
    foursquare_key2 = 'EXAMPLEKEY2'  # Key for second square of Foursquare cipher

    # Generate ciphertexts
    ciphertexts = generate_ciphertexts(plaintexts, digrafid_key, foursquare_key1, foursquare_key2)

    # Save the generated dataset to CSV
    save_to_csv(ciphertexts, '../data/combined_ciphertexts.csv')

if __name__ == '__main__':
    main()
