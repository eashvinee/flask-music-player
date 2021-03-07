from flask import Flask, request,  jsonify, render_template, url_for
#from flaskwebgui import FlaskUI
from uapi import UAPI

app = Flask(__name__)
app.config.from_pyfile('config.py')
#ui = FlaskUI(app)



@app.route('/')
def index():
    term=request.args.get('q')

    if not term:
        term = 'bhojpuri'

    data =UAPI.search(term)
    #request.args.get('q')
    #print(data)
    return render_template('index.html', data = data, term=term)


@app.route('/uapi/search', methods=['GET', 'POST'])
def uapi_search():
    response =UAPI.search(request.args.get('q'))
    
    return jsonify(response)


@app.errorhandler(404)
def not_found(error):
    return 'Page not found!'   


