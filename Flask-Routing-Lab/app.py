from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/product')
def pr():
	return render_template("product.html")

@app.route('/cart')
def ca():
	return render_template("cart.html")

if __name__ == '__main__':
	app.run(debug = True)