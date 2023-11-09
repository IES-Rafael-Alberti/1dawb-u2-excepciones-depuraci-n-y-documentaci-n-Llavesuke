
a = [8,3,1,19,14]

def algoritmo():
    total = len((a))


    for i in range (1,total):
        for j in range(0,total-i):
            if a[j] > a[j+1]:
                exchange = a[j]
                a[j] = a[j+1]
                a[j+1] = exchange
                print(a)
        

def main():
    algoritmo()

if __name__ == "__main__":
    main()