from ecdsa import SigningKey, VerifyingKey, SECP256k1
import hashlib

# تحميل المفتاح الخاص
with open("private_key.pem", "rb") as f:
    private_key = SigningKey.from_pem(f.read())

# تحميل المفتاح العام
with open("public_key.pem", "rb") as f:
    public_key = VerifyingKey.from_pem(f.read())

# الرسالة الأصلية
message = b"Hello, this is a secure message!"

# التوقيع باستخدام المفتاح الخاص (يُشبه التشفير)
signature = private_key.sign(message)
print("Signature (توقيع الرسالة):", signature.hex())

# التحقق من الرسالة باستخدام المفتاح العام (يُشبه فك التشفير)
is_valid = public_key.verify(signature, message)
print("هل التوقيع صحيح؟", is_valid)
