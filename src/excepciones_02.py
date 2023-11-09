"""
Ejercicio 2.3.2

Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
def Ask_User():
    """Ask the user for an input
    """
    age = None

    while age == None:
        try:
            age = int(input('Edad -> '))

            return age
        
        except ValueError:
            print('-Número no válido-')
        

def impar(number:int) -> str:
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