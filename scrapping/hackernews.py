import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
res1 = requests.get("https://news.ycombinator.com/news?p=2")

soup = BeautifulSoup(res.text, 'html.parser')
print(type(soup))
links = soup.select('.storylink')
subText = soup.select('.subtext')
# print(len(votes))
# print(len(links))

def sorted_stories(hnlist):
    return sorted(hnlist, key=lambda k: k['vote'], reverse=True)

def create_custom_hn(links, subText):
    hn = []
    for idx, item in enumerate(links):
        vote = subText[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100 :
                hn.append({
                    'title': item.getText(),
                    'href': item.get('href'),
                    'vote': points
                })
    return sorted_stories(hn)

# pprint.pprint(create_custom_hn(links, subText))