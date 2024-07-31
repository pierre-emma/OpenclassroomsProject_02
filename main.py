import extract
import transform

def main():
    # Extraction des urls catégories depuis la homepage



    # Extraction des urls des produits depuis la liste d'urls de chaque catégorie


    print("yy")
    product_info = extract.extract_information_of_a_product_page('https://books.toscrape.com/catalogue/howl-and-other-poems_522/index.html')
    print(product_info)
    transformed_product_info = transform.transform_information_of_a_product_page(product_info)
    print(transformed_product_info)

if __name__ == "__main__":
    main()