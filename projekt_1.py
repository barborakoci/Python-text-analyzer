"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Kočí
email: barbora.koci@email.cz
discord: barca6493
"""
import re
from task_template import TEXTS
import sys

def analyzuj_text(text):
    upraveny_text = text.strip()
    slova = re.split(r'\s+', upraveny_text)

    vycistena_slova = []
    pocet_slov_mala = []
    pocet_cisel = []
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
    print(pocet_slov)
    print(pocet_slov_velka)
    print(pocet_slov_velke)
    print(pocet_slov_mala)
    print(pocet_cisel)

    # Vytisknutí histogramu
    print("D.|         VÝSKYT       |Č.")
    print("-" * 40)

    for delka, pocet in sorted(delka_slov.items()):
        vyskyty = '*' * pocet
        print(f"{delka:2}|{vyskyty:22}|{pocet}")


def main():
    jmeno = input("Uživatelské jméno: ")
    heslo = input("Heslo: ")

    if uzivatel.get(jmeno, "") == heslo:
        print(f"Ahoj {jmeno}, vítej v aplikaci! Pokračuj...")

        print("Dostupné texty k analýze:")
        for i, text in enumerate(TEXTS, start=1):
            print(f"{i}: {text}")

        try:
            vyber = int(input("Vyber text k analýze. Zadej číslo: "))
            if 1 <= vyber <= len(TEXTS):
                text = TEXTS[vyber - 1]
                print(f"Zvolený text: {text}")
                analyzuj_text(text)
            else:
                print("Neplatná volba. Zadej číslo dostupného textu.")
        except ValueError:
            print("Zadej číslo.")
            sys.exit(1)
    else:
        print("Uživatel není registrován. Program bude ukončen.")
        sys.exit(1)


uzivatel = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

if __name__ == "__main__":
    main()



    

