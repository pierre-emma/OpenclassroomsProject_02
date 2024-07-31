import csv
import requests
from bs4 import BeautifulSoup

def extract_categories_url_from_homepage(url):
    return list_of_categories_urls

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





'''def load_information_of_a_product_page():

def extract_categories_urls(url):
def transform_categories_urls(url):
def load_categories_urls(url):

def extract_products_urls_of_a_category(url):'''



