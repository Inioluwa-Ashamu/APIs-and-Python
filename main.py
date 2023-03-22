import requests

topic = input('Enter your desired topic here: ')
from_date = input('Enter your start date here: ')
to_date = input('Enter your end date here:')

def get_news(language='en', api_key="9f0ea0e4736e408583c7634d39a0947b"):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n {article['title']} \nTITLE\n {article['description']}")
  return results
print(get_news())