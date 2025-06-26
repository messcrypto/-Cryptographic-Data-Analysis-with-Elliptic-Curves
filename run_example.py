.from ecdsa import SigningKey, VerifyingKey
import os

# توليد مفتاح جديد (يمكنك استخدام المفاتيح الموجودة أيضاً)
sk = SigningKey.generate()  # المفتاح الخاص
vk = sk.verifying_key       # المفتاح العام

# حفظ المفاتيح
with open("private_key_temp.pem", "wb") as f:
    f.write(sk.to_pem())

with open("public_key_temp.pem", "wb") as f:
    f.write(vk.to_pem())

# رسالة حساسة
message = b"Confidential: Client's bank data"

# توقيع الرسالة
signature = sk.sign(message)
print("🔐 Signed message.")

# التحقق من التوقيع
is_valid = vk.verify(signature, message)

if is_valid:
    print("✅ Signature verified. The message is authentic.")
else:
    print("❌ Signature invalid. The message may be tampered with.")
