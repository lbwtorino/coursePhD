#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 19:08:10 2018

@author: liubowen
"""

import random
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import math

def generatePrime(keysize):
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

def isPrime(n):
	if n <=1: return False
	i = 2
	while i*i <= n:
		if n%i == 0: return False
		i += 1
	return True                

def choose_gpq(Sa, Sb):
    alfa = 2
    g = 0
    s = max(Sa, Sb)
    if s > 2*Sb:
        return False
    while(True):      
        p = generatePrime(s)
        if math.log(p,2) < s-1:
            continue
        q = (p-1)/2
        if not isPrime(q):
            continue
        while(True):
            alfa = random.randint(2, p-2)
            g = alfa**2 % p
            if g == 1:
                continue
            if g == p-1:
                continue
            break
        b = random.randint(1, q-1)
        B = g**b % p
        break
    message = g+p+q+B
    key = RSA.generate(1024)
    publickey = key.publickey()
    h = SHA256.new(hex(message))
    signature = PKCS1_v1_5.new(key).sign(h)
    return g, p, q, b, B, alfa, publickey, signature

def receiveFromAlice(Sa, g, p, q, B, publickey, signature):
    message = g+p+q+B
    hash_message = SHA256.new(hex(message))
    if PKCS1_v1_5.new(publickey).verify(hash_message, signature) == False:
        print 'error'
    if ((Sa-1) < math.log(p,2)) & (math.log(p,2) < 2*Sa):
        if not isPrime(q):
            print 'error'
        if not isPrime(p):
            print 'error'
        if 2*q != (p-1):
            print 'error'
        if g == 1:
            print 'error'
        if g == p-1:
            print 'error'
        if B == 1:
            print 'error'
        if B**q % p != 1:
            print 'error'
        a = random.randint(1, q-1)
        A = g**a % p
        K_prime = B**a % p
        h = SHA256.new()
        h.update(hex(K_prime))
        K = h.hexdigest()
        message1 = A
        key_new = RSA.generate(1024)
        publickey_new = key_new.publickey()
        hash_new = SHA256.new(hex(message1))
        signature_new = PKCS1_v1_5.new(key_new).sign(hash_new)
        return a, A, K_prime, K, publickey_new, signature_new
    else:
        print 'error'
        
def bobReceive(A, g, p, q, b, publickey_new, signature_new):
    message = A
    hash_message = SHA256.new(hex(message))
    if PKCS1_v1_5.new(publickey_new).verify(hash_message, signature_new) == False:
        print 'error'
    if A == 1:
        print 'error'
    if A**q % p != 1:
        print 'error'
    K_prime = A**b % p
    h = SHA256.new()
    h.update(hex(K_prime))
    K = h.hexdigest()
    return K_prime, K
    
#        
Sa = 8
Sb = 10
N = random.randint(0, 2**256-1)
print '=========Alice sending Sa, N:=============='
print 'Sa is:', Sa
print 'N is:', N
print '=========Bob sending (g,p,q),B,sig(Bob):=============='
g, p, q, b, B, alfa, publickey, signature = choose_gpq(Sa, Sb)
print 'g is:', g
print 'p is:', p
print 'q is:', q
print 'B is:', B
print 'signature is:', signature.encode('hex')
print '=========Alice sending A,sig(Alice):============'
a, A, K_prime, K, publickey_new, signature_new = receiveFromAlice(Sa, g, p, q, B, publickey, signature)
print 'A is:', A
print 'K_prime is:', K_prime
print 'K:', K
print 'signature is:', signature_new.encode('hex')
print '=========Bob verify and generate K============'
K_prime_FromBob, K_FromBob = bobReceive(A, g, p, q, b, publickey_new, signature_new)
print 'K_prime_Bob is:', K_prime_FromBob
print 'K_Bob is:', K_FromBob


