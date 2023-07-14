from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def print_bye():
    return "bye bye bye bye bye bye bye bye bye bye", 200


if __name__ == '__main__':
    app.run()
