# This will do basic Caesar cipher calculations
# This can be edited to shift different values

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ''.join([chr((ord(char) - shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift - 97) % 26 + 97) if char.islower() else char for char in ciphertext])
    return decrypted_text
