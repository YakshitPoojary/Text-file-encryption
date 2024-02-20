# 1) Generate a symmetric key
from cryptography.fernet import Fernet

def  gen_key():
    key = Fernet.generate_key()

    # 2) Save the key into a file
    with open('SecretKey.key', 'wb') as file:
        file.write(key)

        
    