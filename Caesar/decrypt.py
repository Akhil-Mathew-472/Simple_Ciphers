def caesar_cipher_decode(cipher_text, key):
	decoded=""
	for char in cipher_text:
		if char.isalpha():
			ascii_offset=ord('A') if char.isupper() else ord('a')

			shifted=(ord(char)-ascii_offset-key)%26
			decoded_char=chr(shifted+ascii_offset)
			decoded+=decoded_char

		else:
			decoded+=char
	return decoded
def brute_force_decode(cipher_text):
	result={}
	print(f"Cipher Text: {cipher_text}")
	print("\nAll possible decodeings:\n")
	print("-"*60)

	for i in range(1,26):
		decoded = caesar_cipher_decode(cipher_text, i)
		print(f"Key {i:2d}: {decoded}")

def main():
	cipher_text=input("Enter the cipher to decode: ")
	brute_force_decode(cipher_text)

if __name__=="__main__":
	main()
