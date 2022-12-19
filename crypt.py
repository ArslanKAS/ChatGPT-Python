from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# simple_key = get_random_bytes(32)
# print(simple_key)

salt = f"\xb0\xa4\xc86\xafe $kf\x9d\xd69Z\xc2JI\x10\x06j\x9e\xcc@\x9d\xef\xc6`\x8d\x86\x0f"

password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = b"Hello Secret World!"
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open("encrypted.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open("encrypted.bin", "rb") as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
key = unpad(cipher.decrypt(decrypt_data), AES.block_size)

print(key)

with open("key.bin", "wb") as f:
    f.write(key)