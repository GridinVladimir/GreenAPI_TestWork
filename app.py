from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getSettings', methods=['POST'])
def getSettings():
    idInstance = request.form['idInstance']
    apiTokenInstance = request.form['apiTokenInstance']
    
    url = f"https://api.green-api.com/waInstance{idInstance}/getSettings/{apiTokenInstance}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Ошибка: неверный idInstance или apiTokenInstance."})
    else:
        return jsonify({"response": response.text})

@app.route('/getStateInstance', methods=['POST'])
def getStateInstance():
    idInstance = request.form['idInstance']
    apiTokenInstance = request.form['apiTokenInstance']
    
    url = f"https://api.green-api.com/waInstance{idInstance}/getStateInstance/{apiTokenInstance}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Ошибка: неверный idInstance или apiTokenInstance."})
    else:
        return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
