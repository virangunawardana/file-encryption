from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

def main():
  filename = input("Enter a filename: ")
  
  encFile = encrypt(filename)

  cont = input("Do you wish to decrypt a file?: ")
  if cont == 'yes':
    decrypt(encFile, filename)
  else:
    print('')

def encrypt(filename):
  with open(filename, 'rb') as original_file:
    original = original_file.read()
  
  encrypted = f.encrypt(original)

  encrypted_filename = "encrypted_" + filename 
  with open(encrypted_filename, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

  return encrypted_filename

def decrypt(encFile, filename):
  with open(encFile, 'rb') as encrypted_data:
    encData = encrypted_data.read()

  decrypted = f.decrypt(encData)

  decrypted_filename = "decrypted_" + filename 
  with open(decrypted_filename, 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

main()
