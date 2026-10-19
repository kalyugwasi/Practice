# Experiment 5: RSA Key Generation, Encryption and Decryption
# Educational implementation only
import math
# Step 1: Choose two prime numbers
p = 61
q = 53
# Step 2: Calculate n
n = p * q
# Step 3: Calculate Euler's totient
phi = (p - 1) * (q - 1)
# Step 4: Choose e
e = 17
# Step 5: Find d (modular inverse of e modulo phi)
d = pow(e, -1, phi)
# Step 6: Display keys
print("Public Key :", (e, n))
print("Private Key:", (d, n))
# Step 7: Enter a message smaller than n
m = int(input(f"Enter message as an integer (0 to {n-1}): "))
if 0 <= m < n:
# Encryption
    c = pow(m, e, n)
# Decryption
    decrypted = pow(c, d, n)
    print("Original Message :", m)
    print("Encrypted Message:", c)
    print("Decrypted Message:", decrypted)
    if m == decrypted:
        print("RSA verification successful.")
    else:
        print("Invalid message. Message must be between 0 and n-1.")