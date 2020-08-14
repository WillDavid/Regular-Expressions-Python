import re

# findall
# search
# sub
# compile



string = 'Este é um teste de expressões teste regulares.'

print(re.search(r'teste', string))  #Só procura 1
print(re.findall(r'teste', string)) #Procura todas
print(re.sub(r'teste', 'ABCD', string)) #Substitui
print(re.sub(r'teste', 'ABCD', string, count=1))  #Substitui apenas no count

rege = re.compile(r'teste')
print(rege.search(string))
print(rege.findall(string))
print(rege.sub('DEF', string))
