# Affine Cipher

Affine Cipher is a technique which makes use of both transformation and substitution. The core modification is:
for each character ch in text, a*ch+b is replaced in cipher

Key constraints:
a and 26 should be coprimes.
0<=b<=25

Now one thing about decryption agorithm:
We are bruteforcing for all the possible values of a and b. So 312 values are generated. One way would be manually checking through all th list. Another option would be using a wordlist which might require heavier computation.

## Installation and Execution

clone this repo and
python3 encrypt.py
python3 decrypt.py
