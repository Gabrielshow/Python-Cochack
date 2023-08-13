#data compression
import zlib
s = b'witch which has which witches wist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))
print(zlib.crc32(s))