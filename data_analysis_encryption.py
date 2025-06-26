.import hashlib
import secrets
from tinyec import registry
import pandas as pd

# 1. توليد أسماء وهمية
users = ['Alice', 'Bob', 'Charlie', 'David']
data = ['Secret1', 'Secret2', 'Secret3', 'Secret4']

# 2. تشفير البيانات باستخدام SHA-256
hashed_data = [hashlib.sha256(info.encode()).hexdigest() for info in data]

# 3. توليد مفتاح خاص/عام باستخدام ECC
curve = registry.get_curve('brainpoolP256r1')

def generate_keys():
    private_key = secrets.randbelow(curve.field.n)
    public_key = private_key * curve.g
    return private_key, public_key

keys = [generate_keys() for _ in users]
private_keys = [k[0] for k in keys]
public_keys = [f'({k[1].x},{k[1].y})' for k in keys]

# 4. تخزين النتائج في DataFrame
df = pd.DataFrame({
    'User': users,
    'Raw Data': data,
    'Hashed (SHA-256)': hashed_data,
    'Private Key': private_keys,
    'Public Key': public_keys
})

# 5. عرض النتائج
print(df)
