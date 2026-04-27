from flask import Flask, jsonify, request

# Создаем экземпляр Flask-приложения (сервер)
app = Flask(__name__)

# Временное хранилище данных (вместо базы данных)
# Здесь описаны валюты, их текущий курс и история изменений
CURRENCY_DATA = {
    "USD": {
        "name": "Доллар США",
        "current_rate": 92.45,
        "history": [
            {"date": "2026-04-18", "rate": 91.8},
            {"date": "2026-04-19", "rate": 92.1},
            {"date": "2026-04-20", "rate": 92.45}
        ]
    },
    "EUR": {
        "name": "Евро",
        "current_rate": 101.12,
        "history": [
            {"date": "2026-04-18", "rate": 100.5},
            {"date": "2026-04-19", "rate": 100.9},
            {"date": "2026-04-20", "rate": 101.12}
        ]
    }
}


# ENDPOINT 1: Список всех валют

@app.route('/api/currencies')
def get_all_currencies():
    # Возвращаем весь словарь с валютами в формате JSON
    return jsonify(CURRENCY_DATA)



# ENDPOINT 2: Курс валюты по её коду

@app.route('/api/currency/current')
def get_currency():
    # Получаем параметр code из URL (?code=USD)
    code = request.args.get('code', '').upper()

    # Проверяем, существует ли такая валюта
    if code not in CURRENCY_DATA:
        return jsonify({
            "success": False,
            "error": "Currency not found"
        }), 404  # ошибка "не найдено"

    # Возвращаем текущий курс валюты
    return jsonify({
        "success": True,
        "code": code,
        "rate": CURRENCY_DATA[code]["current_rate"]
    })



# ENDPOINT 3: История курсов за период

@app.route('/api/currency/history')
def history():

    # Получаем параметры start и end из URL
    start = request.args.get('start')
    end = request.args.get('end')

    result = []

    # Проходим по всем валютам
    for code, data in CURRENCY_DATA.items():

        # Проходим по истории каждой валюты
        for record in data["history"]:

            # Фильтруем записи по диапазону дат
            if start <= record["date"] <= end:
                result.append({
                    "code": code,
                    "date": record["date"],
                    "rate": record["rate"]
                })

    # Возвращаем найденные записи
    return jsonify(result)


# Точка входа в программу
if __name__ == "__main__":
    # Запуск сервера на локальном хосте и порту 5000
    app.run(port=5000)