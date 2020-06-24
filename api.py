from flask import Flask
from decorators import with_static

app = Flask(__name__)


@app.route('/index')
@with_static('index.html')
def index():
    return dict(value=42)


if __name__ == "main":
    app.run(debug=True)
