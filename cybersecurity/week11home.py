#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:40:57 2018

@author: liubowen
"""

from Cryptodome.Cipher import AES
import hashlib

class KDC(object):
    def __init__(self):
        self.share_dic = {};
        
    def addSharekey(self, name, key):
        self.share_dic[name] = key;
        print self.share_dic
    
    def generateTickets(self, from_name, to_name):
        h = hashlib.sha256();
        h.update(self.share_dic[from_name]);
        h.update(self.share_dic[to_name]);
        KAB = h.hexdigest()
        print '\n====== generate KAB ============='
        print 'KAB:', KAB
        
        IV_bob = hashlib.sha256(to_name).hexdigest()[:16]
        key_bob = self.share_dic[to_name]
        encrypt = AES.new(key_bob, AES.MODE_GCM, IV_bob)
        encryptBob = encrypt.encrypt_and_digest(from_name + KAB)[0]
        print '====== KDC first generate EkB(Alice, KAB) ============='
        print 'EkB(Alice, KAB):', encryptBob.encode('hex');
        IV_alice = hashlib.sha256(from_name).hexdigest()[:16]
        key_alice = self.share_dic[from_name]
        encrypt = AES.new(key_alice, AES.MODE_GCM, IV_alice)
        encryptAlice = encrypt.encrypt_and_digest(KAB + encryptBob)[0]
        print '====== KDC then generate EkA(KAB, EkB(Alice, KAB)) ============='
        print 'EkA(KAB, EkB(Alice, KAB)):', encryptAlice.encode('hex')
        return encryptAlice
        
    
class Alice(object):
    def __init__(self, Ka):
        self.name = 'Alice';
        self.Ka = Ka;
        self.KAB ='';
        print 'kA:', self.Ka
    
    def addSharekey(self, KDC_object):
        KDC_object.addSharekey(self.name, self.Ka);
        
    def getTickets(self, name, KDC_object):
        return KDC_object.generateTickets(self.name, name);
    
    def sendToBob_getResponce(self, message, Bob_object):
        IV_alice = hashlib.sha256(self.name).hexdigest()[:16]
        key_alice = self.Ka
        decryptor = AES.new(key_alice, AES.MODE_GCM, IV_alice)
        plaintext = (decryptor.decrypt(message))
        print '====== Alice first decrypt EkA(KAB, EkB(Alice, KAB)) ====='
        print '======= then extract KAB and EkB(Alice, KAB) ============='
        self.KAB = plaintext[0:64].decode('hex')
        tickets = plaintext[64:len(plaintext)]
        print 'KAB:', self.KAB.encode('hex')
        print 'EkB(Alice, KAB):', tickets.encode('hex')
        message = Bob_object.receiveFromAlice(tickets)
        self.parse(message);
        return message;
    
    def parse(self, message):
        IV = hashlib.sha256('Bob').hexdigest()[:16];
        key = self.KAB;
        decryptor = AES.new(key, AES.MODE_GCM, IV)
        plaintext = (decryptor.decrypt(message))
        print '====== Alice decrypt EKAB(Hi, it is Bob) ============='
        print 'Alice receive:', plaintext;
        
class Bob(object):
    def __init__(self, Kb):
        self.name = 'Bob';
        self.Kb = Kb;
        self.KAB ='';
        print 'kB:', self.Kb
        
    def addSharekey(self, KDC_object):
        KDC_object.addSharekey(self.name, self.Kb);
        
    def getTickets(self, name, KDC_object):
        return KDC_object.generateTickets(self.name, name);
    
    def receiveFromAlice(self, tickets): 
        IV_bob = hashlib.sha256(self.name).hexdigest()[:16]
        key_bob = self.Kb
        decryptor = AES.new(key_bob, AES.MODE_GCM, IV_bob)
        plaintext = (decryptor.decrypt(tickets))
        print '====== Bob first decrypt EkB(Alice, KAB) ============='
        print 'Alice||KAB:', plaintext
        print '====== Bob then extract Alice and KAB ============='
        self.KAB = plaintext[5:len(plaintext)].decode('hex')
        print 'KAB:', self.KAB.encode('hex')
        encrypt = AES.new(self.KAB, AES.MODE_GCM, IV_bob)
        print '====== Bob then send EKAB(Hi, it is Bob) ============='
        encryptBob = encrypt.encrypt_and_digest('Hi, it is Bob')[0]
        print 'EKAB(Hi, it is Bob):', encryptBob
        return encryptBob
    
alice = Alice("so secret key-a!")
bob = Bob("so secret key-b!")
kdc = KDC()

alice.addSharekey(kdc)
bob.addSharekey(kdc)

message_from_KDC = alice.getTickets('Bob', kdc)

alice.sendToBob_getResponce(message_from_KDC, bob)



        

