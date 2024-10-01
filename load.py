import csv
from datetime import datetime
import os
import requests


# Time variables
now = datetime.now()
date_of_now = now.strftime("%d_%m_%Y")
time_of_now = now.strftime("%H_%M_%S")

# Keys for the csv file
header = {
    'product_page_url': '',
    'universal_ product_code (upc)':'',
    'title':'',
    'price_including_tax':'',
    'price_excluding_tax':'',
    'number_available':'',
    'product_description':'',
    'category':'',
    'review_rating':'',
    'image_url' :'',
    }

def save_image(book_detail):
    url = requests.get(book_detail['image_url'])
    category_folder = book_detail['category']
    file_path = os.path.join(category_folder, book_detail['universal_ product_code (upc)'] + '.jpg')
    # Check is the folder exists, if not it creates it
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)
    with open(file_path, "wb") as image:
        image.write(url.content)




def create_category_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder: '{folder_name}' has been created")
    # Check if the folder already exists
    except FileExistsError:
        print(f"Folder: '{folder_name}' already exists.")
    pass


def create_books_detail_file(file_name):
    with open(file_name+'.csv', mode='w') as file:
        # Create the .csv file with headers
        fieldnames = header
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        print(file_name+" has been created")
        pass


def load_book_detail(file_name, book_detail):
    with open(file_name+'.csv', mode='a') as file:
        # Write book detail in file
        fieldnames = book_detail.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(book_detail)
        print(' - '+book_detail['title']+'has been added to: '+file_name)
        pass


