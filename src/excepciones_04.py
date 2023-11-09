def Ask_User():
    number = None
    if type(number) == float:
        raise ValueError()
    
    try:
        number = int(input('Numero -> '))

        return number
    
    except ValueError:
        print('No has introducido un numero entero.')
        

def main():

    Ask_User()

if __name__ == "__main__":
    main()