def fails(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print(saturs)
    except FileNotFoundError:
        print("Failu nevar atrast vai atvērt.")

if __name__ == "__main__":
    faila_nosaukums = input("Ievadi teksta faila nosaukumu: ")
    fails(faila_nosaukums)