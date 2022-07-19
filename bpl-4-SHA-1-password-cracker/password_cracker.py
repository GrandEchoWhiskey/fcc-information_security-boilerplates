import hashlib

def crack_sha1_hash(hash, use_salts=False):
  
  p_file = open("top-10000-passwords.txt", 'r')
  passwords = [p.strip() for p in p_file]
  p_file.close()
  
  salts = ['']
  if use_salts:
    s_file = open("known-salts.txt", 'r')
    salts = [s.strip() for s in s_file]
    s_file.close()
    
  for password in passwords:
    for salt in salts:
      for guess in [password + salt, salt + password]:
        
        if hashlib.sha1(guess.encode()).hexdigest() == hash:
          return password
          
  return "PASSWORD NOT IN DATABASE"