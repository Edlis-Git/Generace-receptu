import re

# Seznam běžných koncovek přídavných jmen
ADJECTIVE_SUFFIXES = [
    r'ý\b', r'á\b', r'é\b', r'í\b', r'ého\b', r'ní\b', r'ních\b', r'ních\b',
    r'ová\b', r'ové\b', r'ovým\b', r'ého\b', r'ním\b', r'ná\b', r'ný\b', r'ná\b'
]


def remove_adjectives(ingredient):
    """ Odstraní přídavná jména na základě koncovek """
    for suffix in ADJECTIVE_SUFFIXES:
        ingredient = re.sub(suffix, '', ingredient, flags=re.IGNORECASE)
    return ingredient.strip()


def clean_ingredient_names(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        ingredients = file.readlines()

    cleaned_ingredients = set()

    for ingredient in ingredients:
        ingredient = ingredient.strip().lower()  # Převedení na malá písmena
        ingredient = re.sub(r'\b\d+([.,]?\d+)?\s*(g|kg|ml|l|ks|špetka|hlávka|hrnek|lžíce|lžička|kousek|kapka)\b', '',
                            ingredient, flags=re.IGNORECASE)
        ingredient = re.sub(r'[^a-zA-Zěščřžýáíéůúóďťň ]+', '', ingredient)  # Odstranění zvláštních znaků
        ingredient = re.sub(r'\s+', ' ', ingredient).strip()  # Odstranění přebytečných mezer

        # Pouze první slovo (např. "kapusta" místo "kapusta středně velká")
        first_word = ingredient.split()[0] if ingredient else ""

        # Odstranění přídavných jmen
        first_word = remove_adjectives(first_word)

        if first_word:
            cleaned_ingredients.add(first_word)

    # Výpis počtu unikátních ingrediencí
    print(f"Počet unikátních ingrediencí po čištění: {len(cleaned_ingredients)}")

    # Uložení do souboru
    with open(output_file, 'w', encoding='utf-8') as file:
        for ingredient in sorted(cleaned_ingredients):
            file.write(ingredient + '\n')

    print(f"Vyčištěný seznam ingrediencí byl uložen do {output_file}")


# Použití
clean_ingredient_names('clean_ingredients.txt', 'final_ingredients.txt')
