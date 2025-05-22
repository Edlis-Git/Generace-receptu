# Název vstupního souboru
vstupni_soubor = "../data.txt"

# Výstupní soubory
soubor_kategorie = "kategorie.txt"
soubor_recepty = "recepty.txt"
soubor_spoje = "recepty_ingredience.txt"

# Otevři vstupní soubor a výstupní soubory
with open(vstupni_soubor, "r", encoding="utf-8") as f:
    obsah = f.read()

# Rozdělíme celý řetězec podle středníků – každý příkaz končí středníkem
prikazy = obsah.split(";")

# Otevři výstupní soubory pro zápis
with open(soubor_kategorie, "w", encoding="utf-8") as f_kat, \
     open(soubor_recepty, "w", encoding="utf-8") as f_rec, \
     open(soubor_spoje, "w", encoding="utf-8") as f_spoj:

    for prikaz in prikazy:
        prikaz = prikaz.strip()
        if not prikaz:
            continue  # přeskočí prázdné řádky

        if "INSERT INTO Categories" in prikaz:
            f_kat.write(prikaz + ";\n")
        elif "INSERT INTO Recipes" in prikaz:
            f_rec.write(prikaz + ";\n")
        elif "INSERT INTO RecipeIngredients" in prikaz:
            f_spoj.write(prikaz + ";\n")
        else:
            print("⚠️ Neznámý řádek, ignoruji:", prikaz[:50])  # jen pro debug

print("✅ Hotovo! Vytvořeny soubory:")
print(" -", soubor_kategorie)
print(" -", soubor_recepty)
print(" -", soubor_spoje)
