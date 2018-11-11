from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['colors'] = ('lightgreen', 'pink', 'lightblue', 'gray', 'orange', 'black')

@app.route('/')
def start():
	return render_template('main.html', the_title = 'Welcome', back_color = 'white', colors = app.config['colors'])

@app.route('/result', methods = ['POST'])
def result():
	return redirect('/result/%s' %request.form['color'])

@app.route('/result/<color>')
def show_color(color):
	if color not in app.config['colors']:
		return render_template('res.html', 
			the_title = 'This is not gonna work...',
			back_color = 'black',
			message = "We don't have such color in our set")
	return render_template('res.html', 
		the_title = 'Here you go', 
		back_color = color, 
		message = 'Is that what you want?')

if __name__ == '__main__':
	app.run(debug = True)