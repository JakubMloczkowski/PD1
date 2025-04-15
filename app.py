from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def moja_strona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get("name", default="")
    if name:
        return f"Hello {name}!"
    return "Hello!"

@app.route('/api/v1.0/predict')
def predict():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0)) 
        if (a+b) > 5.8:
            wynik = 1
        else:
            wynik = 0
            
        return jsonify({
            "wynik": wynik,
            "dane": {
                "num1": a,
                "num2": b }
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run()
