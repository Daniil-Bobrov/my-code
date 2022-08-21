import json

import requests


def get_nickname(nickname) -> str:
    post = requests.get(f"https://api.wotblitz.ru/wotb/account/list/?application_id="
                        f"&search={nickname}&limit=25")
    answer = json.loads(post.text)
    return answer["data"][0]["nickname"]


def get_account_id(nickname) -> str:
    post = requests.get(f"https://api.wotblitz.ru/wotb/account/list/?application_id="
                        f"&search={nickname}&limit=25")
    answer = json.loads(post.text)
    data = answer["data"]
    return str(data[0])


def get_statistics(account_id: str) -> dict:
    post = requests.get(f"https://api.wotblitz.ru/wotb/account/info/?application_id="
                        f"&account_id={account_id}&fields=statistics.all")
    answer = json.loads(post.text)
    return answer["data"][str(account_id)]["statistics"]["all"]


def get_tank_id(name: str) -> str:
    with open("tanks.csv", "r") as file:
        for tank in file.readlines():
            tank = tank.strip().split(",")
            if tank[0] == name:
                return tank[1]


def get_wins_percent(nickname: str) -> str:
    account_id = get_account_id(nickname)
    statistics = get_statistics(account_id)
    percent_wins = int(statistics["wins"]) / int(statistics["battles"]) * 100
    return f"{round(percent_wins, 2)}%"


def get_middle_damage(nickname: str) -> str:
    account_id = get_account_id(nickname)
    statistics = get_statistics(account_id)
    middle_damage = int(statistics["damage_dealt"]) / int(statistics["battles"])
    return str(round(middle_damage))


def get_battles(nickname: str) -> str:
    account_id = get_account_id(nickname)
    statistics = get_statistics(account_id)
    battles = statistics["battles"]
    return battles


def get_tank_info(tank_id: str, fields="") -> str:
    if type(fields) is list:
        fields = ", ".join(fields)
    post = json.loads(requests.get(
        'https://api.wotblitz.ru/wotb/encyclopedia/vehicleprofile/?application_id=8c5158437960ec83f322d4bc67815e27&'
        f'tank_id={tank_id}&fields={fields}').text)
    return post
