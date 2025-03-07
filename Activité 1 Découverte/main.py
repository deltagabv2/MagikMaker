# Importation de Flask
from flask import Flask, render_template

# Création de l'application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page2')
def page2():
    erreur = "!! WARNING !!"
    return render_template("page2.html", erreur=erreur)

@app.route('/page3')
def page3():
    return render_template("page3.html",)


# Exécution de l'application
app.run(host = '0.0.0.0', port = 81)