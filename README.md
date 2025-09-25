# CalendrierDeLAvent
Calendrier de l'avent fait en Python, avec un site web géré avec du php, html et css

![Bannière du projet](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/index.png)

Comment démarrer le site ‘calendrier de l’avent’ ?

Il faut simplement lancer le programme contenu dans le fichier ‘main.py’ (il se situe à la racine du dossier)
Attention, le site n’est pas accessible hors connexion (à cause du java script). 
Ce n’est pas un gros problème puisque à l’origine il s’agit d’un site internet, mais pour le démarrer en local il faut de la connexion.
Aussi accessible via un serveur php, si on le créé au niveau de la racine et qu'on va a /templates/index.php

Comment jouer aux jeux ?

Jour 1 - Duck Hunt :
le but est d'éliminer le plus de canards possibles pour les toucher il faut cliquer avec la souris ou taper sur l'écran le nombre de cœurs représente le nombre de vies restantes, quand il n'y en a plus la partie est finie, il n'y a pas de victoire possible, juste un score qui s'affiche à la fin.

![Duck_Hunt](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/DuckHunt.PNG)

Jour 2  - Pendu :
il s'agit du jeu du pendu avec des mots en lien avec noël, on a droit à 6 erreurs, si jamais on a déjà mis une lettre et que l'on souhaite la remettre, elle n'est pas prise en compte
ATTENTION : le jeu ne fonctionne pas encore sur téléphone 

Jour 3  - Démineur :
c'est un démineur, c'est une grille remplie de bombes, l'objectif étant de découvrir toutes les cases sauf celles où il y a les bombes, si on touche une bombe, c'est Game Over
le numéro sur une case indique le nombre de bombes sur les cases qui l'entourent.
Pour rejouer, cliquer ou taper sur l’écran, une nouvelle partie se relancera automatiquement
pour cliquer c'est clic gauche ou double clic (ou clic sur mobile),
pour poser un drapeau c'est clic droit (ou appui long sur mobile)

![Demineur](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/demineur.PNG)

jour 4  - pyBROS :
c'est un jeu de plateforme, le but est d'atteindre l'arrivée,
pour bouger à droite ou à gauche il faut utiliser les touches directionnelles (ou les flèches sur le gamepad),
pour sauter il faut appuyer sur espace (ou sur le bouton du haut (X) sur le gamepad).
si vous êtes coincés dans une plateforme, sautez et vous en sortirez

![PyBros](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/PyBros.PNG)

jour 5  - ovnis :
le but est d'éliminer le plus d'ennemis possible, le nombre de cœurs s'affiche en haut à gauche de l'écran,
on en perd quand on se fait toucher par un ennemi, quand il n'y en a plus la partie est finie, 
il n'y a pas de victoire possible, juste un score qui s'affiche à la fin
pour toucher les ennemis, il faut appuyer sur espace ou taper sur l'écran
pour bouger il faut utiliser les flèches directionnelles ou les flèches du gamepad

jour 6  - Pac Man :
il s'agit du célèbre jeu Pac Man, pour gagner il faut ramasser toutes les pièces du labyrinthe, si on touche un fantôme c'est Game Over.
les cerises rapportent des points supplémentaires.
pour bouger il faut rester appuyé sur les touches directionnelles ou les flèches du gamepad.
il y a un passage de téléportation entre le bord milieu droit et le bord milieu gauche.

Jour 7  - FlapPY Goat :
le but est de passer le plus de murs possibles, heurter un mur ou sortir de l'écran = Game Over
la gravité fait constamment chuter le personnage, il faut donc le faire sauter pour le maintenir en l'air
pour sauter il faut appuyer sur espace ou taper sur l'écran

jour 8  - Morpy :
c'est un morpion qui se joue à 2, le premier qui aligne 3 de ses symboles a gagné

![Morpy](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/Morpy.PNG)


jour 9  - Snake :
c'est un Snake, le but est d'avaler le plus de pommes possibles pour les manger il faut faire aller le serpent sur la case de la pomme,
il grandit à chaque fois qu'il en avale une. si on heurte le bord de la fenêtre ou qu'on heurte le corps du serpent, c'est Game Over et le score s’affiche.
pour faire bouger le serpent on utilise les flèches directionnelles ou les flèches du gamepad
