from Crypto.Cipher import AES
from Crypto.Util import Padding

def encrypt_and_decrypt():
    key_hex_string = '00112233445566778899AABBCCDDEEFF'
    iv_hex_string = 'aabbccddeeff00998877665544332211'
    key = bytes.fromhex(key_hex_string)
    iv = bytes.fromhex(iv_hex_string)
    data = b'This is a top secret.'

    # Encrypt the entire data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(Padding.pad(data, AES.block_size))

    print("Ciphertext: {0}".format(ciphertext.hex()))

    # Decrypt the ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    unpadded_plaintext = Padding.unpad(plaintext, AES.block_size)

    print("Plaintext: {0}".format(unpadded_plaintext.decode()))

if __name__ == "__main__":
    encrypt_and_decrypt()

