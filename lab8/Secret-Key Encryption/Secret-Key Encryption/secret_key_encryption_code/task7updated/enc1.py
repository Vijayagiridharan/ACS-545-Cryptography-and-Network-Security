from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

def decrypt_aes_ciphertext(ciphertext_hex, key, iv):
    try:
        ciphertext = binascii.unhexlify(ciphertext_hex)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        unpadded_plaintext = unpad(decrypted, AES.block_size, style='pkcs7')
        return unpadded_plaintext.decode('utf-8')
    except Exception as e:
        return None

ciphertext_hex = "3879c71b232cd0d2fc6f5ffcc1d76f074c0fcbe007d9cc53939fdeebf1d6ffd2"
iv_hex = "aabbccddeeff00998877665544332211"

with open('words.txt', 'r') as f:
    english_words = f.read().splitlines()

for word in english_words:
    key = (word.encode() + b"#" * (16 - len(word)))
    decrypted_text = decrypt_aes_ciphertext(ciphertext_hex, key, binascii.unhexlify(iv_hex))
    if decrypted_text:
        print(f"Key found: {word}")
        print(f"Decrypted plaintext: {decrypted_text}")
        break
else:
    print("Key not found in English word list.")







