
def transform_information_of_a_product_page(product_information):
    transformed_product_information = {}
    keys_of_product_information_dictionary = ['product_url','product_info_upc','product_title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','img_url']
    i = 0
    for x in keys_of_product_information_dictionary:
        transformed_product_information[keys_of_product_information_dictionary[i]]=product_information[i]
        i += 1

    return  transformed_product_information



