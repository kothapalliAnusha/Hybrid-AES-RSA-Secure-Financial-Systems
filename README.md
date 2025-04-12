
# 🔐 Hybrid AES-RSA Framework with Constant-Time Decryption

## 🧩 Project Overview

This project implements a **secure hybrid encryption framework** designed for **financial systems** and **online banking platforms**, ensuring both **high performance** and **robust protection** against **timing** and **side-channel attacks**.

- 🔐 **AES-256-GCM** for fast, authenticated encryption.
- 🔑 **RSA-2048 with OAEP** for secure AES key exchange.
- 🕒 **Constant-Time RSA Decryption** to prevent timing-based attacks.

---

## ⚙️ Technologies Used

- **Programming Language**: Python
- **Encryption Algorithms**: AES-256-GCM, RSA-2048 (OAEP)
- **Security Enhancements**: Blinding, Fixed-Window Exponentiation, Bit-Masking
- **Logging**: Python logging module
- **Performance & Timing Analysis**: Custom scripts

---

## 📁 Project Structure

```
├── utils.py                  # RSA key pair generation
├── encrypt.py               # AES encryption + RSA key wrapping
├── decrypt.py               # Constant-time decryption logic
├── test_throughput.py       # Throughput performance evaluation
├── timing_attack_test.py    # Timing attack resistance test
├── evaluate_performance.py  # Consolidated performance results
├── bank_secure_log.py       # Log viewer
├── logs/
│   └── bank_log.log         # Process logs
├── encrypted_data.bin       # Encrypted output
├── encrypted_key.pem        # RSA-encrypted AES key
├── decrypted_output.txt     # Final decrypted result
├── private.pem              # RSA private key
├── public.pem               # RSA public key
```

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/secure-hybrid-encryption.git
cd secure-hybrid-encryption
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Implementation Steps

### ✅ Step 1: Generate RSA Key Pair
- **File**: `utils.py`
- **Command**:
```bash
python utils.py
```
- **Output**: `private.pem`, `public.pem`

### ✅ Step 2: Encrypt Data
- **File**: `encrypt.py`
- **Command**:
```bash
python encrypt.py --input "Transfer $1000 to account XYZ123"
```
- **Output**: `encrypted_data.bin`, `encrypted_key.pem`

### ✅ Step 3: Decrypt Data
- **File**: `decrypt.py`
- **Command**:
```bash
python decrypt.py
```
- **Output**: `decrypted_output.txt`

### ✅ Step 4: Test Throughput
- **File**: `test_throughput.py`
- **Command**:
```bash
python test_throughput.py
```

### ✅ Step 5: Evaluate Timing Attack Resistance
- **File**: `timing_attack_test.py`
- **Command**:
```bash
python timing_attack_test.py
```

### ✅ Step 6: Evaluate Overall Performance
- **File**: `evaluate_performance.py`
- **Command**:
```bash
python evaluate_performance.py
```

### ✅ Step 7: View Logs
- **File**: `bank_secure_log.py`
- **Command**:
```bash
python bank_secure_log.py
```
- **Log Path**: `logs/bank_log.log`

---

## 📊 Results Summary

- **Encryption Time (512B)**: ~1.2 ms
- **Decryption Time**: ~2.5 ms (constant-time verified)
- **Timing Attack Test**: Passed ✅
- **Confidentiality & Integrity**: Verified in simulated online banking scenario

---

## 📌 Use Case

Ideal for SSL/TLS-based platforms, especially where sensitive financial data is transmitted. Suitable for:
- Online banking
- Digital wallets
- FinTech APIs

---
---

## 👨‍💻 Author

**K.ANUSHA** – Software Engineering , VIT  
Passionate about cybersecurity, cryptography, and building secure, high-performance systems.




