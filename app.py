import MySQLdb
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_mysqldb import MySQL
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import logging
from datetime import datetime

colorama_init()

app = Flask(__name__)
app.debug = True
app.config['DEBUG'] = True

# Logging configuration
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'slot_machine'

# Creating a MySQL instance
mysql = MySQL(app)

print(f"{Fore.YELLOW}{Style.BRIGHT}Lancement de l'application : {datetime.now().strftime('%H:%M:%S')}{Fore.RESET}")


@app.route('/')
def index():
    #   Recuperation des données de la table joueurs (sans prendre en compte le mot de passe)
    print("Recuperation des données de la table joueurs (sans prendre en compte le mot de passe)")
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id_joueur, nom, prenom, nb_credits FROM joueurs")
        joueurs = cursor.fetchall()
        cursor.close()
        return render_template('index.html', joueurs=joueurs)
    except MySQLdb.OperationalError:
        print(f"{Fore.RED}Erreur de connexion à la base de donées{Fore.RESET}")

        return render_template('index.html', joueurs=[])


@app.route('/register')
def app_data():
    return render_template('register.html')


@app.route('/register_data', methods=["POST"])
def createjoueur():

    prenom: str = request.form.get("prenom")
    nom: str = request.form.get("nom")
    password: str = request.form.get("password")

    if prenom != '' and nom != '' and password is not None:
        print(
            f"insertion dans la table joueurs d'un nouvel élément : nom : {nom},"
            f" prenom : {prenom}, password : {password}"
        )

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO joueurs (nom, prenom, mot_de_passe) "
                       "VALUES (%s, %s, %s)", (nom, prenom, password))
        mysql.connection.commit()
        cursor.close()

        return redirect('/')
    else:
        print("Un des champs est vide")
        return redirect('/')


if __name__ == '__main__':
    app.run()
