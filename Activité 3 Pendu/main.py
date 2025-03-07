# Importation de Flask et de render_template
from flask import Flask, render_template, session, redirect

# Importation du module os
import os

# Importation du module random
import random

# Création de l'instance de l'app Flask
app = Flask("Pendu")

app.secret_key = os.urandom(24)

@app.route("/")
def accueil():
    # Liste de mot
    liste_de_mots = ["tablette", "téléphone", "nourriture", "panda", "valorant", "minecraft", "pâtes", "casserole", "basketball", "football", "souris", "clavier"]
    # On choisit un mot au hasard
    mot_a_deviner = random.choice(liste_de_mots)
    # On définit le nombre de vies
    vies = 6

    return redirect("/jeu")

@app.route("/jeu")
def jeu():
    # On affiche notre page html
    return render_template("index.html")















# Exécution
app.run(host="0.0.0.0", port = 81)