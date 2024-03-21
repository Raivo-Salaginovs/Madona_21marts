def dati(fails):
    with open(fails, 'r') as f:
        for rinda in f:
           
            kolonnas = rinda.split()
           
            if len(kolonnas) >= 4:
                ceturta_kolonna = kolonnas[3]
                print(ceturta_kolonna)

if __name__ == "__main":
    fails = input("Ievadiet faila nosaukumu: ")
    dati(fails)