from flask import Flask, render_template, send_file
import random

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
	tab = []
	for i in range(1,25):
		tab.append(i)
	tab2 = []
	while len(tab) != 0:
		nbaléa = random.choice(tab)
		tab2.append(nbaléa)
		tab.remove(nbaléa)
	return render_template("index.html", tab=tab2, end=24, jmatv=3)


@app.route('/jour_<num>.html', methods=["GET", "POST"])
def pages(num: None):
	return send_file("templates\\jour_" + num + ".html")

@app.route('/jeux/<nom>.<ext>')
def truc(nom: None, ext: None):
	return send_file('jeux\\' + nom + '\\' + nom + '.' + ext)

if __name__ == '__main__':
	app.run(host = "0.0.0.0")