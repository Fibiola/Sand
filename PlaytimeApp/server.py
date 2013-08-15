from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def indrex():
	return render_template('index.html')

@app.route('/test')
def test():
	return "This is just a test"



if __name__ == '__main__':
	app.run(debug=True)