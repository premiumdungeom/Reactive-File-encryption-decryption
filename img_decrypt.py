import os

import cryptography.fernet

from cryptography.fernet import Fernet




def decrypt():
  key_file = open("key_img.mortkey")
  key = key_file.read()
  os.rename('myfiles/icon.png', 'myfiles/icon.png.mortex')
  file = open('myfiles/icon.png.mortex', 'rb')
  file_1 = file.read()
  files = open('myfiles/icon.png.mortex', 'wb')
  decrypt = Fernet(key).decrypt(file_1)
  files.write(decrypt)
  os.rename('myfiles/icon.png.mortex', 'myfiles/icon.png')
  file.close()
  files.close()

decrypt()

  