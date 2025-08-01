import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_coprime(a, m):
    return gcd(a, m) == 1

def mod_inverse(a, m):
    # Find the modular inverse
    if not is_coprime(a, m):
        return None
    
    # Extended Euclidean Algorithm
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, y = extended_gcd(a, m)
    return (x % m + m) % m

def affine_cipher_decode(cipher_text, a, b):
    """
    Decode an Affine cipher string using parameters a and b.
    Formula: D(y) = a^(-1) * (y - b) mod 26
    """
    # Find modular inverse of a
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return None
    
    decoded = ""
    
    for char in cipher_text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # Convert to 0-25 range
            y = ord(char) - ascii_offset
            
            # Apply inverse affine transformation: a^(-1) * (y - b) mod 26
            decoded_x = (a_inv * (y - b)) % 26
            
            # Convert back to character
            decoded_char = chr(decoded_x + ascii_offset)
            decoded += decoded_char
        else:
            # Keep non-alphabetic characters unchanged
            decoded += char
    
    return decoded

def get_valid_a_values():
    valid_a = []
    for a in range(1, 26):
        if is_coprime(a, 26):
            valid_a.append(a)
    return valid_a

def brute_force_decode(cipher_text):
    results = {}
    valid_a_values = get_valid_a_values()
    
    print(f"Cipher text: {cipher_text}")
    print(f"Valid 'a' values: {valid_a_values}")
    print(f"Total combinations to try: {len(valid_a_values)} * 26 = {len(valid_a_values) * 26}")
    print("\nAll possible decodings:")
    print("-" * 70)
    print(f"{'a':>2} {'b':>2} {'Decoded Text'}")
    print("-" * 70)
    
    for a in valid_a_values:
        for b in range(26):
            decoded = affine_cipher_decode(cipher_text, a, b)
            if decoded is not None:
                results[(a, b)] = decoded
                print(f"{a:2d} {b:2d}: {decoded}")
    
    return results

def main():
    print("Affine Cipher Decoder (Brute Force)")
    print("Formula: D(y) = a^(-1) * (y - b) mod 26")
    print()
    
    # Read cipher text from user
    cipher_text = input("Enter the Affine cipher to decode: ")
    
    # Generate all possible decodings
    all_decodings = brute_force_decode(cipher_text)
    
    # Optional: Ask user to identify the correct decoding
    print("\n" + "=" * 70)
    print("Please look through the results above to find meaningful text.")

if __name__ == "__main__":
    main()
