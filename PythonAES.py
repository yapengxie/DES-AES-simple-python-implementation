# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:34:27 2018

@author: frank
"""
from Crypto.Cipher import AES 
import binascii
#from hashlib import md5
import time

msg = input('Message 16bytes: ')
pwd = input('Password 16bytes: ')

class AESCipher:
   
#    Start = time.clock()
#    for x in range(20000):

    def encrypt(pwd,msg):
            aes = AES.new(pwd, AES.MODE_ECB)
            cipher_text = aes.encrypt(msg)
            hex_cipher_text= binascii.hexlify(cipher_text)
            return hex_cipher_text
            
#    End= time.clock()
#    print('20000 times encrytion:',(End-Start))
    
    def decrypt(pwd,msg):
            aes = AES.new(pwd, AES.MODE_ECB)
            cipher_text = aes.encrypt(msg)
            enc= aes.decrypt(cipher_text)
            
            return enc 
        
print('The encrypted message is:', AESCipher.encrypt(pwd,msg))
print ('The decrypted text is: ', AESCipher.decrypt(pwd,msg))
Start = time.clock()
for x in range(10000):
    AESCipher.encrypt(pwd,msg)
End= time.clock()
print('10000 times AES 128 bits encrytion:',(End-Start))
