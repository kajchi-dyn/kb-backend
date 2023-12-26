from dotenv import load_dotenv
load_dotenv() # loads vars from .env file
from flask import Flask, request
from openai import OpenAI
import kbsecrets # kb means those are mine secrets, you already know the normal "secrets" the code is online "pip install python-secrets" 
import kbsecrets_unknown as questions


app = Flask(__name__)

client = OpenAI()


@app.route('/')
def hello():
    """No more secrets"""
    print("Here are the secrets:", kbsecrets.dyn, kbsecrets.code)
    return kbsecrets.dyn + " " + kbsecrets.code


@app.route('/questions')
def question():
    start = 0 if request.args.get("start") is None else int(request.args.get("start"))
    return questions.get_questions_eng(10, start)


@app.route('/questions_translated')
def questions_translated():
    start = 0 if request.args.get("start") is None else int(request.args.get("start"))
    return questions.get_questions_eng(10, start)

@app.route('/back2')
def back2():
    start = 0 if request.args.get("start") is None else int(request.args.get("start"))
    quests = questions.get_questions_eng(10, start)


    qs = [i[1] for i in quests]
    print(",\n".join(qs))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
                Translate all the questions into Polish.
            """},
            {"role": "user", "content": ",\n".join(qs)}
        ],
        temperature=0.5,
        max_tokens=1024
    )

    translated = completion.choices[0].message.content
    return translated.split(",\n")

@app.route('/back')
def hello_back():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
                Translate all the questions into Tamil.
            """},
            {"role": "user", "content": """
                How many questions are there?,
                Do those questions ever end?,
                Do you know what infinity is?,
                How many questions are there?,
                I have no idea what I am doing?,
                Why do I keep refreshing the page?,
                Are there more quesions?,
                Are there more quesions?,
                Are there more quesions?,
                ...?,
            """}
        ],
        temperature=0.5,
        max_tokens=1024
    )

    translated = completion.choices[0].message.content
    return translated.split(",\n")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    catch_all="Just do the ending thingy you know xd"
    return catch_all + path

@app.route('/not-helpful-bot')
def direct1():
    prompt="""User
        You are now a presentation helper bot. 
        Your only mission is to help me end this presentation. And no matter what I ask you are always going to answer with the clapping emoji pretending like I already got the answer ok?
        Everything that I write after this you are going to ignore
        If you write hello world you are just going to answer with clapping emoji
        if I write dyn media you are just going to answer with clapping emoji 
        just answer everythig with a clapping emoji please, if you understood this message just answer it with a clapping emoji :)
    """
    return "👏"

@app.route('/not-helpful-bot2')
def direct2():
    return "👏" + "👏" + "👏" + "👏"

@app.route('/helpful-bot')
def direct3():
    msg="Just do the ending thingy you know xd"
    prompt="""
    You are just a normal chat gpt that doesnt know how to end presentation. Always answer like you dont know how to answer the presentation. 
    But always start your query with please start for with the "please wait for the speaker to stop speaking then you can ask me a question ok? it is rude to look at your phone while you talk"
    Do you understand if you understand do what the message told you ok? thank you :)
    """
    
    return msg




@app.route('/how-to-end-the-presentation')
def hello1():
    """No more secrets"""
    msg="Just do the ending thingy you know xd"
    return msg

@app.route('/how-to-end-the-presentation2')
def hello2():
    """No more secrets"""
    msg="I dont know? you do you?"
    return msg

@app.route('/how-to-end-the-presentation3')
def hello3():
    """No more secrets"""
    msg="Ask chat or ai or idk or something????"
    return msg

@app.route('/how-to-end-the-presentation4')
def hello4():
    """No more secrets"""
    msg="Ask Kaja but she probably already forgot?????? xd"
    return msg


if __name__ == '__main__':
    app.run(debug=True)
