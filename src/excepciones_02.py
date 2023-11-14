"""
Ejercicio 2.3.2

Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
from src.excepciones_01 import Ask_User

def impar(number:int) -> str:
    """Show the odds between the number gave by the user.

    Args:
        number (int): The input of the user

    Results:

        impares (str): the string with the odd numbers. 

    Raises:
        ValueError: If the name is below 0.
    """
    if number < 0:
            raise ValueError('Introduce un numero positivo')
    
    impares = ''

    for i in range(1,number+1,2):
        if i == number or i == number-1:
            impares += str(i)

        elif i%2 != 0:
            i = str(i) + ','
            impares += i
    
            
    return impares

def main():
    try:

        number = Ask_User()

        print(impar(number))

    except ValueError:
        print('Debes introducir un numero positivo: ' + str(number))

if __name__ == "__main__":
    main()