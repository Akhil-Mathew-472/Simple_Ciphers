def caesar_cipher_encode(text, key=3):
    encoded = ""

    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')


            shifted = (ord(char) - ascii_offset + key) % 26
            encoded_char = chr(shifted + ascii_offset)
            encoded += encoded_char
        else:
            encoded += char

    return encoded

def main():
    # Read input string from user
    input_string = input("Enter the string to encode: ")
    encoded_string = caesar_cipher_encode(input_string, 3)

    print(f"Original string: {input_string}")
    print(f"Encoded string (key=3): {encoded_string}")

    return encoded_string

if __name__ == "__main__":
    main()
