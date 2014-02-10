from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello Engine Yard Folks!", where="Straight from Python")

@app.route('/test')
def test():
    return jsonify(message="We just tested a route! Boom")

if __name__ == '__main__':
    app.run()
