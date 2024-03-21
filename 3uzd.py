import json

def fails(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            dati = json.load(fails)
            print("Faila saturs:")
            print(dati)
    except FileNotFoundError:
        print("Failu nevara atrast vai atvērt.")
    except json.decoder.JSONDecodeError:
        print("JSON fails nav pareizi formatēts.")

if __name__ == "__main__":
    faila_nosaukums = input("Lūdzu, ievadi faila nosaukumu: ")
    fails(faila_nosaukums)