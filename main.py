import base64
import codecs
import urllib.parse
import argparse


def encode_text(text: str, method: str = "base64") -> str:
    """Encode given text using the selected method.

    Args:
        text: Plain string to encode.
        method: Encoding method ("base64", "hex", "rot13", "url").

    Returns:
        Encoded string. If method is invalid, returns an error string.
    """
    if method == "base64":
        return base64.b64encode(text.encode("utf-8")).decode("utf-8")
    if method == "hex":
        return text.encode("utf-8").hex()
    if method == "rot13":
        return codecs.encode(text, "rot_13")
    if method == "url":
        return urllib.parse.quote(text)
    return "❌ Noto'g'ri usul!"


def decode_text(text: str, method: str = "base64") -> str:
    """Decode encoded text using the selected method.

    Args:
        text: Encoded string to decode.
        method: Decoding method ("base64", "hex", "rot13", "url").

    Returns:
        Decoded string if successful, otherwise an error message.
    """
    try:
        if method == "base64":
            return base64.b64decode(text.encode("utf-8")).decode("utf-8")
        if method == "hex":
            return bytes.fromhex(text).decode("utf-8")
        if method == "rot13":
            return codecs.decode(text, "rot_13")
        if method == "url":
            return urllib.parse.unquote(text)
        return "❌ Noto'g'ri usul!"
    except Exception as error:
        return f"❌ Xatolik: {str(error)}"


def main():
    """Command-line interface for Encoder/Decoder."""
    parser = argparse.ArgumentParser(description="Encoder/Decoder CLI App")
    parser.add_argument(
        "mode",
        choices=["encode", "decode"],
        help="Ishlash rejimi: encode yoki decode",
    )
    parser.add_argument(
        "text",
        help="Matn (encode uchun) yoki kodlangan matn (decode uchun)",
    )
    parser.add_argument(
        "--method",
        choices=["base64", "hex", "rot13", "url"],
        default="base64",
        help="Usulni tanlang",
    )

    args = parser.parse_args()

    if args.mode == "encode":
        print("Encoded:", encode_text(args.text, args.method))
    else:
        print("Decoded:", decode_text(args.text, args.method))


if __name__ == "__main__":
    main()
