import math

def gcd(a,b):
	while b:
		a,b=b,a%b
	return a

def is_coprime(a,m):
	return gcd(a,m)==1

def affine_cipher_encode(text,a,b):
	encoded=""

	for char in text:
		if char.isalpha():
			ascii_offset=ord('A') if char.isupper() else ord('a')
			x=ord(char)-ascii_offset

			#Affine Transformation
			encoded_x=(a*x+b)%26
			encoded_char=chr(encoded_x+ascii_offset)
			encoded+=encoded_char

		else:
			encoded+=char

	return encoded

def get_valid_a():
	#Funtion to find valid values of a. a should follow a%26!=0 and the value a would be less than 26
	valid_a=[]
	for a in range(1,26):
		if is_coprime(a,26):
			valid_a.append(a)

	return valid_a

def main():
	print("Affine Character Encoder\n")
	print("Formula: E(x)=ax+b\n")
	print(f"Valid values of a:{get_valid_a}")

	input_string=input("Enter the string:")
	while True:
		try:
			a=int(input("Enter the value of a:"))
			if not is_coprime(a,26):
				print(f"Error: a value must be coprime with 26. Valid values: {get_valid_a}\n")
				continue
			break
		except ValueError:
			print("Please enter a valid value\n")
	while True:
		try:
			b=int(input("Enter the value of b:"))
			if 0<=b<=25:
				break
			else:
				print("Vaue of b should be between 0 and 25, both included\n")
		except ValueError:
			print("Please enter a valid value\n")

	encoded_string=affine_cipher_encode(input_string,a,b)
	if encoded_string is not None:
		print(f"Original Text: {input_string}\n")
		print(f"Cipher Text: {encoded_string}\n")
	else:
		print("Encoded Failed\n")

if __name__=="__main__":
	main()
