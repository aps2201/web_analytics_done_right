from django import template

register = template.Library()

from Crypto.Cipher import AES as aes
from Crypto import Random as rnd
from Crypto.Hash import SHA256 as sha
from wadr.settings import KEY

#KEY = bytes(os.getenv('KEY_AES'),'utf-8')
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
