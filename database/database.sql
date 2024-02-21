drop database if exists slot_machine;
create database slot_machine;
use slot_machine;

create table joueurs (
	id_joueur integer auto_increment,
	nom varchar(50),
	prenom varchar(50),
	mot_de_passe varchar(150),
	nb_credits integer default (0),
    is_admin boolean default (0),
	PRIMARY KEY (id_joueur)

);

create table lots (
	id_lot integer auto_increment,
	nom varchar(255),
	probabilite integer,
	PRIMARY KEY (id_lot)
);

create table tirages (
	id_tirage integer auto_increment,
	id_joueur integer,
	id_lot integer,
	date_tirage datetime,
	reclame boolean,
	PRIMARY KEY (id_tirage),
	FOREIGN KEY (id_joueur) REFERENCES joueurs(id_joueur),
	FOREIGN KEY (id_lot) REFERENCES lots(id_lot)
);


# Inital data insert

# Table joueurs
insert into joueurs (prenom, nom, mot_de_passe, nb_credits) values
('Jean', 'Citron', 'motdepasse', 20),
('Michel', 'FilsdeJack', 'motdepasse', 10),
('Gros', 'Caillou', 'motdepasse', 5),
('Gogo', 'Gadget', 'motdepasse', 2),
('Filles', 'Epices', 'motdepasse', 0);

# Table lots
insert into lots (nom, probabilite) values
('Shot de techpaf', 20),
('Rien', 40),
('Chouchen', 10),
('Pneu', 30);

# Table tirage
insert into tirages (id_joueur, id_lot, date_tirage, reclame) values
(1, 1, NOW(), false),
(1, 2, NOW(), true),
(1, 3, NOW(), false),
(1, 4, NOW(), true),
(2, 1, NOW(), false),
(2, 2, NOW(), true),
(2, 3, NOW(), false),
(2, 4, NOW(), true),
(3, 1, NOW(), false),
(3, 2, NOW(), true),
(3, 3, NOW(), false),
(3, 4, NOW(), true),
(4, 1, NOW(), false),
(4, 2, NOW(), true),
(4, 3, NOW(), false),
(4, 4, NOW(), true);create database if not exists slot_machine;
use slot_machine;

create table joueurs (
	id_joueur integer auto_increment,
	nom varchar(50),
	prenom varchar(50),
	mot_de_passe varchar(150),
	nb_credits integer default (0),
	PRIMARY KEY (id_joueur)

);

create table lots (
	id_lot integer auto_increment,
	nom varchar(255),
	probabilite integer,
	PRIMARY KEY (id_lot)
);

create table tirages (
	id_tirage integer auto_increment,
	id_joueur integer,
	id_lot integer,
	date_tirage datetime,
	reclame boolean,
	PRIMARY KEY (id_tirage),
	FOREIGN KEY (id_joueur) REFERENCES joueurs(id_joueur),
	FOREIGN KEY (id_lot) REFERENCES lots(id_lot)
);


# Inital data insert

# Table joueurs
insert into joueurs (prenom, nom, mot_de_passe, nb_credits) values
('Jean', 'Citron', 'motdepasse', 20),
('Michel', 'FilsdeJack', 'motdepasse', 10),
('Gros', 'Caillou', 'motdepasse', 5),
('Gogo', 'Gadget', 'motdepasse', 2),
('Filles', 'Epices', 'motdepasse', 0);

# Table lots
insert into lots (nom, probabilite) values
('Shot de techpaf', 20),
('Rien', 40),
('Chouchen', 10),
('Pneu', 30);

# Table tirage
insert into tirages (id_joueur, id_lot, date_tirage, reclame) values
(1, 1, NOW(), false),
(1, 2, NOW(), true),
(1, 3, NOW(), false),
(1, 4, NOW(), true),
(2, 1, NOW(), false),
(2, 2, NOW(), true),
(2, 3, NOW(), false),
(2, 4, NOW(), true),
(3, 1, NOW(), false),
(3, 2, NOW(), true),
(3, 3, NOW(), false),
(3, 4, NOW(), true),
(4, 1, NOW(), false),
(4, 2, NOW(), true),
(4, 3, NOW(), false),
(4, 4, NOW(), true);
