import csv
import requests
from bs4 import BeautifulSoup


# Fonction qui extrait les urls principales des categories du site
def extract_urls_of_categories(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_of_urls_of_categories = []
    list_of_names_of_categories = []
    ul_of_categories = soup.find('ul', class_='nav-list').findChild('li').findChild('ul')
    lis_of_categories = ul_of_categories.find_all('li')
    print("Extraction des urls des catégories...")
    for li in lis_of_categories:
        url_of_category = str(li.find('a').get('href'))
        name_of_category = (li.text).strip()

        ''' TO ADD IN TRANSFORM
        url_of_category = url_of_category.replace('..', '', 1)
        url_of_category_absolute = "https://books.toscrape.com/" + url_of_category
        list_of_urls_of_categories.append(url_of_category_absolute) '''
        list_of_urls_of_categories.append(url_of_category)
        list_of_names_of_categories.append(name_of_category)
        print(name_of_category)
        # création d'un dictionnaire
    print(f"{len(list_of_urls_of_categories)} urls ont été extraites")


    return list_of_urls_of_categories, list_of_names_of_categories



    # Recherche de plusieurs pages categories
def get_urls_of_a_category():
    for url in urls:
        i = 1
        base_url = category_urls.replace('index.html', '')
        current_url = (base_url + "page-" + str(i) + ".html")
        urls_of_a_category = []
        all_urls_of_pages = []
        print(base_url)

        while requests.get(current_url).status_code == 200:
            urls_of_a_category.append(current_url)
            all_urls_of_pages = all_urls_of_pages + urls_of_a_category
            i = i + 1
            current_url = (base_url + "page-" + str(i) + ".html")
        print(len(urls_of_a_category))
        return urls_of_a_category

    return  list_of_urls_of_categories 


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
    '''

# Fonction qui extrait les informations d'une page produit
def extract_information_of_a_product_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_information = []
    # récupération des informations produits
    product_url = url
    product_info_upc = soup.find('th', string='UPC').find_next_sibling('td').string
    product_title = soup.find("h1").string
    price_including_tax = soup.find('th', string='Price (incl. tax)').find_next_sibling('td').string
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next_sibling('td').string
    number_available = soup.find('th', string='Availability').find_next_sibling('td').string
    product_description = soup.find('div', id='product_description').find_next_sibling('p').string
    category = soup.find('ul', class_='breadcrumb').findChild('li').find_next_sibling('li').find_next_sibling(
        'li').findChild('a').string

    # récupération de la note
    div_product_info = soup.find('div', class_='col-sm-6 product_main')
    paragraphs_product_info = div_product_info.find_all('p')

    for p in paragraphs_product_info:
        classes = p.get('class')
        if 'One' in classes:
            rating = '1'
        elif 'Two' in classes:
            rating = '2'
        elif 'Three' in classes:
            rating = '3'
        elif 'Four' in classes:
            rating = '4'
        elif 'Five' in classes:
            rating = '5'
        else:
            continue

    # Récupération de l'url de l'image
    divs_item_active = soup.find('div', class_='carousel-inner')
    img_url = divs_item_active.find('img').get('src')
    while img_url.startswith('../'):
        img_url = img_url.replace('../', '', 1)
        img_url_absolute = "https://books.toscrape.com/" + img_url

    product_information =[product_url,product_info_upc,product_title,price_including_tax,price_excluding_tax,number_available,product_description,category,rating,img_url_absolute]
    return product_information





'''





