import requests

API_URL="http://127.0.0.1:5000"


def all_rates():
    r=requests.get(f"{API_URL}/api/currencies")
    print(r.json())


def currency_by_code(code):
    r=requests.get(
      f"{API_URL}/api/currency/current?code={code}"
    )
    print(r.json())


def history():
    start=input("Начальная дата: ")
    end=input("Конечная дата: ")

    r=requests.get(
      f"{API_URL}/api/currency/history?start={start}&end={end}"
    )

    print(r.json())


while True:

    print("1 - Список валют")
    print("2 - Курс по коду")
    print("3 - История")
    print("4 - Выход")

    c=input("> ")

    if c=="1":
        all_rates()

    elif c=="2":
        code=input("Введите код валюты: ")
        currency_by_code(code)

    elif c=="3":
        history()

    elif c=="4":
        break