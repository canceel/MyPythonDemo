from flask import Flask,render_template,jsonify,make_response

_name='_main_'
app=Flask(_name)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

result={
	'code':200,
	'msg':'success',
	'data':tasks
}

@app.route('/')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/getTasks', methods=['GET'])
def get_tasks():
    return jsonify(result)

@app.route('/hello')
def hello():
    return render_template('returnHello.py')

@app.route('/about')
def about():
	return render_template('about/about.html')
	
errorInfo = {'error': 'Not found'}
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(result))

@app.route('/mine')
def mine():
	return render_template('mine.html',
		userName='Shenme')


print('Strat ....')
if _name=='_main_':
	app.run(host='0.0.0.0')