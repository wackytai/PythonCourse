#EXERCISE 1: Given the following code snippet, recreate the missing parts.
import datetime
from datetime import datetime

nome = 'Luiz'
sobrenome = 'Miranda'
idade = 30
ano_nascimento = datetime.now().year - idade
maior_de_idade = idade >= 18
altura_metros = 1.65

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)