from flask import Flask
from waitress import serve
import os

app = Flask(__name__)

@app.route('/')
def hello():
    out = ["Hello World (forked)!"]
    for k, v in os.environ.items():
        out.append(f'{k}={v}')

    return str.join("<br>\n", out)


# to run: FLASK_APP=app python -m flask run
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
