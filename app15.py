# Loop while

import os
os.system ('cls')


while True:
    os.system('cls')
    print('''
    1) Estou com fome
    2) Estou com sono
    3) Quero minha cama

    0) Sair
    ''')
    x= input("Escolha uma opção:")

    
    if x == '1':
        print("Vai comer")
        input ("Tecle [Enter] para continuar")
    
    elif x == '2':
        print("\nVai dormir")
        input("Tecle [Enter] para continuar")
   
    elif x == '3':
        print("\n Grite: CAMA!!!")
        input("Tecle [Enter] para continuar")

    elif x == '0':
        print("\nAcabou")
        break
    
    else:
        print("\nNão entendi")
        input("Tecle [Enter] para continuar")
    
    

    
