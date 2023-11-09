
def Ask_Password(password):
    
    saved_password = 'contraseña'

    if saved_password != password:
        raise NameError
    

def main():
    try:
        password = input('Introduce la contraseña -> ')

        Ask_Password(password)
        print('Has introducido correctamente la contraseña')
        
    except NameError:
        print('Contraseña incorrecta')

if __name__ == "__main__":
    main()