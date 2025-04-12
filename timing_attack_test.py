import time
import os
import statistics
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# Generate fresh RSA key for testing
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Generate random AES keys (simulate the encrypted session keys)
def rsa_encrypt_key(data, public_key):
    return public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# --- Standard Decryption ---
def standard_rsa_decrypt(ciphertext, private_key):
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# --- Constant-Time Decryption using blinding ---
def constant_time_rsa_decrypt(ciphertext, private_key):
    # Blinding is enabled by default in Python cryptography
    # So this function simulates constant-time behavior
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Test Timing for both
standard_times = []
blinded_times = []

for _ in range(1000):
    data = os.urandom(32)
    encrypted = rsa_encrypt_key(data, public_key)

    # Standard RSA
    start = time.perf_counter()
    standard_rsa_decrypt(encrypted, private_key)
    end = time.perf_counter()
    standard_times.append((end - start) * 1000)  # ms

    # Constant-Time (Blinded)
    start = time.perf_counter()
    constant_time_rsa_decrypt(encrypted, private_key)
    end = time.perf_counter()
    blinded_times.append((end - start) * 1000)  # ms

# Results
print("\n=== Timing Attack Test Report ===")
print("Standard RSA Decryption:")
print(f"  Avg Time: {statistics.mean(standard_times):.2f} ms")
print(f"  Std Dev : {statistics.stdev(standard_times):.2f} ms")

print("Constant-Time RSA Decryption (Blinded):")
print(f"  Avg Time: {statistics.mean(blinded_times):.2f} ms")
print(f"  Std Dev : {statistics.stdev(blinded_times):.2f} ms")
