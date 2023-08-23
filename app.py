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


@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    idInstance = request.form['idInstance']
    apiTokenInstance = request.form['apiTokenInstance']
    chatId = request.form['chatId']
    message = request.form['message']
    
    url = f"https://api.green-api.com/waInstance{idInstance}/sendMessage/{apiTokenInstance}"
    payload = {
        "chatId": chatId,
        "message": message
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 200:
        return jsonify({"error": "Ошибка: неверный idInstance или apiTokenInstance."})
    else:
        return jsonify({"response": response.text})
    
@app.route('/sendFileByUrl', methods=['POST'])
def sendFileByUrl():
    idInstance = request.form['idInstance']
    apiTokenInstance = request.form['apiTokenInstance']
    chatId = request.form['chatId2']
    urlFile = request.form['urlFile']
    fileName = urlFile.split('/')[-1]  # Extracting the filename from the URL
    
    url = f"https://api.green-api.com/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}"
    payload = {
        "chatId": chatId,
        "urlFile": urlFile,
        "fileName": fileName,
        "caption": "Отправлен с помощью GreenAPI"
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 200:
        return jsonify({"error": "Ошибка при отправке файла."})
    else:
        return jsonify({"response": response.text})
    
if __name__ == '__main__':
    app.run(debug=True)