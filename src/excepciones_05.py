
def Ask_Password(password):
    """If the user password is different from as the one saved, raise NameError

    Args:
        password (str): The password introduced by the user.

    Raises:
        NameError: If the password and the saved one are not the same. 
    """
    
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