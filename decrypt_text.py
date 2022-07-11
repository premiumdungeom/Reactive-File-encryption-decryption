import os
import cryptography.fernet
from cryptography.fernet import Fernet
import glob

def decrypt():
  with open("key.mortkey", "rb") as key:
    key = key.read()
  
  items = []
  for files in glob.glob("myfiles/*.mortvir"):
    items.append(files)

  for restored in items:
    restore_1 = restored.replace('myfiles/', '')
    restore_2 = restore_1.replace('.mortvir', '')
    final_restore = restore_2
    print("The Files Being Restored Are", final_restore)
  
  for file in items:
    with open(file , 'rb') as thefile:
      contents = thefile.read()
    decrypted = Fernet(key).decrypt(contents)
    with open(file, 'wb') as thefile:
      thefile.write(decrypted)
    vir = '.mortvir'
    new_files = file.replace(vir, '')
    os.rename(file, new_files)
  
  print("Done, Virus is Removed \nThanks For Using The Tool")
decrypt()