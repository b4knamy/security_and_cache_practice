from flask import jsonify, session, render_template
from core import app, cache
from database import db_execute
from random import choice




@app.route('/api/each/name/<int:id>')
def each_name(id):
    is_cooked = f'each_name_{id}'
    if is_cooked in session:
        print('is_cooked from each')
        return jsonify(session[is_cooked])   
    
    data = db_execute(f'select * from names where id={id}').fetchone()
    session[is_cooked] = data

    return jsonify(data)

@app.route('/api/all/name/<int:limit>')
def all_name(limit):
    is_cookie = f'all_name_{limit}'
    if is_cookie in session:
        return jsonify(session[is_cookie])

    data = db_execute(f'SELECT * FROM names limit {limit}').fetchall()
    session[is_cookie] = data
    return jsonify(data)


@app.route('/')
@cache.cached(timeout=5)
def index():
    
    app_titles = ['API TEST', 'TEST API', 'SMALL API TEST', 'BIG API TEST??', 'BAD API TEST', 'GOOD API TEST']
    title = choice(app_titles) # Try reloading the page many times to see caching working
    print(title)
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)