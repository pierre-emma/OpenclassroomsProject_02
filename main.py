import extract
import transform

def main():
    homepage = "https://books.toscrape.com"
    # Extraction des urls de base et des noms de chaque catégorie depuis la homepage


    book_info = extract.get_book_detail("https://books.toscrape.com/catalogue/the-dovekeepers_748/index.html")
    print(book_info)
    books_urls = extract.get_books_from_category('https://books.toscrape.com/catalogue/category/books/travel_2/index.html')
    print(books_urls)




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