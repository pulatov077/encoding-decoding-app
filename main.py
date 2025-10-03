import base64


def encode_text(text):
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def decode_text(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode("utf-8"))
    return decoded_bytes.decode("utf-8")


def main():
    print("=== Base64 Encoder/Decoder ===")
    choice = input("Encode (e) yoki Decode (d)? ")

    if choice.lower() == "e":
        text = input("Matn kiriting: ")
        print("Encoded:", encode_text(text))
    elif choice.lower() == "d":
        encoded_text = input("Encoded matn kiriting: ")
        print("Decoded:", decode_text(encoded_text))
    else:
        print("Noto‘g‘ri tanlov!")


if __name__ == "__main__":
    main()
