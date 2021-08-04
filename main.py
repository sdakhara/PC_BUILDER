from flask import Flask, render_template, jsonify
import requests

url = "https://cpu-data.p.rapidapi.com/cpus"

headers = {
    'x-rapidapi-key': "1c2a41ba92mshec9d61014ca2e68p1e3f1cjsn84607970fe3a",
    'x-rapidapi-host': "cpu-data.p.rapidapi.com"
}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cpu')
def cpu():
    response = requests.request("GET", url, headers=headers)

    return jsonify(response.text)


if __name__ == '__main__':
    app.run(debug=True)
