"""
Ejercicio 2.3.3

Escribir un programa que pida al usuario un número 
entero positivo y muestre por pantalla la cuenta atrás 
desde ese número hasta cero separados por comas. 
Deberá solicitar el número hasta introducir uno correcto. 
"""

from src.excepciones_01 import Ask_User

def Count(number:int) -> str:
    if number < 0:
            raise ValueError()
    
    lista = ''

    for i in range(number,-1,-1):
        if i != 0:
            i = str(i) + ','
            lista += i
        else: 
            lista += str(i)

    return lista
    
        

def main():
    try:

        number = Ask_User()

        print(Count(number))

    except ValueError:
        print('Debes introducir un numero positivo: ' + str(number))

if __name__ == "__main__":
    main()