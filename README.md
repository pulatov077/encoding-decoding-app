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

## Dist Bo'limi
### Uning ichida .exe fayl Windows uchun yuklab ishlataversa buladi va Linux/MacOS uchun alohida app versiyasi bor dasturni.!!!

## 🪟 Windows foydalanuvchilari uchun
```bash 
dist/ papkasidagi main.exe faylni yuklab oling.

Faylni ikki marta bosib ishga tushiring.

Matn kiriting, usulni tanlang (base64, hex, rot13, url), va:

Encode tugmasini bosing — matn kodlanadi.

Decode tugmasini bosing — matn dekodlanadi.

Natija oynaning pastki qismida chiqadi
```

## 🚀 Ishlatish

### 1️⃣ Encode qilish

```bash
#base64
python main.py encode "salom" --method base64
# 🔒 Encoded: c2Fsb20=


#hex
python main.py encode "hello" --method hex
# 🔒 Encoded: 68656c6c6f
```
### 2️⃣ Decode qilish

```bash
#base64
python main.py decode "c2Fsb20=" --method base64
# 🔓 Decoded: salom


#hex
python main.py decode "68656c6c6f" --method hex
# 🔓 Decoded: hello
```

### 3️⃣ Boshqa usullar

ROT13:

```bash
python main.py encode "python" --method rot13
# 🔒 Encoded: clguba

```
URL Encoding:
```bash
python main.py encode "https://yandex.uz/" --method url
# 🔒 Encoded:  https%3A//yandex.uz/

```

## 🆘 Yordam(Support)
```bash
python main.py encode --help

```
