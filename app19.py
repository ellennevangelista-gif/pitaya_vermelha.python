import os
os.system('cls')

pessoas = [
    ("Ana Carolina", "anacarol@gmail.com", "1995-10-25", "foto01.jpg"),
    ("Ana Ester", "anaester@gmail.com", "1993-07-27"),
    ("Ana Maria", "anamaria@gmail.com", "1991-07-24", "foto01.jpg"),
    ("Ana Caroline", "anacarol@gmail.com", "1998-01-16"),

]

# Data de nascimento da Ana Ester
#print (pessoas [1][2])
#print ()


for pessoa in pessoas:
     #Feio
     #print(pessoa)
    for dado in pessoa:
        print('♥', dado)
    print()

