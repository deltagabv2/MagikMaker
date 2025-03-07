# Importation de Flask et de render_template
from flask import Flask, render_template, session, redirect

# Importation du module os
import os

# Importation de nos question
from questions import questions

# Imporation des résultats
from resultats import resultats

# Création de l'instance de l'app Flask
app = Flask("Ma_webapp")

app.secret_key = os.urandom(24)

# Route principal "/"-> notre page d'accueil qui est donc à la racine du site
@app.route("/")
def index():
    session["numero_question"] = 0
    session["score"] = {"1": 0, "2": 0, "3": 0, "4": 0}
    return render_template("index.html")


@app.route("/page2")
def question():
    global questions 
    nb_questions = session["numero_question"]
    if nb_questions < len (questions):
        question = questions[nb_questions]["question"]
        question_copy = questions[nb_questions].copy()
        question_copy.pop("question")
        reponses = list(question_copy.values())
        session["clefs"] = list(question_copy.keys())
        return render_template("page2.html", question = question, reponses = reponses)
    else :
        global resultats
        score = sorted(session["score"], key = session["score"].get, reverse = True)
        vainqueur = score[0]
        description = resultats[vainqueur]
        return render_template("page3.html", vainqueur = vainqueur, description = description)

@app.route("/reponse/<numero>")
def reponse(numero):
    session["numero_question"] += 1
    resultat = session["clefs"][int(numero)]
    session["score"][resultat] += 1
    return redirect("/page2")


# Exécution
app.run(host="0.0.0.0", port = 81)