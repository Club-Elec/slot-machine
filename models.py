from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


class Joueurs(db.Model):
    __tablename__ = 'joueurs'

    id_joueur = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    mot_de_passe = db.Column(db.String(150))
    nb_credit = db.Column(db.Integer)

    def __repr__(self):
        return f"Joueur n°{self.id_joueur}, nommé {self.prenom} {self.nom}. Il possède {self.nb_credit} crédit(s)"


class Lots(db.Model):
    __tablename__ = 'lots'

    id_lot = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))
    probabilite = db.Column(db.String(50))

    def __repr__(self):
        return f"Lot n°{self.id_lot}, nommé {self.nom}. Il a {self.probabilite}% de chances de tomber"


class Tirages(db.Model):
    __tablename__ = 'tirages'

    id_tirage = db.Column(db.Integer, primary_key=True)

    id_joueur = db.Column(db.Integer, db.ForeignKey('joueurs.id_joueur'))
    joueurs = db.relationship("Joueurs", backref=backref("joueurs", uselist=False))

    id_lot = db.Column(db.Integer, db.ForeignKey('lots.id_lot'))
    lots = db.relationship("Lots", backref=backref("lots", uselist=False))

    date_tirage = db.Column(db.DateTime)
    reclame = db.Column(db.Boolean)

    def __repr__(self):
        return f"Tirage n°{self.id_tirage}, effectué par {self.joueurs} Il a {self.probabilite}% de chances de tomber"
