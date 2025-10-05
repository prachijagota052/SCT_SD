import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

url = "https://books.toscrape.com/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

data = []

for book in books:
    # Extract title
    title_tag = book.find('h3').find('a')
    name = title_tag['title'] if title_tag else 'N/A'

    # Extract price
    price_tag = book.find('p', class_='price_color')
    price = price_tag.text.strip() if price_tag else 'N/A'

    # Extract rating
    rating_tag = book.find('p', class_='star-rating')
    rating = rating_tag['class'][1] if rating_tag and len(rating_tag['class']) > 1 else 'N/A'

    data.append([name, price, rating])

df = pd.DataFrame(data, columns=['Name', 'Price', 'Rating'])
print(df)
df.to_csv('books.csv', index=False)
print("Data saved to books.csv")