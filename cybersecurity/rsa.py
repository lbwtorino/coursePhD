#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 20:04:07 2018

@author: liubowen
"""

import random

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#calculate d
def findModInverse(e, phi):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1
    if gcd(e, phi) != 1:
        return None
    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, phi
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
#    print u1, u2, u3, v1, v2, v3, u1 % phi, e, phi, u1*e+u2*phi
    return u1 % phi
#print findModInverse(3, 160)

def egcd(a,b):  # a > b > 0  
    """ Extended great common divisor, returns x , y
        and gcd(a,b) so ax + by = gcd(a,b)       """
    e, phi = a, b
    if a%b==0: return (0,1,b)
    q=[]
    while a%b != 0:
        q.append(-1*(a//b))
        (a,b)=(b,a%b)
    (a,b,gcd)=(1,q.pop(),b)
    while q:
        (a,b)=(b,b*q.pop()+a)
    print (a,b,gcd), a*e+b*phi, e, phi
    return (a,b,gcd)
print egcd(5, 6864)


def generatePrime(keysize):
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

def isPrime(n):
	if n <=1: return False
	i = 2
	while i*i <= n:
		if n%i == 0 : return False
		i += 1
	return True

def Gen(minPrime, keySize):

    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    p = generatePrime(keySize)
    if p < minPrime:
        return;
    q = generatePrime(keySize)
    if q < minPrime:
        return;
    n = p * q
    print 'p is:', p
    print 'q is:', q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    while True:
        # Keep trying random numbers for e until one is valid.
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break
    print 'e is:', e

    # Step 3: Calculate d, the mod inverse of e.
    d = findModInverse(e, (p - 1) * (q - 1))
    print 'd is:', d
    
    print 'test:', findModInverse(5, (79-1)*(89-1))

    publicKey = (n, e)
    privateKey = (n, d)
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return (publicKey, privateKey)

def Enc(pubKey, msg):
    return pow(msg, pubKey[1]) % pubKey[0]

def Dec(privKey, ctxt):
    return pow(ctxt, privKey[1]) % privKey[0]

def main():
    minPrime = 2
    publicKey, privateKey = Gen(minPrime, 10)
    msg = 10000;
    ciphertext =  Enc(publicKey, msg)
    print 'ciphertext is:', ciphertext
    print 'plaintext is:', Dec(privateKey, ciphertext)

if __name__ == '__main__':
    main()
    