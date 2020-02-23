from django import template

register = template.Library()

from Crypto.Cipher import AES as aes
from Crypto import Random as rnd
from Crypto.Hash import SHA256 as sha
import os

KEY = bytes(os.getenv('KEY_AES'),'utf-8')
@register.filter(is_safe=True)
def encrypt(string):
    iv=rnd.new().read(aes.block_size)
    cipher = aes.new(KEY,aes.MODE_CFB,iv)
    msg = iv + cipher.encrypt(string.zfill(16))
    return msg.hex()

def decrypt(encrypted):
    encrypted = bytes(bytearray.fromhex(encrypted))
    iv=rnd.new().read(aes.block_size)
    cipher = aes.new(KEY,aes.MODE_CFB,iv)
    dec = cipher.decrypt(encrypted)
    return dec[16:].decode().lstrip('0')

@register.filter(is_safe=True)
def hasher(string):
    hashing = sha.new()
    hashing.update(bytes(string,'utf-8'))
    hashish = hashing.hexdigest()
    return hashish
{
  "datalayer": "true",
  "pageType": "blog",
  "user_enc": "466e1b9b353f51bb551754eb7f9a4cdf6dcb29ff375c3c52cc38faebf0409f7b",
  "user_hash": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
}
