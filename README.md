
# ETL Scraping Program (Beta Version)

## Description
This project is a scraping program designed to extract, transform, and load data from the website [Books to Scrape](https://books.toscrape.com). It was developed as part of a price monitoring system for competitor websites.

### Beta Version
> **Note:** This program is in beta version and only works with the `Books to Scrape` website.

## Project Objective
The program retrieves book information from the site, such as:

- **Title**
- **Price**
- **Availability**
- **Category**
- **Description**
- **Image**
- **Rating (number of stars)**
- **UPC**
- **Ex-VAT Price**
- **Price (Incl. VAT)**

## Installation
1. **Clone the repository:**
   ```bash
   git clone git@github.com:pierre-emma/OpenclassroomsProject_02.git
   or from https://github.com/pierre-emma/OpenclassroomsProject_02
   cd OpenclassroomsProject_02
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   # On Windows
   .\env\Scriptsctivate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Program
Run the `main.py` file:

```bash
python main.py
```

## How It Works
The program follows these steps:

1. **Extraction (`extract.py`)**: Retrieve book data.
2. **Transformation (`transform.py`)**: Format and clean the data.
3. **Loading (`load.py`)**: Save the data into a .csv file and store the images.

## Contributor
- Pierre-Emma
