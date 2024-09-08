import extract
import load
import transform

#import transform

def main():
    homepage = "https://books.toscrape.com"
    # Extraction des urls de base et des noms de chaque catégorie depuis la homepage
    #categories = extract.get_categories(homepage)

    #for category in categories:



    url = 'https://books.toscrape.com/catalogue/category/books/childrens_11/index.html'
    file_name = load.get_file_name(url)
    # Create the .csv file
    load.create_category_file(file_name, url)
    # Loop for scraping books detail pages from a category
    while True:
        # Scraping des urls des livres d'une category
        books = extract.get_books_from_category(url)

        # Extraction des informations des livres de la catégorie
        for book in books:
            book_detail = extract.get_book_detail(book)
            print(book_detail)
            book_detail = transform.transform_book_detail(book_detail)
            print(book_detail)
            load.load_book_detail(file_name, book_detail)

            #print(book_detail)
        #print(books)
        next_page = extract.get_next_page(url)
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