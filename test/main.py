

def caesar_cipher(encrypt: bool, text: str, key: int): 
  new_text: str = ''
  
  # Encrypt.
  if encrypt: 
    for c in text: 
      new_text += chr((ord(c.upper()) + key-65) % 26 + 65)  # Shift forwards.

  # Decrypt.
  else: 
    for c in text: 
      new_text += chr((ord(c.upper()) - key-65) % 26 + 65)  # Shift backwards.
    
  return new_text


def main(): 
  print(caesar_cipher(True, 'hello', 3))
  print(caesar_cipher(False, 'khoor', 3))
  
  
if __name__ == "__main__": 
  main()