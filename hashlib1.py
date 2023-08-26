import hashlib
import base64

hash = "e1edf9d1967ca96767dcc2b2d6df69f4" 

print(hashlib.md5(bytes.fromhex(hash)).hexdigest())

encoded_hash = "e1edf9d1967ca96767dcc2b2d6df69f4"
hash_bytes = bytes.fromhex(encoded_hash)
md5_hash = hashlib.md5()
md5_hash.update(hash_bytes)
original_string = md5_hash.digest()
original_string = original_string.decode('utf-8')
print(original_string)

original_hex = md5_hash.digest().hex() 

original_b64 = base64.b64encode(md5_hash.digest())
original_string = md5_hash.digest().decode('ascii', errors='ignore')
