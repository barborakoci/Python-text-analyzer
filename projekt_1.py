"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Kočí
email: barbora.koci@email.cz
discord: barca6493
"""
from task_template import TEXTS

uzivatel = {
            'bob': '123', 
            'ann': 'pass123',
            'mike': 'password123',
            'liz': 'pass123'
            }


if uzivatel.get(jmeno := input("Uživatelské jméno: ")) == (heslo := input("Heslo: ")):
    print(f"Ahoj {jmeno}, vítej v aplikaci! Pokračuj...")
    vyber = input("Vyber text k analýze. Zadej 1, 2 nebo 3: ")
    if vyber in ["1", "2", "3"]:
        if vyber == "1":
            text = TEXTS[0]
        elif vyber == "2":
            text = TEXTS[1]
        elif vyber == "3":
            text = TEXTS[2]
        
        upraveny_text = text.replace("\n", " ")
        rozdelena_slova = upraveny_text.split(" ")
        slova = rozdelena_slova[1:-1]
        
        vycistena_slova = []
        pocet_slov_velka = []
        pocet_slov_velke = []
        pocet_slov_mala = []
        pocet_cisel = []
        suma_cisel = []
        for slovo in slova: 
            vycistena_slova.append(slovo.strip(".,"))
        for slovo in vycistena_slova:
            if slovo.istitle():
                pocet_slov_velke.append(slovo)
            if slovo.isupper():
                pocet_slov_velka.append(slovo)
            if slovo.islower():
                pocet_slov_mala.append(slovo)
            if slovo.isdigit():
                pocet_cisel.append(int(slovo))
        
        pocet_slov = len(vycistena_slova)
        print(f"V textu je celkem {pocet_slov} slov.")
        print(f"Počet slov s velkým počátečním písmenem je: {len(pocet_slov_velke)}.")
        print(f"Počet slov velkými písmeny je: {len(pocet_slov_velka)}.")
        print(f"Počet slov malými písmeny je: {len(pocet_slov_mala)}.")
        print(f"Počet čísel je: {len(pocet_cisel)}.")
        print(f"Součet čísel v textu je: {sum(pocet_cisel)}.")
        print(pocet_slov_velke)
        print(pocet_slov_velka)
        print(pocet_slov_mala)
        print(pocet_cisel)
        print(vycistena_slova)
        delka_slov = {}

        # Zpracování délek slov
        for slovo in vycistena_slova:
            delka = len(slovo)
            if delka in delka_slov:
                delka_slov[delka] += 1
            else:
                delka_slov[delka] = 1

        # Vytisknutí histogramu
        print("D.|         VÝSKYT       |Č.")
        print("-" * 40)

        for delka, pocet in sorted(delka_slov.items()):
            vyskyty = '*' * pocet
            print(f"{delka:2}|{vyskyty:22}|{pocet}")
        
            
    else:   
        while vyber.isnumeric():
            print("Číslo není v požadovaném rozsahu.")
            break
        else:
            print("Je třeba zadat celé číslo 1-3.")
            quit()

else:
    print("Uživatel není registrován. Program bude ukončen.")
    quit()
    


    

