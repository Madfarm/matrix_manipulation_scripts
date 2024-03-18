import rsa

def generate_keys():
    (public_key, private_key) = rsa.newkeys(512)
    return public_key, private_key

def encrypt_message(message, public_key):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    return decrypted_message

public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "Hello, World!"
encrypted_message = encrypt_message(message, public_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)