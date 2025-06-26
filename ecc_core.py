..from cryptography.fernet import Fernet

# Generate key (do this only once)
# key = Fernet.generate_key()
# with open('secret.key', 'wb') as f:
#     f.write(key)

# Load key
with open('secret.key', 'rb') as f:
    key = f.read()

cipher = Fernet(key)

# Encrypt data
data = b"Hello Hadjer, this is a secure message!"
encrypted = cipher.encrypt(data)
print("Encrypted:", encrypted)

# Decrypt
decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted)
