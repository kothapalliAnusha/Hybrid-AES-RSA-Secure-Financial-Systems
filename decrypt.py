# decrypt.py
from utils import load_rsa_keys, aes_decrypt
from secure_utils import secure_rsa_decrypt_key
from bank_secure_log import log_event

# Load keys
private_key, _ = load_rsa_keys()

# Load encrypted AES key
with open("encrypted_key.pem", "rb") as f:
    encrypted_key = f.read()

# Secure RSA decryption
try:
    aes_key = secure_rsa_decrypt_key(encrypted_key, private_key)
    log_event("info", "Secure AES key decryption successful.")
except ValueError:
    log_event("error", "Secure RSA decryption failed.")
    raise

# Load encrypted data
with open("encrypted_data.bin", "rb") as f:
    encrypted_data = f.read()

# Decrypt message
decrypted = aes_decrypt(encrypted_data, aes_key)

# Save decrypted output
with open("decrypted_output.txt", "wb") as f:
    f.write(decrypted)

log_event("info", "Decryption successful. Output saved.")
print("✅ Decryption successful! Output saved to: decrypted_output.txt")
