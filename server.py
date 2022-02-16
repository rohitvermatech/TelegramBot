from flask import Flask, request
from TelegramBot import echo

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        echo(request.json)
    return "ok"


# main driver function
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=80)
