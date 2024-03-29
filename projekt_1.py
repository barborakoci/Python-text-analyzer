"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Kočí
email: barbora.koci@email.cz
discord: barca6493
"""
from task_template import TEXTS
import re

uzivatel = {
            'bob': '123', 
            'ann': 'pass123',
            'mike': 'password123',
            'liz': 'pass123'
            }

if uzivatel.get(jmeno := input("Uživatelské jméno: ")) == (heslo := input("Heslo: ")):
    print(f"Ahoj {jmeno}, vítej v aplikaci! Pokračuj...")

    text_na_vyber = {
        "1": TEXTS[0],
        "2": TEXTS[1],
        "3": TEXTS[2]
    }

    print("Dostupné texty k analýze:")
    for varianta, text in text_na_vyber.items():
        print(f"{varianta}: {text}")

    vyber = input("Vyber text k analýze. Zadej číslo: ")

    if vyber in text_na_vyber:
        text = text_na_vyber[vyber]
        print(f"Zvolený text: {text}")
        
        upraveny_text = text.replace("\n", " ")
        rozdelena_slova = upraveny_text.split(" ")
        slova = rozdelena_slova[1:-1]
        
        vycistena_slova = []
        pocet_slov_mala = []
        pocet_cisel = []
        suma_cisel = []
        delka_slov = {}
        pocet_slov_velke = re.findall(r'\b[A-Z][a-z]*\b', text)
        pocet_slov_velka = re.findall(r'\b[A-Z]+\b', text)
        for slovo in slova:
            vycistena_slova.append(slovo.strip(".,"))
        for slovo in vycistena_slova:
            if slovo.islower():
                pocet_slov_mala.append(slovo)
            if slovo.isdigit():
                pocet_cisel.append(int(slovo))
            delka = len(slovo)
            if delka in delka_slov:
                delka_slov[delka] += 1
            else:
                delka_slov[delka] = 1

        pocet_slov = len(vycistena_slova)
        print(f"V textu je celkem {pocet_slov} slov.")
        print(f"Počet slov s velkým počátečním písmenem je: {len(pocet_slov_velke)}.")
        print(f"Počet slov velkými písmeny je: {len(pocet_slov_velka)}.")
        print(f"Počet slov malými písmeny je: {len(pocet_slov_mala)}.")
        print(f"Počet čísel je: {len(pocet_cisel)}.")
        print(f"Součet čísel v textu je: {sum(pocet_cisel)}.")

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


    

