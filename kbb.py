from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello():
    """Huh there arent also any secrets here where are they? maybe you should ask the presenter"""
    return 'Hello, this is a simple Flask app!'

if __name__ == '__main__':
    app.run(debug=True)
