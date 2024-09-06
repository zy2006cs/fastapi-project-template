from typing import List
import hashlib,base64
def create_md5(text):
    md5=hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
def create_sha256(text):
    sha256=hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()
def b64_encode(text):
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")
def b64_decode(text):
    return base64.b64decode(text).decode('utf-8')
def hex_encode(text:str):
    return text.encode('utf-8').hex()
def hex_decode(text:str):
    return bytes.fromhex(text).decode('utf-8')
def rc4(key: str, text: str) -> List:
    key=key.encode('utf-8')
    data=text.encode('utf-8')
    S = list(range(256))
    j = 0
    out = []
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(char ^ S[(S[i] + S[j]) % 256])
    out=bytes(out)
    return out.decode('utf-8')

