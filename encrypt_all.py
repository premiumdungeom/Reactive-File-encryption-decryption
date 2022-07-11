import os
import cryptography.fernet
from cryptography.fernet import Fernet
import glob

def encrypt():
  key = Fernet.generate_key()
  keyfile = open("key_all.mortkey", "wb")
  keyfile.write(key)
  keyfile.close()
  items = []
  encrypted_items = []
  for item in glob.glob("myfiles/*"):
    items.append(item)
  for files in items:
    new = files+".mortex"
    os.rename(files, new)
  for encrypted_files in glob.glob("myfiles/*"):
    encrypted_items.append(encrypted_files)
    print(encrypted_files)
  for file in encrypted_items:
    with open(file, 'rb') as thefile:
      contents = thefile.read()
    with open(file, 'wb') as thefile:
      encrypt = Fernet(key).encrypt(contents)
      thefile.write(encrypt)
  print("Files Encrypted Successfully")

def decrypt():
  keyfile = open("key_all.mortkey", "rb")
  key = keyfile.read()
  items = []
  for item in glob.glob('myfiles/*'):
    items.append(item)
  for file in items:
    with open(file, 'rb') as thefile:
      contents = thefile.read()
    with open(file, 'wb') as thefile:
      decrypt = Fernet(key).decrypt(contents)
      thefile.write(decrypt)
    new = file.replace('.mortex', '')
    os.rename(file, new)
  print("Files Decrypted Successfully")
  