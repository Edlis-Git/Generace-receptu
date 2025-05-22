import re

# Načti suroviny ze souboru (např. jeden řádek = jedna ingredience)
with open("chybejici_ingredience.txt", "r", encoding="utf-8") as f:
    radky = f.readlines()

def vycisti_ingredienci(text):
    # Odstraň závorky a jejich obsah
    text = re.sub(r"\([^)]*\)", "", text)

    # Odstraň čárky a vše za nimi
    text = re.sub(r",.*", "", text)

    # Odstraň čísla a jednotky (např. 200 g, 1/2 hrnek, 0.75 l, 3 ks...)
    text = re.sub(r"\b\d+[.,]?\d*\b", "", text)  # čísla
    text = re.sub(r"\b(ks|g|ml|l|kg|balíček|hrnek|lžíce|lžička|špetka|kapka|kousek|plátek|dcl|cl|sklenice|porce|šťáva|kostka)\b", "", text, flags=re.IGNORECASE)

    # Rozděl na slova a odstraň přídavná jména podle koncovek
    slova = text.strip().split()
    slova = [slovo for slovo in slova if not re.search(r"(ý|á|é|í|ního|ního|ová|ové|ích|ních)$", slovo.lower())]

    # Spoj zpět
    return " ".join(slova).strip().lower()

# Zpracuj a odstraň duplicity
ocistene = []
seen = set()
for line in radky:
    ingredience = vycisti_ingredienci(line)
    if ingredience and ingredience not in seen:
        ocistene.append(ingredience)
        seen.add(ingredience)

# Ulož do souboru
with open("ocistene_ingredience.txt", "w", encoding="utf-8") as f:
    for ing in ocistene:
        f.write(ing + "\n")

print("Hotovo! Výsledek je v 'ocistene_ingredience.txt'")
