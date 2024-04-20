from flask import Flask, jsonify, session, request
from flask_cors import CORS
from database import db_execute

app = Flask(__name__)
CORS(app=app, resources={'/api/*': {
    'origins': 'http://127.0.0.1:5500', 'max_age': 12}})


@app.route('/api/name/<int:id>')
def home(id):
    session['username'] = 'heronosso'
    session['password'] = '123'
    if request.method == 'GET':
        print('eoq')
    return jsonify(session)
    return jsonify(db_execute(f'select * from names where id={id}').fetchone())

@app.route('/api/all')
def another():

    return jsonify(db_execute('SELECT * FROM names limit 2').fetchall())


if __name__ == '__main__':
    app.secret_key = 'eoq'
    host = '0.0.0.0'
    app.run(debug=True, host=host)