import random
import time
import urllib
import json

from colorama import Fore, init
from data_worker import *
from proxy_checker import *
from view_response import *

init(autoreset=True)


def main():
    say_hello()

    data = reader_data_validate()
    print(f"Проверка прокси")

    checkout_list_proxy(data)

    max_delay = 0
    while True:
        for i, acc in enumerate(data, 1):
            user_data = acc['query'].split('&')[1].split('=')[1]
            user_info = urllib.parse.unquote(user_data)
            user_info = json.loads(user_info)

            username = user_info.get('username', '')
            firstname = user_info.get('first_name', 'Unknown')

            proxy = None if acc['proxy'] == '' else {'http': acc['proxy'], 'https': acc['proxy']}
            query = acc['query']

            user_visit_data = user_visit_view(query, proxy)
            if user_visit_data:
                print(f"{Fore.LIGHTBLUE_EX}\n\n===== [ {username} ({firstname}) ] =====           ", flush=True)
                flag_farm_is_finish, second_to_finish = user_info_view(query, proxy=proxy)
                if flag_farm_is_finish is None:
                    continue
                if flag_farm_is_finish:
                    farm_view(query, proxy)
                else:
                    if second_to_finish > max_delay:
                        max_delay = int(second_to_finish)
                print(f"{Fore.LIGHTBLUE_EX}{'='*40}")

        print(f"\n\n{Fore.YELLOW}{'='*40}\nСпим: {max_delay}\n{'='*40}")
        time.sleep(max_delay + random.randint(10, 100))
        max_delay = 0


def say_hello():
    print(Fore.BLUE + r"""  _____                  
 |  __ \                 
 | |__) |_ _ _ __  _   _ 
 |  ___/ _` | '_ \| | | |
 | |  | (_| | | | | |_| |
 |_|   \__,_|_| |_|\__,_|                             
""")
    print(Fore.CYAN + "Questions - https://t.me/Panunchik")
    print(Fore.CYAN + "GitHub - https://github.com/VrotNaoborot")


if __name__ == '__main__':
    main()
