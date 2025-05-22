import re

# Cesty k souborům
vstupni_soubor = "../../recepty.txt"
vystupni_soubor = "konečné R.txt"

# Čtení vstupního souboru
with open(vstupni_soubor, "r", encoding="utf-8") as f:
    radky = f.readlines()

upraveny_radky = []

for radek in radky:
    # Nahrazení názvů tabulek a sloupců
    radek = re.sub(r'\bRecipeName\b', 'name', radek)
    radek = re.sub(r'\bSteps\b', 'steps', radek)
    radek = re.sub(r'\bPortions\b', 'portions', radek)
    radek = re.sub(r'\bSELECT CategoryID\b', 'SELECT id', radek)
    radek = re.sub(r'\bCategoryID\b', 'category_id', radek)
    radek = re.sub(r'\bCategories\b', 'categories', radek)
    radek = re.sub(r'\bCategoryName\b', 'name', radek)

    upraveny_radky.append(radek)

# Zápis do nového souboru
with open(vystupni_soubor, "w", encoding="utf-8") as f:
    f.writelines(upraveny_radky)

print("Hotovo! Výstupní soubor:", vystupni_soubor)
