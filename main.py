import extract
import load
import transform
from datetime import datetime


now = datetime.now()
date_of_now = now.strftime("%d_%m_%Y")
time_of_now = now.strftime("%H_%M_%S")
#import transform
homepage = "https://books.toscrape.com"
def main():
    # Extract categories with a dictionary containing keys: 'name' and 'url'
    categories = extract.get_categories(homepage)
    # Loop to extract books from a category url
    for category in categories:

        # Create the .csv file
        #load.create_category_file(file_name, url)
        # Loop for scraping books detail pages from a category
        while True:
            # Scraping des urls des livres d'une category
            print(category['url'])
            books = extract.get_books_from_category(category['url'])


            # Extraction des informations des livres de la catégorie
            for book in books:
                file_name = category['name'] + date_of_now
                book_detail = extract.get_book_detail(book)
                #print(book_detail)
                book_detail_transformed = transform.transform_book_detail(book_detail)
                #print(book_detail)
                load.load_book_detail(file_name, book_detail_transformed)

                #print(book_detail)
            #print(books)
            next_page = extract.get_next_page(category['url'])
            url = next_page
            if not url:
                break
            else:
                continue












    # Extraction de toutes les pages de chaque catégorie s'il y en a plusieurs
    #for category in list_of_urls_of_categories:












    # Extraction des urls produits de chaque catégorie
    '''for url in list_of_urls_of_categories:
        extract.extract_products_urls_from_category_urls(url)'''



'''
    # Extraction des urls des produits depuis la liste d'urls de chaque catégorie

    # Extraction des informations des produits de chaque catégories

    print("yy")
    product_info = extract.extract_information_of_a_product_page('https://books.toscrape.com/catalogue/howl-and-other-poems_522/index.html')
    print(product_info)
    transformed_product_info = transform.transform_information_of_a_product_page(product_info)
    print(transformed_product_info)
'''
if __name__ == "__main__":
    main()