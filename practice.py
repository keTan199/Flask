from flask import Flask

app = Flask (__name__)

@app.route ('/Home')

def hello_world():

    return 'Hello, World!'

app.run(debug=True)


#Run Command
#flask --app practice run
