import requests

# Адрес сервера
API_URL = "http://127.0.0.1:5000"


# Получить список всех валют
def all_rates():
    response = requests.get(f"{API_URL}/api/currencies")
    print(response.json())


# Получить курс по коду валюты
def currency_by_code(code):
    response = requests.get(
        f"{API_URL}/api/currency/current?code={code}"
    )
    print(response.json())


# Получить историю за период
def history():
    start = input("Начальная дата: ")
    end = input("Конечная дата: ")

    response = requests.get(
        f"{API_URL}/api/currency/history?start={start}&end={end}"
    )

    print(response.json())


# Основное меню программы
while True:

    print("1 - Список валют")
    print("2 - Курс по коду")
    print("3 - История")
    print("4 - Выход")

    choice = input("> ")

    if choice == "1":
        all_rates()

    elif choice == "2":
        code = input("Введите код валюты: ")
        currency_by_code(code)

    elif choice == "3":
        history()

    elif choice == "4":
        break