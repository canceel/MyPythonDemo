from flask import Flask,render_template,jsonify,make_response

_name='_main_'
app=Flask(_name)

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/mobile')
def mobile():
    return render_template("mobile.html")



print('Strat ....')
if _name=='_main_':
	app.run(host='0.0.0.0')