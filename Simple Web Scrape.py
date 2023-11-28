# This is used to pull down basic information about a webpage
# Make sure to install the beautifulsoup and requests libraries before running using the following syntax: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information from the webpage
        # For example, let's extract all the links on the page
        links = soup.find_all('a')
        
        for link in links:
            print(link.get('href'))

    else:
        print(f"Error: Failed to retrieve content. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace this URL with the target webpage URL
    target_url = "https://example.com"

    # Call the function to scrape the webpage
    scrape_webpage(target_url)
