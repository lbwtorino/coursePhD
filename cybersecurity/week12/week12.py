#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Cryptodome.Cipher import AES
import hashlib
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import time

class RootCA(object):
    def __init__(self):
        self.key = RSA.generate(1024)
        self.publicKey = self.key.publickey()
        
    def generateCertiChain(self, public_key):
        owner = 'IntermediaCA'
        issuer = 'RootCA'
        not_before = int(time.time())
        not_after = int(time.time() + 10*365*24*60*60)
        publicKey = public_key
        message = owner+issuer+str(not_before)+str(not_after)
        hash_message = SHA256.new(message)
        signature = PKCS1_v1_5.new(self.key).sign(hash_message)
        certificate = []
        certificate.append(owner)
        certificate.append(issuer)
        certificate.append(not_before)
        certificate.append(not_after)
        certificate.append(publicKey)
        certificate.append(signature)
        return certificate
#        return owner, issuer, not_before, not_after, publicKey, signature
        
    def applyCertificateChain(self, message, public_key, signature):
        hash_message = SHA256.new(message);
        verified = PKCS1_v1_5.new(public_key).verify(hash_message, signature)
        if verified == True:
            return self.generateCertiChain(public_key);
    
    def getPublicKey(self):
        return self.publicKey;
    
class IntermediaCA(object):
    def __init__(self):
        self.key = RSA.generate(1024)
        self.publicKey = self.key.publickey()
        self.CAdic = {}
        
    def getPKIKey(self, name, PKI_object):
        key = PKI_object.getPublicKey();
        self.CAdic[name] = key;
        
    def getPublicKey(self):
        return self.publicKey;
    
    def generateCertiChain(self, public_key):
        owner = 'Alice'
        issuer = 'IntermediaCA'
        not_before = int(time.time())
        not_after = int(time.time() + 10*365*24*60*60)
        publicKey = public_key;
        message = owner+issuer+str(not_before)+str(not_after)
        hash_message = SHA256.new(message)
        signature = PKCS1_v1_5.new(self.key).sign(hash_message)
        certificate = []
        certificate.append(owner)
        certificate.append(issuer)
        certificate.append(not_before)
        certificate.append(not_after)
        certificate.append(publicKey)
        certificate.append(signature)
        return certificate
    
    def applyToRootCA(self, message, intermedia):
        hash_message = SHA256.new(message);
        signature = PKCS1_v1_5.new(self.key).sign(hash_message)
        return intermedia.applyCertificateChain(message, self.publicKey, signature)

    def applyCertificateChain(self, message, public_key, signature):
        hash_message = SHA256.new(message);
        verified = PKCS1_v1_5.new(public_key).verify(hash_message, signature)
        if verified == True:
            return self.generateCertiChain(public_key);
    
    
class Alice(object):
    def __init__(self):
        self.key = RSA.generate(1024)
        self.publicKey = self.key.publickey()
        self.CAdic = {}

    def getPKIKey(self, name, PKI_object):
         key = PKI_object.getPublicKey();
         self.CAdic[name] = key;
    
    def applyCertificateChain(self, message, PKI_object):
        hash_message = SHA256.new(message)
        signature = PKCS1_v1_5.new(self.key).sign(hash_message)
        return PKI_object.applyCertificateChain(message, self.publicKey, signature)
    
    def sendToBob(self, certificate, send_objetc):
        return send_objetc.BobVerify(certificate)
        
class Bob(object):
    def __init__(self):
        self.key = RSA.generate(1024)
        self.publicKey = self.key.publickey();
        self.CAdic = {}
        
    def getPKIKey(self, name, PKI_object):
        key = PKI_object.getPublicKey();
        self.CAdic[name] = key;
        
    def applyCertificate(self, message, PKI_object):
        hash_message = SHA256.new(message)
        signature = PKCS1_v1_5.new(self.key).sign(hash_message)
        message, signature = PKI_object.applyCertificate(message,self.publicKey, signature)
        return message, signature
    
    def BobVerify(self, certificate):
        for cert in certificate:
            print cert
            if time.time() < cert[2] or time.time() > cert[3]:
                return False;
            message = cert[0]+cert[1]+str(cert[2])+str(cert[3]);
            hash_message = SHA256.new(message);
            verified = PKCS1_v1_5.new(self.CAdic[cert[1]]).verify(hash_message, cert[5])
            if verified == False:
                return False;
        return 'The certificate chain authentication is:', True;
            
alice = Alice()
bob = Bob()
rootca = RootCA()
intermediaca = IntermediaCA()

alice.getPKIKey('RootCA', rootca)
alice.getPKIKey('IntermediaCA', intermediaca)
bob.getPKIKey('RootCA', rootca)
bob.getPKIKey('IntermediaCA', intermediaca)

ceriFromIntermedia = alice.applyCertificateChain('I am Alice!', intermediaca)
ceriFromRoot = intermediaca.applyToRootCA('I am intermedia!', rootca)

certificateChian = [ceriFromIntermedia, ceriFromRoot]

alice.sendToBob(certificateChian, bob)
print bob.BobVerify(certificateChian)






        

