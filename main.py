import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://stackoverflow.com/search'
error = input('Input the error: ')

response = requests.post(url, data = error)
soup = BeautifulSoup(response.text, 'lxml')

question = soup.find_all('div', class_ = 'summary')

print (question)
