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

    match x:
        case '0':
            print('\nAcabou')
            
            # Esse break interrompe o 'while'
            break

        case '1':
            print('\nVai comer')
            
        
        case '2':
            print('\nVai dormir')
           
        
        case '3':
            print('\n Grite: CAMA!!!')
            


       # Nenhuma das opções é válidas
        case _:
            print('\nNão entendi')
    input('Tecle [Enter] para continuar.')    