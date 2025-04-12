# encrypt.py
from utils import load_rsa_keys, aes_encrypt, rsa_encrypt_key
from bank_secure_log import log_event
import os

# Generate RSA keys (only once)
if not os.path.exists("rsa_keys/private_key.pem"):
    from utils import generate_rsa_keys
    generate_rsa_keys()
    log_event("info", "RSA key pair generated.")

# Load public key
_, public_key = load_rsa_keys()

# Generate AES key
aes_key = os.urandom(32)

# Read plaintext input
with open("input.txt", "rb") as f:
    message = f.read()

# Encrypt using AES + RSA
aes_encrypted = aes_encrypt(message, aes_key)
rsa_encrypted_key = rsa_encrypt_key(aes_key, public_key)

# Save outputs
with open("encrypted_data.bin", "wb") as f:
    f.write(aes_encrypted)

with open("encrypted_key.pem", "wb") as f:
    f.write(rsa_encrypted_key)

log_event("info", "Encryption complete.")
print("✅ Encryption complete! Files saved:")
print("• encrypted_data.bin")
print("• encrypted_key.pem")
