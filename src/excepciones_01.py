"""
Ejercicio 2.3.1

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
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
        
def Age_Loop(age:int) -> str:
    """Show the years between 1 and the age the user introduced

    Args:
        age(int): The number that the user introduced before.
    
    Results:
        birthdays(str): The list of years between 1 and the age, separated by comma.
    """
    birthdays = ''

    for year in range(1,age+1):
        if year != age:
            year = str(year) + ','
            birthdays += year
        else: 
            birthdays += str(year)

    return birthdays

def main():
    """Call the modules
    
    """

    age = Ask_User()

    print(Age_Loop(age))
if __name__ == "__main__":
    main()