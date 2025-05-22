import re

# Cesty k souborům
vstupni_soubor = "../recepty_ingredience_ocistene.txt"
vystupni_soubor = "konečné R_I.txt"

# Čtení vstupního souboru
with open(vstupni_soubor, "r", encoding="utf-8") as f:
    radky = f.readlines()

upraveny_radky = []

for radek in radky:
    # Nahrazení názvů tabulek a sloupců
    radek = re.sub(r'\bRecipeIngredients\b', 'RecipeIngredients', radek)
    radek = re.sub(r'\bRecipeID\b', 'recipe_id', radek)
    radek = re.sub(r'\bIngredientID\b', 'ingredience_id', radek)
    radek = re.sub(r'\bIngredients\b', 'ingrediences', radek)
    radek = re.sub(r'\bIngredientName\b', 'name', radek)
    radek = re.sub(r'\bRecipeName\b', 'name', radek)
    radek = re.sub(r'\bID\b', 'id', radek)
    radek = re.sub(r'\brecipe_id\b', 'id', radek)

    # Nahrazení SELECT klauzulí
    radek = re.sub(r'\(SELECT RecipeID FROM Recipes WHERE RecipeName = ',
                   r"(SELECT id FROM Recipes WHERE name = ", radek)
    radek = re.sub(r'\(SELECT IngredientID FROM Ingredients WHERE IngredientName = ',
                   r"(SELECT id FROM ingrediences WHERE name = ", radek)

    upraveny_radky.append(radek)

# Zápis do nového souboru
with open(vystupni_soubor, "w", encoding="utf-8") as f:
    f.writelines(upraveny_radky)

print("Hotovo! Výstupní soubor:", vystupni_soubor)
