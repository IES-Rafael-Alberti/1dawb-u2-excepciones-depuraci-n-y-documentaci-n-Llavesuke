
a = [8,3,1,19,14]

def algoritmo():
    """Order a list from lower to higher.
    
    Returns:
        a (list[int]): The new list with the new order.
    """
    total = len((a))


    for i in range (1,total):
        for j in range(0,total-i):
            if a[j] > a[j+1]:
                exchange = a[j]
                a[j] = a[j+1]
                a[j+1] = exchange

    return a
        

def main():
    print(algoritmo())

if __name__ == "__main__":
    main()