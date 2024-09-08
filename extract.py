import csv
import requests
from bs4 import BeautifulSoup
# TO DO set everything in en, set the transform functions,
homepage = 'https://books.toscrape.com/'


# Fonction qui extrait les urls principales des categories du site
def get_categories(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_dic_categories = []
    ul_of_categories = soup.find('ul', class_='nav-list').findChild('li').findChild('ul')
    lis_of_categories = ul_of_categories.find_all('li')
    print("Extraction des urls des catégories...")

    for li in lis_of_categories:
        url_of_category = str(li.find('a').get('href'))
        name_of_category = (li.text).strip()
        url_of_category = url_of_category.replace('..', '', 1)
        url_of_category_absolute = "https://books.toscrape.com/" + url_of_category

        current_category_dic = {"name": name_of_category, "url": [url_of_category_absolute]}
        list_dic_categories.append(current_category_dic)
        print(name_of_category)
        # création d'un dictionnaire
    print(f"{len(list_dic_categories)} urls ont été extraites")
    #print(f"Voici la liste de dictionnaires {list_dic_categories}")
    return categories



# Récupération des livres d'une page catégorie
def get_books_from_category(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.findAll('h3')
    books_urls = []
    for h3 in books:
        url_of_product = str(h3.find('a').get('href'))
        url_of_product_absolute = url_of_product.replace('../../../', 'https://books.toscrape.com/catalogue/', 1)
        books_urls.append(url_of_product_absolute)
    return books_urls

def get_next_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    base_url = url.rsplit('/', 1)[0] + '/'
    next_li = soup.find('li', class_ = 'next')
    if next_li:
        next_page = base_url + soup.find('li', class_ = 'next').findChild('a').get('href')
        return next_page

    else:
        print("Scraping terminé")









# Fonction qui extrait les urls des produits d'une page catégorie
def extract_products_urls_from_category_urls(url):
    page = requests.get(url)
    soup_category_page = BeautifulSoup(page.content, 'html.parser')
    name_of_category = soup_category_page.find('h1')
    h3s_of_books = soup_category_page.findAll('h3')
    urls_of_products_of_a_category = []
    dic_of_a_category = {}
    for h3 in h3s_of_books:
        url_of_product = str(h3.find('a').get('href'))
        url_of_product = url_of_product.replace('../../../', '', 1)
        url_of_product_absolute = 'https://books.toscrape.com/catalogue/' + url_of_product
        #print(url_of_product_absolute)
        urls_of_products_of_a_category.append(url_of_product_absolute)


    print("Liste des urls à scraper", urls_of_products_of_a_category)
    print("Nombre de produits dans la page : ", len(urls_of_products_of_a_category))

    return urls_of_products_of_a_category


# Fonction qui extrait les informations d'une page produit
def get_book_detail(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Scrape of raw rating
    rating = soup.select_one('p.star-rating').attrs



    # essayer de faire un mapping avec dic -> à mettre dans le transform


    book_detail = {
        'product_page_url': url,
        'universal_ product_code (upc)': soup.find('th', string='UPC').find_next_sibling('td').string,
        'title': soup.find("h1").string,
        'price_including_tax': soup.find('th', string='Price (incl. tax)').find_next_sibling('td').string,
        'price_excluding_tax': soup.find('th', string='Price (excl. tax)').find_next_sibling('td').string,
        'number_available': soup.find('th', string='Availability').find_next_sibling('td').string,
        'product_description': soup.find('div', id='product_description').find_next_sibling('p').string if soup.find('div', id='product_description') else None,
        'category': soup.find('ul', class_='breadcrumb').findChild('li').find_next_sibling('li').find_next_sibling(
            'li').findChild('a').string,
        'review_rating': rating,
        'image_url' : soup.find('div', class_='item active').findChild('img')["src"].replace('../', homepage, 1)
    }
    return book_detail














