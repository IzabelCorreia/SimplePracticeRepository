# gerador de senhar aleatórias 

import random
import string

password = ""

def altSenha( size = 8):
    charactere = string.ascii_letters + string.digits + string.punctuation
    for digito in range(size):
        aleatorio = random.choice(charactere)
    password += aleatorio


print("-" * 20)
print(altSenha)
print("-" * 20)

