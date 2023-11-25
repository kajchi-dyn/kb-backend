from flask import Flask
import secrets as kbsecrets # kb means those are mine secrets, you already know the normal "secrets" the code is online "pip install python-secrets" 

app = Flask(__name__)



@app.route('/')
def hello():
    """No more secrets"""
    print("Here are the secrets:", kbsecrets.dyn, kbsecrets.code)
    return 'Hello, this is a simple Flask app!'

if __name__ == '__main__':
    app.run(debug=True)
