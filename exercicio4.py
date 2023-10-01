import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/"

search_word = "syntax"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

occurrences = soup.body.text.lower().count(search_word.lower())

print(f"The word '{search_word}' appears {occurrences} times on the webpage.")