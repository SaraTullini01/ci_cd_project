from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "dimmi che funzioni ti prego!<br> non mi deludere!<br>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
