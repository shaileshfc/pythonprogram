import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    name = flask.request.args.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run()
