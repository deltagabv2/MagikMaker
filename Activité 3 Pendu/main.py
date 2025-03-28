# Importation de Flask et de render_template
from flask import Flask, render_template, session, redirect, request

# Importation du module os
import os

# Importation du module random
import random

# Création de l'instance de l'app Flask
app = Flask("Pendu")

from pendu import Pendu
app.secret_key = os.urandom(24)

@app.route("/")
def accueil():
    # Liste de mot
    liste_de_mots = ["tablette", "téléphone", "nourriture", "panda", "valorant", "minecraft", "pâtes", "casserole", "basketball", "football", "souris", "clavier"]
    # On choisit un mot au hasard
    mot_a_deviner = random.choice(liste_de_mots)
    # On définit le nombre de vies
    vies = 6
    # On crée une instance du Pendu
    session["etat_du_jeu"] = Pendu.initialisation(mot_a_deviner, vies)

    return redirect("/jeu")

@app.route("/jeu")
def jeu():
    # On affiche notre page html
    return render_template("index.html", etat_du_jeu = session["etat_du_jeu"])

# On crée un route pour l'entrée de l'utilisateur
@app.route("/deviner", methods=["POST"])
def deviner():
    # On récupère l'entrée de l'utilisateur
    entree = request.form["entree"]
    # On met à jour le jeu grâce à la méthode deviner
    session["etat_du_jeu"] = Pendu.deviner(session["etat_du_jeu"], entree.upper())
    # On redirige vers l'affichage du jeu
    return redirect("/jeu")





# Exécution
app.run(host="0.0.0.0", port = 81)

# Fin fonctionnelle : 👎
# Defaite : 👎
# Victoire : 👍
# Vies : 👎
# Bonnes lettres : 👍
# Mot entier : 👍
# Test du mot partiel : 
# Affichage du message : 👍
# Champ vide : 👍
# Deux fois la même lettre : 👍