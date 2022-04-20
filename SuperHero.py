import requests


def search_hero(url_token, name_hero):
    url = url_token + r'/search/'+name_hero
    response = requests.get(url).json()
    for hero in response['results']:
        if hero['name'] == name_hero:
            return name_hero, int(hero['powerstats']['intelligence'])


def max_intelligence (url_token, list_heroes):
    global name_best
    intelligence_max = 0
    for hero in list_heroes:
        name, intelligence = search_hero(url_token, hero)
        print(f"{name} - интелект {intelligence}")
        if intelligence > intelligence_max:
            intelligence_max = intelligence
            name_best = name
    return name_best


access_token = '2619421814940190'
url = 'https://superheroapi.com/api/'
url_token = url + access_token

list_heroes = ['Hulk', 'Captain America', 'Thanos']

print(f"best - {max_intelligence(url_token, list_heroes)}")