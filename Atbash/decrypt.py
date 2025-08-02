def atbash_cipher_decode(cipher_text):
	decoded=""
	for char in cipher_text:
		if char.isalpha():
			if char.isupper():
				old_pos=ord(char)-ord('A')
				new_pos=25-old_pos
				decoded_char=chr(new_pos+ord('A'))
			else:
				old_pos=ord(char)-ord('a')
				new_pos=25-old_pos
				decoded_char=chr(new_pos+ord('a'))
			decoded+=decoded_char
		else:
			decoded+=char
	return decoded


def main():
	print("Atbash Decoder\n")
	print("-"*60)

	encoded_text=input("Enter the string:")
	decoded=atbash_cipher_decode(encoded_text)
	print(f"Cipher Text: {encoded_text}")
	print(f"Decoded Text: {decoded}")

if __name__=="__main__":
	main()
