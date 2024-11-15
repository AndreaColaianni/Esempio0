from flask import Flask
app = Flask (__name__)

@app.route('/')
def index():
    return 'Benvenuto'

@app.route('/prova')
def prova():
    return ('<h1>Provola</h1>')

app.run(host='localhost',debug=True)
