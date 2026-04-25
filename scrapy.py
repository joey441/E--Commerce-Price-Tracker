import requests
from bs4 import BeautifulSoup   
from urllib.parse import urljoin #for pagination scraping
import re #for regex
from datetime import datetime #for timestamping
import os
from save import save_to_tracker
import time

#getting input from the user
user_provided_url = input("Enter the URL of the website you want to scrape: ").strip()
if not user_provided_url.startswith(("http://","https://")):
    user_provided_url = "http://" + user_provided_url
#create a function to scrape the website
def scrape_website(start_url):
    headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Referer": "https://google.com"
}
    current_page=start_url
    while current_page:
        try:
            response = requests.get(current_page, headers=headers, timeout=10)  # Set a timeout for the request
            response.raise_for_status()  # Check if the request was successful
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop if there's an error
       
        soup = BeautifulSoup(response.text, 'lxml')# Parsing the HTML content using BeautifulSoup
        #selectors for scraping
        title=soup.find(string=re.compile('title',re.IGNORECASE))
        price=soup.find(string=re.compile('price',re.IGNORECASE))
        availability=soup.find(string=re.compile('availability',re.IGNORECASE))

        product_data= {
            'timestamp':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'product_name': title.text.strip() if title else 'N/A',
            'price': price.text.strip() if price else 'N/A',
            'availability': availability.text.strip() if availability else 'N/A',

    }
        save_to_tracker(product_data)
            #returning the scraped data
        next_button = soup.find('a', string=re.compile('next', re.IGNORECASE))
        if next_button and 'href' in next_button.attrs:
            current_page = urljoin(current_page, next_button['href'])
            time.sleep(2)  # Sleep for 2 seconds before the next request
        else:
            url = None  # No more pages to scrape
            current_page = None
if __name__ == "__main__":
    scrape_website(user_provided_url)
   
        
        
    
    

    
