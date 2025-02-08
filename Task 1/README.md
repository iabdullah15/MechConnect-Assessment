# Product Scraper

This repository contains a Python-based web scraper that extracts product information from the website [pakmotors.pk](https://pakmotors.pk/modifications-accessories/) and saves the data into a CSV file. The scraper respects the site's `robots.txt` policy and handles pagination to scrape multiple pages.

## Environment Setup

You can set up the Python environment using either `venv` or `pipenv`. Follow one of the methods below.

### Using `venv`

1. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

### Using `pipenv`

1. **Install pipenv (if not already installed):**

   ```bash
   pip install pipenv
   ```

2. **Create and Activate a New Pipenv Environment**

   ```bash
   pipenv shell
   ```

3. **Install Dependencies**

   ```bash
   pipenv install -r requirements.txt
   ```

## Code Overview

The scraper performs the following tasks:

1. **Robots.txt Check**  
   The `can_fetch()` function reads the site's `robots.txt` file to verify whether the given URL is allowed to be scraped with the specified user-agent.

2. **Pagination Loop**  
   The script starts from the provided URL and uses the `requests` library to fetch page content. It uses BeautifulSoup to parse the HTML and locate all product elements. It also looks for a "next page" link (an `<a>` element with `rel="next"`) to continue scraping until there are no more pages.

3. **Product Data Extraction**  
   The `parse_product()` function processes each product element (identified by the class `porto-tb-item`) and extracts useful information such as:

   - **Title & Product URL:** Retrieved from the product title element.
   - **Categories:** Extracted from a meta element containing category links.
   - **Discount:** If available, the discount label is extracted.
   - **Prices:** The current price (from an `<ins>` element) and the original price (from a `<del>` element) are extracted.
   - **Rating:** If provided, the rating is extracted.
   - **Image URL:** Retrieved from the product's featured image.

4. **CSV Output**  
   Once all pages are scraped, the collected product data is saved to a CSV file (`products.csv`), with each product's details written as a row.

5. **Delay**  
   A short delay (2 seconds) is added between page requests to be respectful of the server load as a good practice.

## How to Run the Scraper

After setting up your environment and installing dependencies, run the scraper with:

```bash
python scraper.py
```

The scraper will process the pages, extract product data, and output a CSV file named `products.csv` in the project directory.
