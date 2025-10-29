# === Simple Cryptography Case Study (Caesar & Vigenere) ===

# Fungsi Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Fungsi Vigenere Cipher
def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            shift = ord(key[key_index % len(key)]) - 97
            result += chr((ord(ch) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += ch
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            shift = ord(key[key_index % len(key)]) - 97
            result += chr((ord(ch) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += ch
    return result


# === Forensic Case ===
def forensic_case():
    print("=== Digital Forensic ===")

    # Pesan yang ditemukan
    pesan1 = "MEETING AT 10 PM"
    pesan2 = "CONFIDENTIAL DATA"

    # Enkripsi
    cipher1 = caesar_encrypt(pesan1, 5)
    cipher2 = vigenere_encrypt(pesan2, "KEY")

    print("\nEncrypted Evidence 1 (Caesar):", cipher1)
    print("Encrypted Evidence 2 (Vigenere):", cipher2)

    # Dekripsi
    print("\n[Decryption Process]")
    print("Decrypted Evidence 1:", caesar_decrypt(cipher1, 5))
    print("Decrypted Evidence 2:", vigenere_decrypt(cipher2, "KEY"))

    print("\nCase Conclusion:")
    print("The recovered messages show coordination timing between suspects.")


if __name__ == "__main__":
    forensic_case()
