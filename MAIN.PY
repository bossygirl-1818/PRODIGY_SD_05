from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up Selenium WebDriver (adjust path to your ChromeDriver)
driver_path = 'path_to_chromedriver'  # Example: 'C:/path/to/chromedriver'
driver = webdriver.Chrome(driver_path)

# Function to scrape product data from an e-commerce site
def scrape_ecommerce_site(url):
    driver.get(url)  # Open the URL in the browser
    time.sleep(5)  # Allow time for the page to fully load

    # Get page source after JavaScript has executed
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract product details
    products = []
    for product in soup.find_all('div', class_='product'):  # Modify based on actual HTML tags
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('span', class_='product-price').text.strip()
        rating_tag = product.find('span', class_='product-rating')
        rating = rating_tag.text.strip() if rating_tag else "No rating"
        products.append({'Name': name, 'Price': price, 'Rating': rating})

    # Save product data to a CSV file
    df = pd.DataFrame(products)
    df.to_csv('products.csv', index=False)
    print(f"Scraped {len(products)} products and saved to 'products.csv'.")

# Example usage
url = 'http://example.com/products'  # Replace with the actual URL
scrape_ecommerce_site(url)

# Close the Selenium browser
driver.quit()
