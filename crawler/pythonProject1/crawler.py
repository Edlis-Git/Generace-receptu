import urllib.request
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re

base_url = "https://www.recepty.cz/recept/nakladane-rizky-11051"
data_file = "data_ingredients.txt"

def write_data(message):
    with open(data_file, "a", encoding="utf-8") as log:
        log.write(f"{message} ")

def get_soup(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_page_links(url):
    soup = get_soup(url)
    links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)]
    return links

def get_steps(url):
    soup = get_soup(url)
    step = soup.find_all("div", {"class": "cooking-process__number-cover"})
    numbers = [int(div['id'].split('-')[1]) for div in step]
    max_n = max(numbers)
    steps = []
    for i in range(1, max_n + 1):
        stringig = str(f"paragraph-{str(i)}")
        stepik = soup.find_all("div", {"id": stringig})
        steps.append(stepik[0].text.strip())
    return steps

def get_recepie_name(url):
    soup = get_soup(url)
    name = soup.find("h1", {"class": "recipe-title-box__title"}).contents[0]
    return name

def get_needed_ingredients(url):
    soup = get_soup(url)
    needed_ingredients = soup.find_all("li", {"class": "ingredient-assignment__item"})
    ingredient_list = []
    for ingredient in needed_ingredients:
        desc_div = ingredient.find("div", {"class": "ingredient-assignment__desc"})
        desc = desc_div.text.strip() if desc_div else ""
        desc = desc.replace("\n", " ").replace("  ", " ").strip()
        full_desc = f"{desc}".strip()
        full_desc = re.sub(' +', ' ', full_desc)
        ingredient_list.append(full_desc)

    return ingredient_list

def get_portions(url):#porce jsou vedle surovin, bude potřeba na správné počítání ingrediencí na jednu porci
    soup = get_soup(url)
    try:
        portion_number = soup.find("span", {"title": "Počet porcí"}).contents[0]
    except:
        portion_number = 1
    return portion_number

def get_recepie_type(url):
    soup = get_soup(url)
    category_div = soup.find("div", {"class": "recipe-categories__detail-categories"})
    if category_div:
        category = category_div.find("a").text.strip()
        return category
    return None

def display_recepie_info():
    #ingredience
    ingredients = get_needed_ingredients(base_url)
    i = 0
    for ingredient in ingredients:
        i += 1
        print(f"{i}: {ingredient}")
    #jmeno
    print(f"name: {get_recepie_name(base_url)}")
    #porce
    print(f"porce: {get_portions(base_url)}")
    #kroky
    steps = get_steps(base_url)
    i = 0
    for step in steps:
        i += 1
        print(f"step {i}: {step}")
    #typ
    print(f"category: {get_recepie_type(base_url)}")

categories = []
ingredients_array = []

def delete_quantity(ingredient):
    pattern = r"^\d+\s*(ks|stroužek|lžíce|lžičky|lžička|g|ml|kg|l)?\s*"
    return "\n".join([re.sub(pattern, "", line) for line in ingredient.split("\n")]).strip()

def delete_note(ingredient):
    pattern = r"\s*(-|…|\.{3}|\,{3}).*"
    return "\n".join([re.sub(pattern, "", line).strip() for line in ingredient.split("\n")])

def write_recipe_data(url):
    name = get_recepie_name(url)
    ingredients = get_needed_ingredients(url)
    """
    portions = get_portions(url)
    steps = get_steps(url)
    category = get_recepie_type(url)

    # Write SQL commands to insert data into the database
    
    if category not in categories:
        categories.append(category)
        write_data(f"INSERT INTO Categories (CategoryName) VALUES ('{category}');")
    write_data(
        f"INSERT INTO Recipes (RecipeName, CategoryID, Steps, Portions) VALUES ('{name}', (SELECT CategoryID FROM Categories WHERE CategoryName = '{category}'), '{' '.join(steps)}', {portions});")
    """

    for ingredient in ingredients:
        if ingredient not in ingredients_array:
            #vyčistit ingredienci od gramáže a quantity
            cleared_ingredient = delete_quantity(delete_note(ingredient))
            ingredients_array.append(cleared_ingredient)
            write_data(f"INSERT INTO Ingredients (IngredientName) VALUES ('{cleared_ingredient}');")
        write_data(
            f"INSERT INTO RecipeIngredients (RecipeID, IngredientID) VALUES ((SELECT RecipeID FROM Recipes WHERE RecipeName = '{name}'), (SELECT IngredientID FROM Ingredients WHERE IngredientName = '{ingredient}'));")
    write_data("\n")

def get_next_recepies_url(url):
    urls = get_page_links(url)
    correct_urls = []
    not_recepies = []
    for one_url in urls:
        if re.match("^https:\/\/www\.recepty\.cz\/recept\/[a-z0-9-]+-\d+$", one_url):
            correct_urls.append(one_url)
        else:
            not_recepies.append(one_url)
    return correct_urls

def crawl_recipes(start_url):
    visited_urls = set()
    urls_to_visit = [start_url]
    categories = []
    ingredients = []

    while urls_to_visit:
        current_url = urls_to_visit.pop(0)
        if current_url in visited_urls:
            continue

        print(f"Crawling: {current_url}")
        try:
            write_recipe_data(current_url)
        except:
            continue
        visited_urls.add(current_url)

        next_urls = get_next_recepies_url(current_url)
        for next_url in next_urls:
            if next_url not in visited_urls and next_url not in urls_to_visit:
                urls_to_visit.append(next_url)


crawl_recipes(base_url)
