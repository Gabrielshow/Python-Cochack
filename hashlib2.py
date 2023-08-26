import hashlib

encoded_hash = "4194eb91842c8e7e6df099ca73c38f28"

hash_bytes = bytes.fromhex(encoded_hash) 

md5 = hashlib.md5()
md5.update(hash_bytes)

original_bytes = md5.digest()

base10_num = int.from_bytes(original_bytes, byteorder='big') 

print(base10_num)
