import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


#compute X coordinate of public key based on private key k
#and starting point G on the curve secp256k1  (Y**Y = X**3 + 7), using 62 bit prime
"""n = int(input())
P = 0x3fddbf07bb3bc551
B = 7
G = (0x69d463ce83b758e, 0x287a120903f7ef5c)
#curve = ((x**3) + b) % p
for i in range(n):
    k = input()
    X, Y = point_multiply(k, G, P)

    #define curve 
    #coordinate = k * g
    #Fermat's Theorum for modular inverse
    def mod_inverse(a, p): 
        return pow(a, p - 2, p)

    #point addition on elliptic curve
    def point_add(C, D, P):
        #define Xc and Yc as C
        Xc, Yc = C
        #define Xd and Yd as D
        Xd, Yd = D
        if C == D:
            #point doubling 
            L = (3 * Xc**2) * mod_inverse(2 * Yc, P) % P
        else:
            #C !=D
            L = (Yd - Yc) * mod_inverse(Xd - Xc, P) % P
            
        Xs = (L**2 - Xc - Xd) % P
        Ys = (L * (Xc - Xs) - Yc) % P

        return (Xs, Ys)

    #point multiplication 
    def point_multiply(k, G, P):
        result = (0, 0) #neutral element
        base = G #set base to G

        while k > 0:
            if k % 2 == 1:
                result = point_add(result, base, P)
            base = point_add(base, base, P)
            k //= 2

        return result

print(hex(X)[2:])"""

#    xG = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
#    yG = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08F26BCA2A6
#    G = (xG, yG)
#    twoC = (xG -yG)
    #get C+D
    #private key
#    key = g
#    print(twoC)

# Define P, A and B
P = 0x3fddbf07bb3bc551  # The prime field as 62 bit rather than usual 256
A = 0  
B = 7 

# G = (X_G, Y_G)
G = (0x69d463ce83b758e, 0x287a120903f7ef5c)

# Modular inverse using Fermat's Little Theorem
def modinv(a, p):
    return pow(a, p - 2, p)

# Point doubling on the elliptic curve
def point_double(C):
    Xc, Yc = C
    if Yc == 0:  # Adding prevented incorrect results
        return (0, 0)
    num = (3 * Xc**2 + A) % P 
    denom = (2 * Yc) % P
    L = (num * modinv(denom, P)) % P #L  = (Yd - Yc) / (Xd - Xc)  mod P
    Xs = (L**2 - 2 * Xc) % P #Xs = L² - Xc - Xd           mod P
    Ys = (L * (Xc - Xs) - Yc) % P #Ys = L * (Xc - Xs) - Yc     mod P
    return (Xs, Ys)

# Point addition on the elliptic curve
def point_add(C, D):
    Xc, Yc = C
    Xd, Yd = D
    if C == (0, 0):  # Identity point
        return D
    if D == (0, 0):  # Identity point
        return C
    if Xc == Xd and Yc != Yd:  # Opposite points
        return (0, 0)
    num = (Yd - Yc) % P
    denom = (Xd - Xc) % P
    L = (num * modinv(denom, P)) % P
    Xs = (L**2 - Xc - Xd) % P
    Ys = (L * (Xc - Xs) - Yc) % P
    return (Xs, Ys)

# Double and add method for scalar multiplication of point G
def scalar_multiply(k, G):
    result = (0, 0)  # The identity point for the elliptic curve
    addend = G
    while k > 0:
        if k & 1:  # Check if the least significant bit is 1
            result = point_add(result, addend)
        addend = point_double(addend)
        k >>= 1
    return result

# Main function
def main():

    n = int(input()) 
    for _ in range(n):
        k = int(input(), 16)  
        result = scalar_multiply(k, G)  # PScalar multiplication
        print(hex(result[0]))  #X coordinate in hex format
        print(k)
        print(n)
# Use main function to execute
if __name__ == "__main__":
    main()
