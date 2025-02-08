import requests
from bs4 import BeautifulSoup
import urllib.robotparser
import urllib.parse
import time
import csv


def can_fetch(url, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"):
    """
    Checks the robots.txt file for the domain of the given URL to determine
    if our scraper is allowed to fetch and get data from the URL.
    """
    parsed_url = urllib.parse.urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        
    except Exception as e:
        print(f"Error reading robots.txt from {robots_url}: {e}")
        return False

    return rp.can_fetch(user_agent, url)


def find_next_page(soup, base_url):
    """
    Finds the <a> element with rel="next" that has the next page link.
    Returns the full URL for the next page if found, otherwise None.
    """
    next_link = soup.find('a', {"rel": "next"})
    
    if next_link and next_link.get('href'):
        return urllib.parse.urljoin(base_url, next_link['href'])
    
    return None


def parse_product(product):
    """
    Extracts useful information from a product element.
    Returns the product data as a dictionary
    """
    # Title and product URL
    title_element = product.find("h3", class_="porto-heading")
    
    if title_element:
        a_tag = title_element.find("a")
        title = a_tag.get_text(strip=True) if a_tag else None
        product_url = a_tag.get("href") if a_tag else None
        
    else:
        title, product_url = None, None

    # Categories
    cat_element = product.find("span", class_="porto-tb-meta")
    
    if cat_element:
        category_links = cat_element.find_all("a")
        categories = ", ".join(link.get_text(strip=True)
                               for link in category_links)
        
    else:
        categories = None

    # Discount (if any)
    discount_element = product.find("div", class_="onsale")
    discount = discount_element.get_text(
        strip=True) if discount_element else None

    # Prices: current price (inside <ins>) and original price (inside <del>)
    price_div = product.find("div", class_="tb-woo-price")
    
    if price_div:
        ins_element = price_div.find("ins")
        current_price = ins_element.get_text(
            strip=True) if ins_element else None
        del_element = price_div.find("del")
        original_price = del_element.get_text(
            strip=True) if del_element else None
        
    else:
        current_price, original_price = None, None

    # Rating (if available)
    rating_div = product.find("div", class_="star-rating")
    if rating_div:
        rating_span = rating_div.find("span")
        rating = rating_span.get_text(strip=True) if rating_span else None
        
    else:
        rating = None

    # Image URL from the featured image <img>
    image_link = product.find("a", {"aria-label": "post featured image"})
    
    if image_link:
        img_tag = image_link.find("img")
        image_url = img_tag.get("src") if img_tag else None
        
    else:
        image_url = None

    return {
        "title": title,
        "product_url": product_url,
        "categories": categories,
        "discount": discount,
        "current_price": current_price,
        "original_price": original_price,
        "rating": rating,
        "image_url": image_url
    }


def main():
    # Define the starting URL
    url = "https://pakmotors.pk/modifications-accessories/"

    # realistic browser user-agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }

    # Check robots.txt before starting
    if not can_fetch(url, user_agent):
        print(f"Scraping the page {url} is disallowed by robots.txt.")
        return
    
    else:
        print("Robots.txt check passed: We can scrape this page.")

    current_url = url
    page_count = 1
    all_products = []

    # Loop through pages until no next page is found
    while current_url:
        
        print(f"\nFetching page {page_count}: {current_url}")
        
        try:
            response = requests.get(current_url, headers=headers)
            response.raise_for_status()  # Raise an error if the request failed
            
        except Exception as e:
            print(f"An error occurred while trying to access the page: {e}")
            break

        # Parse the page with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all product elements
        products = soup.find_all("div", class_="porto-tb-item")
        print(f"Found {len(products)} products on page {page_count}.")

        # Extract data for each product
        for product in products:
            data = parse_product(product)
            all_products.append(data)

        # Find the next page URL
        next_page = find_next_page(soup, current_url)
        if next_page:
            print("Next page URL:", next_page)
        else:
            print("No more pages found.")

        # Prepare for the next iteration
        current_url = next_page
        page_count += 1

        # 2 second delay between requests
        time.sleep(2)

    # Save the collected data to a CSV file
    csv_filename = "products.csv"
    fieldnames = ["title", "product_url", "categories", "discount",
                  "current_price", "original_price", "rating", "image_url"]
    try:
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in all_products:
                writer.writerow(item)
                
        print(f"\nSaved {len(all_products)} products to {csv_filename}.")
        
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")


if __name__ == "__main__":
    main()
