def transform_book_detail(book_detail):
    # Transform rating data
    rating = book_detail['review_rating']['class'][1]
    if 'One' in rating:
        book_detail['review_rating'] = '1'
    elif 'Two' in rating:
        book_detail['review_rating'] = '2'
    elif 'Three' in rating:
        book_detail['review_rating'] = '3'
    elif 'Four' in rating:
        book_detail['review_rating'] = '4'
    elif 'Five' in rating:
        book_detail['review_rating'] = '5'
    # Transform Prices
    book_detail['price_including_tax'] = book_detail['price_including_tax'].replace('£','')
    book_detail['price_excluding_tax'] = book_detail['price_excluding_tax'].replace('£','')
    # Transform stock quantity
    book_detail['number_available'] = ''.join([char for char in book_detail['number_available'] if char.isdigit()])
    # Transform image url
    book_detail['image_url'] = book_detail['image_url'].replace('..','.')


    return book_detail



def transform_url(url):
    base_url = 'https://books.toscrape.com/catalogue/'
    url_absolute = base_url + url.replace("../../../", "")
    return url_absolute





