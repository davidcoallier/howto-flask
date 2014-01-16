from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Engine Yard Python World!'

@app.route('/test')
def test():
    return "Testing from a route in Python"

if __name__ == '__main__':
    app.run()
