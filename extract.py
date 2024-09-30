import requests
from bs4 import BeautifulSoup

homepage = "https://books.toscrape.com"

# Extract book information from a book detail page
def get_categories(homepage):
    page = requests.get(homepage)
    soup = BeautifulSoup(page.content, 'html.parser')
    categories = soup.find('ul', class_='nav-list').findChild('li').findChild('ul').find_all('li')
    categories_urls = [li.find('a')['href'] for li in categories]
    categories_name = [li.find('a').get_text() for li in categories]
    categories_name = [name.strip() for name in categories_name]
    categories_dict =[{'name': name, 'url': url} for name, url in zip(categories_name, categories_urls)]
    print("Searching for categories...")
    for category in categories_dict:
        category['url'] = str(homepage) + '/' + category['url']


    print(f"{len(categories_dict)} categories have been found")
    return categories_dict



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
    print('Searching for next page...')
    if next_li:
        next_page = base_url + soup.find('li', class_ = 'next').findChild('a').get('href')
        return next_page

    else:
        pass


# Extract the information of a single book from book detail page
def get_book_detail(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Extract of raw rating
    rating = soup.select_one('p.star-rating').attrs

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














