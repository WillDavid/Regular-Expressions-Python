import re

#META CARACTERES


# | -> OU
# . -> Qualquer Caractere (Com exceção da quebra de linha)
# [] conjunto de caracteres

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo 6aria.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|adultos', texto))
print(re.findall(r'João|.aria|ad...os', texto))
print(re.findall(r'[Jj]oão|Maria', texto)) #Procura J maiusculo e minusculo
print(re.findall(r'[Jj]oão|[Mmabcda]aria', texto)) #Procura J maiusculo e minusculo
print(re.findall(r'[a-zA-Z0-9]aria', texto)) #Procura J maiusculo e minus

## Flag

print(re.findall(r'[a-zA-Z0-9]aria|jOÃo', texto, flags=re.I))
