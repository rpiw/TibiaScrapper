import re
from datetime import datetime
from typing import Tuple, List

from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Player:
    vocations = ("Elite Knight", "Knight", "Elder Druid", "Druid",
                 "Royal Paladin", "Paladin", "Master Sorcerer", "Sorcerer",
                 "None")

    def __init__(self, name, vocation=None, level=0, world=""):
        # game data
        self.name = name
        self.vocation = vocation
        self.level = level

        self.sex = "Male"
        self.title = None
        self.achievement_points = 0
        self.world = world
        self.residence = "Thais"
        self.last_login = datetime.min
        self.online = False

        self.account_created = datetime.min
        self.account_title = ""

        self.other_characters = []

        # metadata
        self.last_update = None


class World:
    worlds = "https://www.tibia.com/community/?subtopic=worlds"
    worlds_html_class_name = ("Odd", "Even")  # capitalization does matter!
    worlds_tag = "tr"
    worlds_continents = ("South America", "North America", "Europe")
    world_url = "https://www.tibia.com/community/?subtopic=worlds&world="

    _session = None

    def __init__(self, name):
        self.name = name
        self.ok = True
        self.players_list: List[Player] = []

        # keep types explicit - in future we migrate to Django
        self.status: bool = False
        self.players_online: int = 0
        self.online_record: Tuple[int, datetime] = (0, datetime.now())
        self.creation_date: datetime = datetime(2020, 1, 1)
        self.location: str = ""
        self.pvp_type: str = ""
        self.transfer_type: str = ""
        self.world_quest_titles: str = ""
        self.battle_eye_status: str = ""
        self.game_world_type: str = ""

        self._data = None  # prototype, Im lazy, sorry

    @staticmethod
    def get_worlds_list():
        session = HTMLSession()
        response = session.get(World.worlds)
        if not response.ok:
            print(f"Response is not ok: {response}")
            return None
        print("Response is ok.")
        print("Begin to parse html...")
        text = response.text
        soup = BeautifulSoup(text, features='lxml')

        results = []
        for odd in World.worlds_html_class_name:
            tables = soup.find_all(World.worlds_tag, attrs={"class": re.compile(odd)})
            for table in tables:
                href, text = table.a, table.text
                # text structure follows the order: world name, online players, continent, pvp rules
                split = re.search(r'\d+', text)
                if split:
                    name = text[:split.start()]
                    results.append(name)
                else:
                    continue

        results.sort()
        return results

    def scrap_world_data(self):
        if not World._session:
            World._session = HTMLSession()
        url = World.world_url + self.name
        response = World._session.get(url)

        if not response.ok:
            self.ok = False
            return

        print(f"Working on {self.name}.")
        soup = BeautifulSoup(response.text, features='lxml')
        # meta data
        table1 = soup.find_all("table", attrs={"class": re.compile("Table1")})[1]

        html_tag = "td"
        tables = table1.find_all(html_tag)[1:]
        self._data = dict((tables[i].text, tables[i + 1].text.replace(u'\xa0', ' ')) for i in range(0, len(tables), 2))

        # players list
        tables = []
        for odd_even in World.worlds_html_class_name:  # the same applies to players as well
            tables.extend(soup.find_all(World.worlds_tag, attrs={"class": re.compile(odd_even)}))

        for table in tables:
            level_re = re.search(r'\d+', table.text)  # name: str, level: int, vocation: str
            name = table.text[:level_re.start()]
            vocation = table.text[level_re.end():]
            level = table.text[level_re.start():level_re.end()]

            player = Player(name, vocation, level, self.name)
            self.players_list.append(player)


if __name__ == '__main__':
    worlds_list = World.get_worlds_list()
    for w in enumerate(worlds_list):
        print((w), ",", end="")
    # worlds = []
    # for world in worlds_list:
    #     worlds.append(World(world))
    # for w in worlds:
    #     w.scrap_world_data()
