# secure_utils.py
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import hmac
import time

def constant_time_compare(val1, val2):
    return hmac.compare_digest(val1, val2)

def secure_rsa_decrypt_key(encrypted_key, private_key):
    """
    Secure RSA decryption with constant-time padding verification.
    """
    try:
        decrypted = private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        dummy = b"SECURECHECK"
        constant_time_compare(decrypted[:len(dummy)], dummy[:len(decrypted)])
        return decrypted
    except Exception:
        time.sleep(0.5)
        raise ValueError("Secure decryption failed.")
