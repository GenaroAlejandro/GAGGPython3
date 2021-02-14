import  random
import Comparador as com
valor=['pi','pa','ti']
print('Bienvenido al juego de piedra papel o tijera\nEscoge entre:\nPierdra --> 0\nPapel--> 1\nTijera --> 2\n')
de='n'
while(de!='y'):


    print('Ingresa tu valor :')
    ele = int(input())
    if((ele==0)|(ele==1)|(ele==2)):
        usuario = valor[ele]
        ran = random.randint(0, 2)
        maquina = valor[ran]
        resultado = com.PPT(usuario, maquina)
        if (resultado == 1):
            print('Ganaste!!!')

        elif (resultado == 2):
            print('Perdiste :V')

        elif (resultado == 3):
            print('Empate :O')

        else:
            print('Hubo un error')

    else:
        print('Ingreso numero invalido')

    print('Quiere salir? [y/n]:')
    de = input()


