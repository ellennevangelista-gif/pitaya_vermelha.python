# Dicionário
import os
os.system('cls')

pessoas = {
    'p1': {'nome': 'Priscila', 'idade':30, 'conceito':'A'},
    'p2': {'nome': 'Camille', 'idade':26, 'conceito':'B'},
    'p3': {'nome': 'Pedro', 'idade':22, 'conceito':'A'},
    'p4': {'nome': 'Geovanne', 'idade':29, 'conceito':'C'}
}

print(pessoas)

pessoas ['p3']['idade'] = 32
print()
print(pessoas)

del pessoas ['p2']
print()
print (pessoas)




"""
contador = 1

for pessoa in pessoas:
    print(
        f'''
    {contador}) {pessoa ['nome']}:\n
    \t • Idade:{pessoa['idade']}
    \t • Conceito: {pessoa ['conceito']}
           '''
    )   
    contador = contador + 1 
"""
