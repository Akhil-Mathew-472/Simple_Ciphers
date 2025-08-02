def atbash_cipher_encode(text):
	encoded=""
	for char in text:
		if char.isalpha():
			if char.isupper():
				old_pos=ord(char)-ord('A')
				new_pos=25-old_pos
				encoded_char=chr(new_pos+ord('A'))
			else:
				old_pos=ord(char)-ord('a')
				new_pos=25-old_pos
				encoded_char=chr(new_pos+ord('a'))
			encoded+=encoded_char
		else:
			encoded+=char

	return encoded

def main():
	print("Atbash Cipher Encoder\n")
	print("-"*60)
	input_string=input("Enter the string:")
	encoded_string=atbash_cipher_encode(input_string)

	print(f"Original Text: {input_string}")
	print(f"Cipher Text: {encoded_string}")

if __name__=="__main__":
	main()
