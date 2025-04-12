# evaluate_performance.py
import os
from time import perf_counter as timer  # High-resolution timer
from utils import aes_encrypt, aes_decrypt, rsa_encrypt_key, load_rsa_keys
from secure_utils import secure_rsa_decrypt_key

private_key, public_key = load_rsa_keys()

# Message sizes to test (in bytes)
sizes = [512, 1024, 5120, 10240]  # 512 B, 1 KB, 5 KB, 10 KB

results = []

for size in sizes:
    message = os.urandom(size)
    aes_key = os.urandom(32)

    # Measure AES encryption
    t1 = timer()
    encrypted_data = aes_encrypt(message, aes_key)
    t2 = timer()
    aes_enc_time = (t2 - t1) * 1000  # in ms

    # Measure RSA encryption (key wrapping)
    t3 = timer()
    rsa_encrypted_key = rsa_encrypt_key(aes_key, public_key)
    t4 = timer()
    rsa_enc_time = (t4 - t3) * 1000

    # Measure Hybrid decryption (RSA + AES)
    t5 = timer()
    decrypted_key = secure_rsa_decrypt_key(rsa_encrypted_key, private_key)
    decrypted_data = aes_decrypt(encrypted_data, decrypted_key)
    t6 = timer()
    hybrid_dec_time = (t6 - t5) * 1000

    results.append((size, aes_enc_time, rsa_enc_time, hybrid_dec_time))

# Print results in a formatted table
print(f"{'Message Size (bytes)':<20}{'AES Time (ms)':<18}{'RSA Time (ms)':<18}{'Hybrid Decrypt (ms)':<20}")
for r in results:
    print(f"{r[0]:<20}{r[1]:<18.4f}{r[2]:<18.4f}{r[3]:<20.4f}")
