import hashlib

text = b"virus"
print(hashlib.md5(text).hexdigest())