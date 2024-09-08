import csv
import extract
from datetime import datetime
from bs4 import BeautifulSoup
import requests


# For testing purpose
book_detail = extract.get_book_detail('https://books.toscrape.com/catalogue/sophies-world_966/index.html')

# Time variables
now = datetime.now()
date_of_now = now.strftime("%d_%m_%Y")
time_of_now = now.strftime("%H_%M_%S")

def get_file_name(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    file_name = soup.find('h1').string + '_'+ date_of_now + '.csv'
    return file_name


def create_category_file(file_name, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    with open(file_name, mode='w') as file:
        fieldnames = book_detail.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        pass

def load_book_detail(file_name, book_detail):
    with open(file_name, mode='a') as file:
        fieldnames = book_detail.keys()
        # Write book detail in file
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(book_detail)
        pass


