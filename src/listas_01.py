
def ask_subject():
    Subjetcs = []
    subject = None

    while not subject == 'exit':
        try:  
        
            subject = input('Introduce una asignatura (exit para salir) -> ')
            
            if subject.lower() == 'exit':
                return Subjetcs
            if int(subject):
                raise ValueError
            
        
            Subjetcs.append(subject)
        
        except ValueError:
            print('No puedes introducir números')

def main():
    
    print(ask_subject())
        
if __name__ == "__main__":
    main()