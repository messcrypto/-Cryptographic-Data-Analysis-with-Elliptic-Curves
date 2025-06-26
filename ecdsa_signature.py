.from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature, encode_dss_signature
from cryptography.hazmat.primitives import serialization

# Step 1: Generate Private and Public Keys
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Step 2: Sign a message
message = b"This is a secret message."
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Optional: Print signature components
r, s = decode_dss_signature(signature)
print("Signature (r, s):", r, s)

# Step 3: Verify signature
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("✅ Signature is valid.")
except Exception as e:
    print("❌ Signature is invalid:", e)
