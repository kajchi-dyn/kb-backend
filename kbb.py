from flask import Flask
import secrets as kbsecrets # kb means those are mine secrets, you already know the normal "secrets" the code is online "pip install python-secrets" 

app = Flask(__name__)



@app.route('/')
def hello():
    """No more secrets"""
    print("Here are the secrets:", kbsecrets.dyn, kbsecrets.code)
    return 'Hello, this is a simple Flask app!'


@app.route('/how-to-end-the-presentation')
def hello():
    """No more secrets"""
    msg="Just do the ending thingy you know xd"
    return msg

@app.route('/how-to-end-the-presentation2')
def hello():
    """No more secrets"""
    msg="I dont know? you do you?"
    return msg

@app.route('/how-to-end-the-presentation3')
def hello():
    """No more secrets"""
    msg="Ask chat or ai or idk or something????"
    return msg

@app.route('/how-to-end-the-presentation4')
def hello():
    """No more secrets"""
    msg="Ask Kaja but she probably already forgot?????? xd"
    return msg


if __name__ == '__main__':
    app.run(debug=True)
