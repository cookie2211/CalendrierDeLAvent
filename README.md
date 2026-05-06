# 🎄 Calendrier de l'Avent

Un calendrier de l’avent interactif développé en **Python**, accompagné d’un site web en **PHP / HTML / CSS / JavaScript**. Chaque jour débloque un mini‑jeu différent.

![Bannière du projet](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/index.png)

---

## 🚀 Démarrer le projet

### ▶️ Lancer la version locale

Pour démarrer le calendrier de l’avent localement :

1. Exécutez le fichier **`main.py`** à la racine du projet.
2. Assurez‑vous d’avoir une connexion Internet : certains scripts JavaScript nécessitent un accès réseau.

### 🌐 Via un serveur PHP

Vous pouvez également lancer le site à l’aide d’un serveur PHP local :

1. Placez vous à     CalendrierDeLAvent/src/CalendrierDeLAvent
2. tapez cette commande
```
php artisan serve
```
### sur internet

Le jeu est aussi disponible sur ce [site](https://calendrierdelavent.eu.pythonanywhere.com/)

---

## Les jeux du Calendrier

Chaque jour débloque un mini‑jeu différent. Certains jeux ont été développés par d’autres contributeurs — un lien vers leur profil GitHub est alors indiqué. 

---

### **Jour 1 – Duck Hunt**

Objectif : éliminer un maximum de canards.

* Tir : clic souris ou pression tactile.
* Vies représentées par des cœurs.
* Pas de victoire : seul le score final compte.

![Duck\_Hunt](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/DuckHunt.PNG)

---

### **Jour 2 – Pendu**

Le classique jeu du pendu, avec des mots autour du thème de Noël.

* 6 erreurs possibles.
* Répéter une lettre déjà tentée ne compte pas.
* ⚠️ Non compatible mobile pour le moment.

---

### **Jour 3 – Démineur**

Développeur : [*Mattis Vaucoulon*](https://github.com/Mat06v)

Un démineur complet :

* Découvrir toutes les cases sauf celles contenant des bombes.
* Numéros = nombre de bombes adjacentes.
* Rejouer : clic ou pression sur l’écran.
* Actions :

  * Découvrir : clic gauche / double‑clic / pression mobile.
  * Drapeau : clic droit / appui long mobile.

![Demineur](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/demineur.PNG)

---

### **Jour 4 – pyBROS**

Développeur : [*Bastien ISNARD*](https://github.com/Lisnarde)

Jeu de plateforme : atteindre l’arrivée.

* Déplacement : flèches ou gamepad.
* Saut : espace ou bouton X du gamepad.
* Si bloqué dans une plateforme : sauter pour s'en dégager.

![PyBros](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/PyBros.PNG)

---

### **🛸 Jour 5 – Ovnis**

Survivre et éliminer un maximum d’ennemis.

* Score final affiché en fin de partie.
* Tir : espace ou pression mobile.
* Mouvement : flèches ou gamepad.

---

### **🟡 Jour 6 – Pac‑Man**

Développeur : [*Elisabeth MAUPAS*](https://github.com/KitsuneNoMegami)

Version revisitée de Pac‑Man.

* Objectif : manger toutes les pièces.
* Cerises = bonus.
* Collision fantôme = Game Over.
* Téléportation sur les bords gauche/droit du milieu.

---

### **🐐 Jour 7 – FlapPY Goat**

Développeur : [*Bastien ISNARD*](https://github.com/Lisnarde)

Inspiré de Flappy Bird.

* Éviter les murs.
* Saut : espace ou pression mobile.
* Sortir de l’écran = Game Over.

---

### **⭕ Jour 8 – Morpy** (Morpion)

Développeur : *Alban STORCK*

Jeu du morpion à un joueur.

* Le premier à aligner 3 symboles gagne.

![Morpy](https://github.com/cookie2211/CalendrierDeLAvent/blob/v1/assets/Morpy.PNG)

---

### **🐍 Jour 9 – Snake**

Version classique de Snake.

* Manger des pommes pour grandir.
* Collision mur ou corps = Game Over.
* Contrôles : flèches ou gamepad.

---

## 📄 Licence

Projet distribué sous licence **MIT**. Voir le fichier `LICENSE` pour plus d’informations.
