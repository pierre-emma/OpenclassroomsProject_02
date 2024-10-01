import extract
import load
import transform
from datetime import datetime

# Values
now = datetime.now()
date_of_now = now.strftime("%d_%m_%Y")
time_of_now = now.strftime("%H_%M_%S")
homepage = "https://books.toscrape.com"


def main():
    # Extract categories with a dictionary containing keys: 'name' and 'url'
    categories = extract.get_categories(homepage)
    # Loop to extract all books from a category

    for category in categories:
        # Loop for scraping books detail urls from a category
        url = category['url']
        load.create_category_folder(category['name'])
        load.create_books_detail_file(category['name']+'_'+ date_of_now)

        while True:

            # Scraping books url from category pages
            print('Scraping of: ' +(url))
            books = extract.get_books_from_category(url)
            print(len(books), 'book(s) found')
            # Loop to extract all book detail pages present in a category
            for book in books:
                file_name = category['name'] + '_' + date_of_now
                book_detail = extract.get_book_detail(book)
                # Transform raw data into readable format
                book_detail_transformed = transform.transform_book_detail(book_detail)
                # Write the book to the .csv file
                load.load_book_detail(file_name, book_detail_transformed)
                # Save book's image
                load.save_image(book_detail)
            # Retrieve the next page url
            next_page = extract.get_next_page(url)
            if next_page:
                print('page found: ', next_page)
                url = next_page
                pass
            else:
                print('No next page')
                break









if __name__ == "__main__":
    main()