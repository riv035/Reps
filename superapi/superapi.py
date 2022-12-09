import requests
from operator import itemgetter

super_url = "https://akabab.github.io/superhero-api/api/all.json"
super_list = requests.get(super_url)
super_hero = ["Hulk", "Captain America", "Thanos", "A-Bomb"]
super_comparement = []


def hero_comparement(super_hero):
    for hero in super_hero:
        for super_heroes in super_list.json():
            if hero in super_heroes.values():
                super_comparement.append(
                    {"name": super_heroes["name"], "intelligence": super_heroes["powerstats"]["intelligence"]})
                smart_guy = sorted(super_comparement, key=itemgetter("intelligence"), reverse=True)
    print(f"Самый умный герой из списка {super_hero}:\n"
          f"{smart_guy[0]['name']} с показателем интеллекта {smart_guy[0]['intelligence']}")


hero_comparement(super_hero)
