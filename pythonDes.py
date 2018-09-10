# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 19:05:01 2018

@author: Yapeng Xie 
"""

from Crypto.Cipher import DES
import binascii
#from hashlib import md5
import time

msg = input('Message...: ')
pwd = input('Password8bytes: ')

class DESCipher:
   
#    Start = time.clock()
#    for x in range(20000):
    def encrypt(pwd,msg):
            des = DES.new(pwd, DES.MODE_ECB)
            cipher_text = des.encrypt(msg)
            hex_cipher_text= binascii.hexlify(cipher_text)
            return hex_cipher_text
            
#    End= time.clock()
#    print('20000 times encrytion:',(End-Start))
    
    def decrypt(pwd,msg):
            des = DES.new(pwd, DES.MODE_ECB)
            cipher_text = des.encrypt(msg)
            enc= des.decrypt(cipher_text)
            
            return enc 
        
print('The encrypted message is:', DESCipher.encrypt(pwd,msg))
print ('The decrypted text is: ', DESCipher.decrypt(pwd,msg))
Start = time.clock()
for x in range(20000):
    DESCipher.encrypt(pwd,msg)
End= time.clock()
print('20000 times DES 64 bits encrytion:',(End-Start))
