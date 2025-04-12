# test_throughput.py
import time
import os
from utils import aes_encrypt, rsa_encrypt_key, load_rsa_keys

# Load RSA keys
private_key, public_key = load_rsa_keys()

# Get user input for message size
try:
    size = int(input("Enter message size in bytes (e.g., 1024 for 1 KB): "))
except ValueError:
    print("Invalid input. Using default size 1024 bytes.")
    size = 1024

# Get number of messages
try:
    NUM_MESSAGES = int(input("Enter number of messages to encrypt: "))
except ValueError:
    print("Invalid input. Using default of 100 messages.")
    NUM_MESSAGES = 100

# Generate random message and AES key
message = os.urandom(size)
aes_key = os.urandom(32)  # AES-256

# Start throughput test
start = time.time()
for _ in range(NUM_MESSAGES):
    enc_data = aes_encrypt(message, aes_key)
    rsa_key = rsa_encrypt_key(aes_key, public_key)
end = time.time()

# Calculate results
total_time = end - start
throughput = NUM_MESSAGES / total_time

print("\n=== Throughput Test Report ===")
print(f"Message size       : {size} bytes")
print(f"Number of messages : {NUM_MESSAGES}")
print(f"Total time         : {total_time:.2f} seconds")
print(f"Throughput         : {throughput:.2f} messages/sec")
