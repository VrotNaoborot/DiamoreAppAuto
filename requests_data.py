from datetime import datetime
import json
import random

import requests
from getuseragent import UserAgent
from colorama import Fore, init

ua = UserAgent("android")
init(autoreset=True)


def user_visit(query, proxy=None):
    headers = {
        'content-length': '0',
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Token ' + query,
        'user-agent': random.choice(ua.list),
        'origin': 'https://app.diamore.co',
        'x-requested -with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://app.diamore.co/',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://diamore-propd.smart-ui.pro/user/visit'
    try:
        if proxy is None:
            response = requests.post(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, proxies=proxy)

        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"Неизвестная ошибка: {ex}")
        return None


def user_info(query, proxy=None):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Token ' + query,
        'user-agent': random.choice(ua.list),
        'origin': 'https://app.diamore.co',
        'x-requested -with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://app.diamore.co/',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://diamore-propd.smart-ui.pro/user'

    try:
        if proxy is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=proxy)

        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"Неизвестная ошибка: {ex}")
        return None


def quests(query, proxy=None):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Token ' + query,
        'user-agent': random.choice(ua.list),
        'origin': 'https://app.diamore.co',
        'x-requested -with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://app.diamore.co/',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://diamore-propd.smart-ui.pro/quests'

    try:
        if proxy is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=proxy)

        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"Неизвестная ошибка: {ex}")
        return None


def farm(query, proxy=None):
    headers = {
        'content-length': '18',
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Token ' + query,
        'user-agent': random.choice(ua.list),
        'origin': 'https://app.diamore.co',
        'x-requested -with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://app.diamore.co/',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = json.dumps({
        "tapBonuses": 498
    })
    url = 'https://diamore-propd.smart-ui.pro/user/syncClicks'
    try:
        if proxy is None:
            response = requests.post(url, headers=headers, data=data)
        else:
            response = requests.post(url, headers=headers, data=data, proxies=proxy)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"Неизвестная ошибка: {ex}")
        return None
