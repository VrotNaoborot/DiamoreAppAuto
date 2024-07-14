from requests_data import *
import pytz
from datetime import datetime, timezone


def user_visit_view(query, proxy):
    response = user_visit(query, proxy)
    if response is not None and response['message'] == "ok":
        return True
    else:
        return False


def user_info_view(query, proxy):
    """Возвращает True, если фарминг закончился"""
    response = user_info(query, proxy=proxy)
    if response is not None and 'message' not in response:
        print(f"{Fore.CYAN}[ BALANCE ] {response['balance']}")
        limit_date_str = response['limitDate']
        if limit_date_str is not None:
            try:
                # Преобразуем строку в объект datetime (предполагаем, что limitDate в UTC)
                farming_end_utc = datetime.fromisoformat(limit_date_str.rstrip('Z')).replace(tzinfo=timezone.utc)

                moscow_tz = pytz.timezone('Europe/Moscow')
                farming_end_msk = farming_end_utc.astimezone(moscow_tz)

                current_time_msk = datetime.now(moscow_tz)

                if farming_end_msk <= current_time_msk:
                    print(f"{Fore.CYAN}[ FARM ] Фарминг закончился...")
                    return True, 0
                else:
                    print(f"{Fore.CYAN}[ FARM ] Фарминг еще не закончился...")
                    return False, (farming_end_msk - current_time_msk).total_seconds()
            except ValueError as e:
                print(f"{Fore.RED}[ ERROR ] Не удалось преобразовать в datetime: {e}")
                raise
        else:
            return False, 0
    else:
        print(f"{Fore.RED}[ ERROR ] Не удалось получить ответ: {response}")
        return None, 0


def farm_view(query, proxy):
    response = farm(query, proxy)
    if response is not None:
        if response['message'] == 'Bonuses incremented':
            print(f"{Fore.CYAN}[ FARM ] 498 токенов получено")
        else:
            print(f"{Fore.CYAN}[ FARM ] Токены не были получены. {response}")
    else:
        print(f"{Fore.CYAN}[ FARM ] Токены не были получены. {response}")
