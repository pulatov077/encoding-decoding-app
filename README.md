# 🔐 Encoder/Decoder CLI App

Matnlarni turli usullarda (Base64, Hex, ROT13, URL) **kodlash va dekodlash** uchun qulay CLI dastur.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📖 Loyiha haqida

Bu dastur sizga matnlarni tez va oson **encoding/decoding** qilish imkonini beradi.  
Hozircha qo‘llab-quvvatlanadigan usullar:

- 🟦 Base64
- 🟨 Hex
- 🌀 ROT13
- 🌐 URL Encoding

## ⚙️ O‘rnatish

1. Repository’ni yuklab oling:
```bash
git clone https://github.com/pulatov077/encoding-decoding-app.git
cd encoding-decoding-app
```

## 🚀 Ishlatish

### 1️⃣ Encode qilish

```bash
#base64
python app.py encode "salom" --method base64
# 🔒 Encoded: c2Fsb20=


#hex
python app.py encode "hello" --method hex
# 🔒 Encoded: 68656c6c6f
```
### 2️⃣ Decode qilish

```bash
#base64
python app.py decode "c2Fsb20=" --method base64
# 🔓 Decoded: salom


#hex
python app.py decode "68656c6c6f" --method hex
# 🔓 Decoded: hello
```

### 3️⃣ Boshqa usullar

ROT13:

```bash
python app.py encode "python" --method rot13
# 🔒 Encoded: clguba

```
URL Encoding:
```bash
python app.py encode "https://yandex.uz/" --method url
# 🔒 Encoded:  https%3A//yandex.uz/

```

## 🆘 Yordam(Support)
```bash
python app.py encode --help

```
