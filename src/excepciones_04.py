def Ask_User():
    """Ask the user for an input

    Ask the user for an input but it cant be a float
    """
    
    try:
        number = int(input('Numero -> '))

        return number
    
    except ValueError:
        print('No has introducido un numero entero.')
        

def main():

    Ask_User()

if __name__ == "__main__":
    main()