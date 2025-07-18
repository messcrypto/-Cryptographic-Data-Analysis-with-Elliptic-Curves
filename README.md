9
.# Cryptographic Data Analysis using Elliptic Curves

This project demonstrates basic cryptographic operations using **Elliptic Curve Cryptography (ECC)** with Python. It simulates secure data handling and key generation techniques over the `secp256k1` curve.

## 🔒 What It Does
- Generates a private and public key pair using ECC
- Applies scalar multiplication over elliptic curve points
- Hashes text messages using SHA-256
- Demonstrates secure data encryption foundation

## 🧠 Why This Project?
This project reflects my academic background in mathematics and cryptography, and my passion for applying mathematical theory to real-world secure applications.

## 🛠️ Technologies Used
- Python
- Elliptic Curve Cryptography
- SHA-256 (Hashing)

## 👩‍💻 Author
**Hadjer Meskem**  
Mathematics graduate | Cryptography enthusiast | Building a career in data security & remote technologies.
# Cryptographic Data Analysis using Python 🔐📊

This project demonstrates how to combine basic data analysis with modern encryption techniques using Python.

## 🔧 Technologies Used
- Python
- Pandas
- ECC (Elliptic Curve Cryptography)
- SHA-256 Hashing
- tinyec library

## 🧠 Project Goals
- Generate sample user data.
- Encrypt data using SHA-256 hashing.
- Generate private/public key pairs using elliptic curve cryptography (ECC).
- Store and display results using pandas DataFrame.

## 📂 Project Structure
- `data_analysis_encryption.py` → main script with full logic
- `README.md` → project documentation

## 💡 Why this project?
This mini-project is designed to:
- Demonstrate applied cryptography.
- Bridge your math background (elliptic curves) with practical data processing.
- Build a clean portfolio project for GitHub and job applications.

## 🚀 How to Run
Install dependencies:
```bash
pip install pandas tinyec
.# 🔐 Cryptographic Data Analysis using ECC in Python

## Overview
This project demonstrates practical cryptographic operations using **Elliptic Curve Cryptography (ECC)** in Python, including:
- Key generation using ECC (SECP256R1)
- Digital signatures using ECDSA
- Secure storage of keys

## Files
- `ecc_key_generator.py`: Generates private and public keys using ECC and saves them in PEM format.
- `ecdsa_signature.py`: Signs a message using the private key and verifies it with the public key.

## Requirements
- Python 3.x
- `cryptography` library: Install via `pip install cryptography`

## Run the Scripts
```bash
python ecc_key_generator.py
python ecdsa_signature.py
