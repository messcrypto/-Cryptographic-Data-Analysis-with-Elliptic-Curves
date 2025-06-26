from ecdsa import SigningKey, SECP256k1

# توليد المفتاح الخاص
private_key = SigningKey.generate(curve=SECP256k1)
print("Private Key:", private_key.to_string().hex())

# توليد المفتاح العام
public_key = private_key.get_verifying_key()
print("Public Key:", public_key.to_string().hex())

# حفظ المفاتيح في ملفات
with open("private_key.pem", "wb") as f:
    f.write(private_key.to_pem())

with open("public_key.pem", "wb") as f:
    f.write(public_key.to_pem())
