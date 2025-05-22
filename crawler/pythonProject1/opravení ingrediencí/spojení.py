# Pole ingrediencí v Pythonu
pole_ingredienci = [
    'acai', 'agar', 'ajvar', 'amaretto', 'ananas', 'angrešt', 'anýz', 'ančovičky',
    'aperol', 'arašídy', 'artyčoky', 'avokádo', 'badyán', 'bageta', 'baileys',
    'baklažán', 'balkánský sýr', 'balzamikový ocet', 'bambusové výhonky', 'banány',
    'batáty', 'bazalka', 'bešamel', 'borůvky', 'brambory', 'brandy', 'brokolice',
    'broskve', 'brusinky', 'bryndza', 'bulgur', 'burrata', 'bylinky', 'camembert',
    'candát', 'celer', 'celozrnná mouka', 'cherry rajčata', 'chia semínka', 'chilli',
    'chléb', 'chobotnice', 'chorizo', 'chutney', 'chřest', 'ciabatta', 'cibule',
    'citron', 'citronová tráva', 'cizrna', 'česnek', 'dýně', 'eidam', 'estragon',
    'fazole', 'feferonky', 'fíky', 'gorgonzola', 'grepfruit', 'grenadina',
    'grilovací koření', 'guacamole', 'gulášová směs', 'halušky', 'hamburger',
    'hermelín', 'hlíva ústřičná', 'hovězí maso', 'hořčice', 'hrášek', 'hummus',
    'hrušky', 'jáhly', 'jablka', 'jalapeňo', 'jogurt', 'kapary', 'kapusta',
    'kardamom', 'kari koření', 'karamel', 'karotka', 'kaviár', 'kedlubna', 'kefír',
    'kešu oříšky', 'kečup', 'kiwi', 'klobása', 'kokos', 'kokosové mléko',
    'koriandr', 'krabí maso', 'krevety', 'krůtí maso', 'křen', 'kukuřice', 'kuskus',
    'kuřecí maso', 'květák', 'kysaná smetana', 'lanýže', 'lasagne', 'limetka',
    'lilek', 'lískové ořechy', 'losos', 'majoránka', 'makrela', 'mango', 'mascarpone',
    'mandle', 'máslo', 'med', 'meloun', 'meruňky', 'mozzarella', 'mrkev',
    'mleté maso', 'muškátový oříšek', 'mušle', 'máta', 'nudle', 'oregáno',
    'oříšky', 'paprika', 'parmazán', 'pažitka', 'pečivo', 'petržel', 'pistácie',
    'pomeranč', 'rajčata', 'rýže', 'rozinky', 'rozmarýn', 'rukola', 'rum', 'ryby',
    'salát', 'sardinky', 'sezam', 'skopové maso', 'slanina', 'smetana', 'sůl',
    'šafrán', 'šampaňské', 'špagety', 'špenát', 'švestky', 'tofu', 'treska',
    'tvaroh', 'tymián', 'uzené maso', 'vanilka', 'vejce', 'vepřové maso', 'víno',
    'wasabi', 'whisky', 'zázvor', 'žampiony'
]

# Načti ingredience ze souboru (každý řádek = jedna ingredience)
with open("ocistene_ingredience.txt", "r", encoding="utf-8") as f:
    soubor_ingredience = []
    for radek in f:
        ingredience = radek.strip().lower()
        if ingredience.startswith("- "):
            ingredience = ingredience[2:]  # odstraní '- '
        if ingredience:
            soubor_ingredience.append(ingredience)

# Spoj pole a soubor, odstraň duplicity a seřaď
vsechny_ingredience = sorted(set(pole_ingredienci + soubor_ingredience))

# Zapiš do nového souboru ve formátu SQL insert
with open("ingredience_insert.txt", "w", encoding="utf-8") as f:
    for ing in vsechny_ingredience:
        f.write(f"insert into ingrediences (name) values ('{ing}');\n")

print("Hotovo! Výstup je v 'ingredience_insert.sql'")
