import hashlib

encoded_hash = "e1edf9d1967ca96767dcc2b2d6df69f4"

md5 = hashlib.md5() 
md5.update(bytes.fromhex(encoded_hash))

original_bytes = md5.digest() 

base10_int = int.from_bytes(original_bytes, byteorder='little', signed=False)

print(base10_int)
# 4613732
