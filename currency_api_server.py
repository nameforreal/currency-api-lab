from flask import Flask, jsonify, request

app = Flask(__name__)

CURRENCY_DATA = {
    "USD": {
        "name":"Доллар США",
        "current_rate":92.45,
        "history":[
            {"date":"2026-04-18","rate":91.8},
            {"date":"2026-04-19","rate":92.1},
            {"date":"2026-04-20","rate":92.45}
        ]
    },

    "EUR":{
        "name":"Евро",
        "current_rate":101.12,
        "history":[
            {"date":"2026-04-18","rate":100.5},
            {"date":"2026-04-19","rate":100.9},
            {"date":"2026-04-20","rate":101.12}
        ]
    }
}


# ЗАДАНИЕ 1
@app.route('/api/currencies')
def get_all_currencies():
    return jsonify(CURRENCY_DATA)


# ЗАДАНИЕ 2
@app.route('/api/currency/current')
def get_currency():

    code=request.args.get('code','').upper()

    if code not in CURRENCY_DATA:
        return jsonify({
            "success":False,
            "error":"Currency not found"
        }),404

    return jsonify({
        "success":True,
        "code":code,
        "rate":CURRENCY_DATA[code]["current_rate"]
    })


# ЗАДАНИЕ 3
@app.route('/api/currency/history')
def history():

    start=request.args.get('start')
    end=request.args.get('end')

    result=[]

    for code,data in CURRENCY_DATA.items():
        for record in data["history"]:
            if start <= record["date"] <= end:
                result.append({
                    "code":code,
                    "date":record["date"],
                    "rate":record["rate"]
                })

    return jsonify(result)


if __name__=="__main__":
    app.run(port=5000)