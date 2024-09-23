

def transform_book_detail(book_detail):
    rating = book_detail['review_rating']['class'][1]
    print(rating)
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

    return book_detail







