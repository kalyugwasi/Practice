def encrypt(word: str, key: int):
    return "".join(chr(ord(ch) ^ key) for ch in word)
msg = "Hello World"
key = 78
print(msg)
cipher = encrypt(msg, key)
print(cipher)
des = encrypt(cipher,key)
print(des)
