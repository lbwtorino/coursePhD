#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:42:00 2018

@author: liubowen
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:54:28 2018

@author: liubowen
"""
#from Cryptodome.Cipher import AES
#from Cryptodome.Cipher import AES
from Crypto.Cipher import AES
#from PyCrypto import AES
import binascii
import time
import hashlib
import hmac
import os
from Crypto.Util import Counter
#import seed
import random
from random import seed
from Crypto.Hash import SHA256

h = SHA256.new()
h.update('Hello')
#print len(h.hexdigest())
#==============================================
def md5():
    m = hashlib.md5()
    m.update("Nobody inspects")
    m.update(" the spammish repetition")
    return m.digest().encode('hex')
#print md5()
#import hmac
#import hashlib
#import base64
#dig = hmac.new(b'1234567890', msg=your_bytes_string, digestmod=hashlib.sha256).digest()
#base64.b64encode(dig).decode()      # py3k-mode
#'Nace+U3Az4OhN7tISqgs1vdLBHBEijWcBeCqL5xN9xg='
plain = ('48656C6C6F2C20776F726C642E202020').decode('hex')
#print plain
#print plain
def sha():
    return (hashlib.sha256(plain).hexdigest())
#print sha()

def Hmac():
    key = ('0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b').decode('hex')
    msg = ('4D4143732061726520766572792075736566756C20696E2063727970746F67726170687921').decode('hex')
    h = hmac.new(key, msg, hashlib.sha256)
    return len(h.hexdigest())
#print Hmac()

#exercise-1
def Sha1():
    str1= "51.505-Foundations-of-Cybersecurity-MSSD"
    str2= "51.505-Foundations-of-Cybersecurity-MSSd"
    return (hashlib.sha1(str1).hexdigest()), (hashlib.sha1(str2).hexdigest())
#print Sha1()

#exercise-2
def Hmac256():
    key = ('0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b').decode('hex')
    msg = ('4869205468657265').decode('hex')
    h = hmac.new( key, msg, hashlib.sha256 )
    return (h.hexdigest())
#print Hmac256()

#exercise-4
def preImage8():
    start = time.time()
    counter = 0
    while(True):
        states = (hashlib.sha512(str(counter)).hexdigest())[:2] == '00'
        if (states == True):
            break;
        counter = counter+1
    end = time.time()
    return end-start, counter 
#print (preImage8())
#print hashlib.sha512(str(61)).hexdigest()
    
def preImage16():
    start = time.time()
    counter = 0
    while(True):
        states = (hashlib.sha512(str(counter)).hexdigest())[:4] == '0000'
        if (states == True):
            break;
        counter = counter+1
    end = time.time()
    return end-start, counter 
#print (preImage16())
#print hashlib.sha512(str(6899310)).hexdigest()


def preImage24():
    start = time.time()
    counter = 0
    while(True):
        states = (hashlib.sha512(str(counter)).hexdigest())[:6] == '000000'
        if (states == True):
            break;
        counter = counter+1
    end = time.time()
    return end-start, counter 
#print (preImage24())
#print hashlib.sha512(str(6899310)).hexdigest()

def preImage32():
    start = time.time()
    for i in range(2**16):
        for j in range(2**16):
            states = (hashlib.sha512(str(i*2**16+j)).hexdigest())[:8] == '00000000'
            print i*2**16+j
            if (states == True):
                end = time.time()
                return end-start, i*2**16+j
#print (preImage32())
#print hashlib.sha512(str(6899310)).hexdigest()

def preImage40():
    start = time.time()
    for i in range(2**20):
        for j in range(2**20):
            states = (hashlib.sha512(str(i*2**20+j)).hexdigest())[:10] == '0000000000'
            print i*2**20+j
            if (states == True):
                end = time.time()
                return end-start, i*2**20+j
#print (preImage40())


#exercise-3
def collision():
    start = time.time()
    msg1 = hashlib.sha512('mssd').hexdigest()[:2]
    counter = 0
    while(True):
        states = (hashlib.sha512(str(counter)).hexdigest())[:2] == msg1
        if (states == True):
            break;
        counter = counter+1
    end = time.time()
    return end-start, counter 
#print collision()
#print hashlib.sha512(str(14)).hexdigest()[:2]

def collision16():
    start = time.time()
    msg1 = hashlib.sha512('mssd').hexdigest()[:4]
    counter = 0
    while(True):
        states = (hashlib.sha512(str(counter)).hexdigest())[:4] == msg1
        if (states == True):
            break;
        counter = counter+1
    end = time.time()
    return end-start, counter 
#print collision16()

def collision24():
    start = time.time()
    msg1 = hashlib.sha512('mssd').hexdigest()[:6]
    counter = 0
    while(True):
        states = (hashlib.sha512(str(counter)).hexdigest())[:6] == msg1
        if (states == True):
            break;
        counter = counter+1
    end = time.time()
    return end-start, counter 
#print collision24()

def collision32():
    start = time.time()
    msg1 = hashlib.sha512('mssd').hexdigest()[:8]
    counter = 0
    while(True):
        states = (hashlib.sha512(str(counter)).hexdigest())[:8] == msg1
        if (states == True):
            break;
        counter = counter+1
    end = time.time()
    return end-start, counter 
#print collision32()

#==============================================



#==============================================
#key = 'abcdefghijklmnop'
#cipher = AES.new(key, AES.MODE_ECB)
#msg =cipher.encrypt('TechTutorialsX!!TechTutorialsX!!')
#print (type(msg))
#print(msg.encode("hex"))
# 
#decipher = AES.new(key, AES.MODE_ECB)
#print(decipher.decrypt(msg))
#==============================================
#week-5 exercise-1
#key = '00000000000000000000000000000000'.decode('hex')
#cipher = AES.new(key, AES.MODE_ECB)
#ciphertext = cipher.encrypt('SUTD-MSSD-51.505*Foundations-CS*')
##print 'The ciphertext is:', ciphertext.encode('hex')
#
##decipher = AES.new(key, AES.MODE_ECB)
##print cipher.decrypt(ciphertext)
#
#cipher_swap = 'c97b2e6400a34bbde36f48684376dda8885c4ce846078dea93b799e0bab3e710'.decode('hex')
##print 'The plaintext after swapping is:\n', cipher.decrypt(cipher_swap)
#
#cipher_revise = '885c4ce846078dea93b799e0bab3e710c97b2e6400a34bbde36f48684376dda9'.decode('hex')
#print 'The plaintext after altering is:\n', cipher.decrypt(cipher_revise)
#

#============================================ ==
#key = "aaaabbbbccccdddd"
#cipher = AES.new(key, AES.MODE_ECB)
#with open("BLK.BMP", "rb") as f:
#  clear = f.read()
#  
#print len(clear)
#print len(clear)%16
## -6 is generated by len(clear)%16
#clear_trimmed = clear[64:-6]
#ciphertext = cipher.encrypt(clear_trimmed)
#
#ciphertext = clear[0:64] + ciphertext + clear[-6:]
#with open("blk2.bmp", "w") as f:
#  f.write(ciphertext)
#==============================================
key = ('56e47a38c5598974bc46903dba290349').decode('hex')
IV = ('8ce82eefbea0da3c44699ed7db51b7d9').decode('hex')
plaintext1 = ('a0a1a2a3a4a5a6a7a8a9aaabacadaeaf').decode('hex')
plaintext2 = ('b0b1b2b3b4b5b6b7b8b9babbbcbdbebf').decode('hex')
plaintext3 = ('c0c1c2c3c4c5c6c7c8c9cacbcccdcecf').decode('hex')
plaintext4 = ('d0d1d2d3d4d5d6d7d8d9dadbdcdddedf').decode('hex')
#print plaintext1
#print len(plaintext1 + plaintext2 + plaintext3 + plaintext4)
cipher = AES.new(key, AES.MODE_CBC,IV)
ciphertext = cipher.encrypt(plaintext1 + plaintext2 + plaintext3 + plaintext4)
#print len(ciphertext)
cipher = AES.new(key, AES.MODE_CBC,IV)
plain = cipher.decrypt(ciphertext).encode('hex')
#print plain
#==============================================

#week-5 exercise-2
#key = ('8000000000000000000000000000000000000000000000000000000000000001').decode('hex')
#IV = ('87F348FF79B811AF3857D6718E5F0F91').decode('hex')
#ciphertext = ('7C3D26F77377635A5E43E9B5CC5D05926E26FFC5220DC7D405F1708670E6E017').decode('hex')
#cipher = AES.new(key, AES.MODE_CBC, IV)
#print 'The plaintext is:\n', cipher.decrypt(ciphertext)



#========================================================
#exercise-3
#key = binascii.hexlify('\x00'*int(8))
#IV = binascii.hexlify('\x00'*int(8))
#def CBCLibrary():
#    plaintex = ''
#    for i in range (int(10**3)):
#        for j in range(int(2*10**4)):
#            plaintex += (binascii.hexlify('\x00')*int(8))
#    cipher = AES.new(key, AES.MODE_CBC, IV)
#    return (cipher.encrypt(plaintex).encode('hex'))
#start = time.time()
#print CBCLibrary()
#end = time.time()
#print (end - start)

#print len(binascii.hexlify('\x00'*int(8)))
# 1pure CBC
#def CBCPure():
#    res = ''
#    C = ''
#    for i in range(int(2*10**4)):
#        for j in range(int(10**3)):
#            cipher = AES.new(key, AES.MODE_CBC, IV)
#            if i +j == 0:
#                C0 = binascii.hexlify('\x00'*int(8))
#                C = C0;
#                P = binascii.hexlify('\x00'*int(8))
#                res += cipher.encrypt(P).encode('hex')
#                C = res;
#                continue;
#            P = binascii.hexlify('\x00'*int(8))
#            size = len(format(int(P, 16) ^ int(C, 16), 'x'))
#            if size == 32:
#                xor_res = format(int(P, 16) ^ int(C, 16), 'x').decode('hex')
#            else:
#                diff = 32 - size;
#                xor_res = ('0'*diff+format(int(P, 16) ^ int(C, 16), 'x')).decode('hex')
#            C = cipher.encrypt(xor_res).encode('hex')
#            res += C
#    return (res)
#start = time.time()
#print CBCPure()
#end = time.time()
#print (end - start)
##    
##print CBCLibrary()
#print CBCPure()
#C0 = binascii.hexlify('\x00'*int(8))
#cipher = AES.new(key, AES.MODE_CBC, IV)
#res = ''
#C = C0;
#P = binascii.hexlify('\x00'*int(8))
#res += cipher.encrypt(P).encode('hex')
#C = res;
#print C
#for i in range(3):
#    cipher = AES.new(key, AES.MODE_CBC, IV)
#    P = binascii.hexlify('\x00'*int(8))
#    xor_res = format(int(P, 16) ^ int(C, 16), 'x').decode('hex')
##    print 'len xor:', len(xor_res)
##    print 'Xor_res:', (xor_res)
#    C = cipher.encrypt(xor_res).encode('hex')
##    print 'C:', C
##    print 'len C:', len(C)
#    res += C
#print (res)
### test 2
#plaintex = ''
#for i in range (10):
#    plaintex += (binascii.hexlify('\x00')*int(8))
#cipher = AES.new(key, AES.MODE_CBC, IV)
#print (cipher.encrypt(plaintex).encode('hex'))

#======================================================
#exercise-6

#C_to_int = int("4664DC0697BBFE69330715079BA6C23D", 16)
#Cprime_to_int = int("517ECC05C3BDEA3B33570E1BD897D530", 16)
#P_to_int = int("43727970746F67726170687920437279", 16)
#
#Pprime = format((C_to_int ^ P_to_int ^ Cprime_to_int), 'x')
#print Pprime

#print hex(int(Pprime, 16) ^ Cprime_to_int ^ P_to_int)
#======================================================

#key = ('00000000000000000000000000000000').decode('hex')
#IV = ('00000000000000000000000000000000').decode('hex')
#msg1 = ('a0a1a2a3a4a5a6a7a8a9aaabacadaeaf').decode('hex')
#cipher1 = AES.new(key, AES.MODE_CBC,IV)
#tag1 = cipher1.encrypt(msg1).encode('hex')
#print tag1
#
#msg1_to_int = int("a0a1a2a3a4a5a6a7a8a9aaabacadaeaf", 16)
#tag1_to_int = int(tag1, 16)
#msg2 = format((msg1_to_int ^ tag1_to_int), 'x').decode('hex')
#cipher2 = AES.new(key, AES.MODE_CBC,IV)
#tag2 = cipher2.encrypt(msg1+msg2).encode('hex')[32:64]
#print tag2
#=================================================
random.seed(1)  
#print random.random()
random.seed(4)
#print random.randint(1, 10)
#==================================
#os.urandom(16)
#key = 'abcdefghijklmnop'
#ctr = Counter.new(128)
#crypto = AES.new(key, AES.MODE_CTR, counter = ctr)
#crypto = AES.new(os.urandom(32), AES.MODE_CTR, counter = lambda : os.urandom(16))
#encrypted = crypto.encrypt('aaaaaaaaaaaaaaaa')
#print encrypted.encode('hex')
#crypto1 = AES.new(key, AES.MODE_CTR, counter = ctr)
#print (crypto.decrypt(encrypted).encode('hex'))
#===============================================
#exercise-1
#from Cryptodome.Cipher import AES
#IV_1 = '0000000000000000'
#key_1 = '1111111111111111'
#encryptor = AES.new(key_1, AES.MODE_GCM, IV_1)
#ciphertext, tag = encryptor.encrypt_and_digest('SUTD-MSSD-51.505*Foundations-CS*SUTD-MSSD-51.505')
#print binascii.hexlify(ciphertext), binascii.hexlify(tag)
#print len(ciphertext.encode('hex'))
#decryptor = AES.new(key_1, AES.MODE_GCM, IV_1)
#print decryptor.decrypt_and_verify(binascii.unhexlify('0f3578c16aecd9e4bbb0d8f52f0e4f0fce8aaa8490d12a99e538f499eabab47b16042f8a8df1c09dee68e56a1a1d9157'), tag)
#print binascii.hexlify(decryptor.decrypt(binascii.unhexlify('0f3578c16aecd9e4bbb0d8f52f0e4f0fce8aaa8490d12a99e538f499eabab47b16042f8a8df1c09dee68e56a1a1d9157')))

#print decryptor.decrypt_and_verify(binascii.unhexlify('16042f8a8df1c09dee68e56a1a1d9157ce8aaa8490d12a99e538f499eabab47b'), tag)
#print decryptor.decrypt(binascii.unhexlify('16042f8a8df1c09dee68e56a1a1d9157ce8aaa8490d12a99e538f499eabab47b'))

#print decryptor.decrypt_and_verify(binascii.unhexlify('16042f8a8df1c09dee68e56a1a1d9157ce8aaa8490d12a99e538f499eabab47b0f3578c16aecd9e4bbb0d8f52f0e4f0e'), tag)
#print decryptor.decrypt(binascii.unhexlify('16042f8a8df1c09dee68e56a1a1d9157ce8aaa8490d12a99e538f499eabab47b0f3578c16aecd9e4bbb0d8f52f0e4f0e'))
#16042f8a8df1c09dee68e56a1a1d9157
#ce8aaa8490d12a99e538f499eabab47b
#0f3578c16aecd9e4bbb0d8f52f0e4f0f

#===============================================
#print len(hashlib.sha256(format(0, 'x')).hexdigest()[:16])

from Cryptodome.Protocol import KDF
from Crypto.Hash import SHA256
master = "abcd"
array = (KDF.HKDF(master, salt=None, key_len=32, hashmod=SHA256, num_keys=2, context=None))
#print len(array[0].encode('hex')), (binascii.hexlify(array[1]))
#
#print (("Msg from alice to bob").encode('hex'))
#print (("Msg from alice to bob").encode('hex') + (16 - len("Msg from alice to bob") % 16)*'80')

class Peer(object):
    def __init__(self, key):
        self.share_key = key;
        #set counter for sending and receiving
        self.sender_counter = 0;
        self.receiver_counter = 0;
        #derive the encryption key and authentication key from share_key
        self.encry_key = (KDF.HKDF(self.share_key, salt=None, key_len=32, hashmod=SHA256, num_keys=2, context=None))[0]
        self.auth_key = (KDF.HKDF(self.share_key, salt=None, key_len=32, hashmod=SHA256, num_keys=2, context=None))[1]
        
    def send(self, msg):
        #generate a new IV based on current 
        #sender_counter for each sending process
        IV = hashlib.sha256(format(self.sender_counter, 'x')).hexdigest()[:16]
        cipher = AES.new(self.encry_key, AES.MODE_CBC, IV)
        #padding if needed
        #use '0x80' + rest is '0x00' padding mode
        if len(msg) % 16 == 0:
            message = msg
        else:
            message = msg.encode('hex') + '80' + (16 - len(msg) % 16 - 1)*'00'
        ciphertext = binascii.hexlify(cipher.encrypt(message))
        authtext = (hmac.new(self.auth_key, ciphertext, hashlib.sha256).hexdigest())
        counter_len = len((format(self.sender_counter, 'x')))
        #set counter to 32-bit(4 bytes)
        #each format() has 4-bit so 32-bit == (4*2) * 4-bit
        if counter_len < 4*2:
            counter = (4*2 - counter_len)*'0' + (format(self.sender_counter, 'x'))
        else:
            counter = counter_len
        #sending message is counter || ciphertext || authtext
        protected_msg = counter + ciphertext + authtext
        #increase the sender_counter
        self.sender_counter += 1
        print 'whole sending message is:', counter, (ciphertext), (authtext)
        return protected_msg
    
    def receive(self, protected_msg):
        size = len(protected_msg)
        #extract authtext (last 256-bit)
        authtext =  protected_msg[size-64:]
        #extract ciphertext (middle part)
        ciphertext = (protected_msg[8:size-64])
        #extract counter (first 32-bit)
        counter = int(protected_msg[0:8], 16)
        #first verify the authtext
        verify_authtext = hmac.new(self.auth_key, (ciphertext), hashlib.sha256).hexdigest()
        if (authtext == verify_authtext):
            #generate the IV which is same as the sender
            IV = hashlib.sha256(format(counter, 'x')).hexdigest()[:16]
            cipher = AES.new(self.encry_key, AES.MODE_CBC, IV)
            msg = cipher.decrypt((ciphertext).decode('hex'))
            #remove the padding
            msg_size = len(msg)
            for i in range(msg_size / 2):
                if msg[msg_size-2:] == '00':
                    msg = msg[0:msg_size-2]
                    msg_size -= 2
                    continue;
                if msg[msg_size-2:] == '80':
                    msg = msg[0:msg_size-2]
                    msg_size -= 2
                    break;
            #increase the receiver_counter
            self.receiver_counter += 1
            #print the native message
            print 'message to receiver is:', binascii.unhexlify(msg)
        else:
            print 'authenticate failed!'

#alice = Peer("very secret key!")
#bob = Peer("very secret key!")
#
#msg1 = alice.send("Msg from alice to bob")
#bob.receive(msg1)
#
#msg2 = alice.send("Another msg from alice to bob")
#bob.receive(msg2)
#
#msg3 = bob.send("Hello alice")
#alice.receive(msg3)


#==================================
import matplotlib.pyplot as plt
import numpy as np

def native():
    bit_array = np.random.randint(0, 2, size=8)
    total = 0
    for i in range(8):
        total += bit_array[i] * 2**(8-1-i)
    res = total % 128
    return res
#    total = 0
#    for i in range(8):
#        total += random.randint(0, 1) * 2**(8-1-i)
#    res = total % 128
#    return res

def Multiple(num):
    number = []
    for i in range(num):
        number.append(native())
    return number

#histogram = Multiple(512)
#print histogram
#plt.hist(histogram, bins=128, color='blue', edgecolor='black', align='left') 
#plt.xlabel('Random value')
#plt.ylabel('Freq')
#plt.savefig('distribution.pdf')

#=====================================
#from Crypto.PublicKey import RSA
#import ast
#
#key = RSA.generate(1024)
#print key.exportKey('PEM')
#
#publickey = key.publickey()
#print  publickey
#
#encrypted = publickey.encrypt('hello world!', 32)
#print 'encrypted message:', (encrypted[0]).encode('hex') 
#
#decrypted = key.decrypt(encrypted)
#print 'decrypted', decrypted
#=============================
from fractions import gcd
#print gcd(20,8)
def egcd(a, b):
    u, u1 = 1, 0
    v, v1 = 0, 1
    g, g1 = a, b
    while g1:
        q = g // g1
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        g, g1 = g1, g - q * g1
    return g, u, v
#print egcd(74,167)

#=======================
#from Crypto.Signature import PKCS1_v1_5
#from Crypto.Hash import SHA256
#from Crypto.PublicKey import RSA
#message = 'To be signed!!'
##key = RSA.import_key(open('private_key.der').read())
#key = RSA.generate(1024)
#publickey = key.publickey()
#print publickey.exportKey('PEM')
#h = SHA256.new(message)
#signature = PKCS1_v1_5.new(key).sign(h)
#print signature
#print 'The certificate authentication is:', True;
##print len(signature.encode('hex'))
#
#h = SHA256.new(message)
#print PKCS1_v1_5.new(publickey).verify(h, signature), time.time(), time.time()+10*365*24*60*60
#=================
def Prime(n):
	if n <=1: return False
	i = 2
	while i*i <= n:
		if n%i == 0 : return False
		i += 1
	return True

#print isinstance(1, (int, long, float))
#print isinstance(1.4, int)
#================
#p=141301# publicly known 
#g=5728435 # publicly known
#x=76435 # only Alice knows this 
#y=37846 # only Bob knows this
#aliceSends = (g**x)%p 
#aliceComputes = (bobSends**x)%p
#bobSends = (g**y)%p
#bobComputes = (aliceSends**y) %p
#bobSends = (g**y)%p
#bobComputes = (aliceSends**y) %p
#print ("Alice sends    ", aliceSends )
#print ("Bob computes   ", bobComputes )
#print ("Bob sends      ", bobSends)
#print ("Alice computes ", aliceComputes)
#==============================
#p = 23    # p
#g = 5      # g
#alice = 6     # a
#bob = 15      # b
#
#print( "p: " , p )
#print( "g: " , g )
# 
## Alice Sends Bob A = g^a mod p
#A = pow(g, alice) % p
#print( "Alice sending message: " , A )
# 
## Bob Sends Alice B = g^b mod p
#B = pow(g, bob) % p
#print( "Bob sending message: ", B )
# 
#print( "===========================" )
## Alice Computes Shared Secret: s = B^a mod p
#aliceSecret = (B ** alice) % p
#print( "Alice Shared info: ", aliceSecret )
# 
## Bob Computes Shared Secret: s = A^b mod p
#bobSecret = (A**bob) % p
#print( "Bob Shared info: ", bobSecret )
#===================
    
from fractions import gcd
from Crypto.Hash import SHA256

def calculateD(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

p = 71
q = 89
n = p * q
m = (p-1) * (q-1)
e = 3
d = 4107
#
m1 = 5416
m2 = 2397
m3 = (m1*m2) % n
#print 'm1:', m1
#print 'm2:', m2
#print 'm3:', m3

sig1 = (m1**d) % n
sig2 = (m2**d) % n
sig3 = (m3**d) % n

#print 'sig1:', sig1
#print 'sig2:', sig2
#print 'sig3:', sig3
#print (sig1 * sig2) % n == sig3

verify1 = (sig1**e) % n
verify2 = (sig2**e) % n
verify3 = (sig3**e) % n
#print 'verify1', verify1
#print 'verify2', verify2
#print 'verify3', verify3

s1 = (m1**e) % n
s2 = (m2**e) % n
s3 = (m3**e) % n
#print 'e1:', s1
#print 'e2:', s2
#print 'e3:', s3

sm1 = (s1**d) % n
sm2 = (s2**d) % n
sm3 = (s3**d) % n
#print 's1:', sm1
#print 's2:', sm2
#print 's3:', sm3
#=======================================

#print int('ffff', 16)
#print math.log(16,2)
#print 1 != 2

for i in range(1000):
    if 89 * i % 79 == 1:
        print i
        
print (-16) % 79
print 5612 % 79, 5612 % 89
#print 1429 % 79, 1429 % 89



