
def fahr2cel(fahr:float) -> float:
    ''' Convertir grados Fahrenheit a grados Celsius'''
    if fahr < -459.67:
        raise ValueError('Temperatura Fahrenheit incorrecta: ' + str(fahr))

    cel = (fahr - 32.0) * 5.0 / 9.0
    return cel

if __name__ == '__main__':
    numeroCorrecto = False
    fahr = None
    while not numeroCorrecto:

            ent = input('Introduzca la Temperatura Fahrenheit:')
            fahr = float(ent)
            cel = fahr2cel(fahr)
            numeroCorrecto = True
    

    print(cel)