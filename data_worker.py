import csv

DATA_FILE = 'data.csv'


def reader_data_validate():
    try:
        with open(DATA_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            headers = reader.fieldnames
            if not headers:
                raise ValueError("Неверный разделитель или пустой файл")

            rows = list(reader)
            for row in rows:
                if len(row) != len(headers):
                    raise ValueError(f"Некорректная строка: {row}")

            return rows

    except FileNotFoundError:
        print("Файл data.csv не найден.")
        raise
    except PermissionError:
        print(f"Ошибка: Нет прав для чтения файла '{DATA_FILE}'.")
        raise
    except UnicodeDecodeError:
        print(f"Ошибка: Не удалось декодировать файл '{DATA_FILE}' с указанной кодировкой.")
        raise
    except ValueError as ve:
        print(f"Ошибка в данных файла: {ve}")
        raise
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")
        raise



