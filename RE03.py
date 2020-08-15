import re

#META CARACTERES

# * 0 ou n vezes
# + 1 ou n vezes
# ? 0 ou 1
# { } = pode ser {n} ou {min, max}

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


## Flag

print(re.findall(r'jo+Ão+', texto, flags=re.I))
print(re.sub(r'jo+Ão+','Felipe',texto, flags=re.I))
