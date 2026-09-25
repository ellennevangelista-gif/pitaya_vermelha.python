import os

# Defone o valor da variável
has_invitation = False
# Varaável que está uma atrelada a outra
invited = age = vip = str()

# Limpa a tela do terminal CMD
os.system("cls")

age = int(input ("Digite a idade:"))
vip = input("É vip? [Sim/Não]") 



# Testa a entrada do usuário
if vip.lower() == 'sim':
    is_vip = True
else:
    invited = input("Tem convite? [Sim/Não]:")

# Testa a entrada do usuário
if invited.lower() == 'sim':
    # Neste caso, altera o valor da variável
    has_invitation = True

#Depuração de variáveis
print ("age", type(age), age)
print ("has_ivitation", type(has_invitatiom), has_invitation)
print ("is_vip", type(is_vip), is_vip)

'''
if age >= 18 and has_invitation: 
    print("Entrada permitida") 

elif is_vip:
    print('Que bom ver você novamente')

else: 
    print("Entrada não permitida") 
'''

print ("Acabou")



