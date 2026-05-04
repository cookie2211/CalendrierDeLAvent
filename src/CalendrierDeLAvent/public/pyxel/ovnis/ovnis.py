# on rajoute random
import pyxel, random

class Jeu:
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        pyxel.init(128, 128, title="ovnis")

        # position initiale du vaisseau
        # (origine des positions : coin haut gauche)
        self.vaisseau_x = 60
        self.vaisseau_y = 60

        # vies
        self.vies = 4

        # initialisation des tirs
        self.tirs_liste = []

        # initialisation des ennemis
        self.ennemis_liste = []
        self.ennemisA_liste = []
        self.score = 0

        # initialisation des explosions
        self.explosions_liste = []

        # chargement des images
        pyxel.load("ovnis.pyxres")

        pyxel.run(self.update, self.draw)


    def deplacement(self):
        """déplacement avec les touches de directions"""

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) and self.vaisseau_x<120:
            self.vaisseau_x += 2
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) and self.vaisseau_x>0:
            self.vaisseau_x += -2
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) and self.vaisseau_y<120:
            self.vaisseau_y += 2
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP) and self.vaisseau_y>0:
            self.vaisseau_y += -2


    def tirs_creation(self):
        """création d'un tir avec la barre d'espace"""

        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.tirs_liste.append([self.vaisseau_x, self.vaisseau_y-4])


    def tirs_deplacement(self):
        """déplacement des tirs vers le haut et suppression quand ils sortent du cadre"""

        for tir in  self.tirs_liste:
            tir[1] -= 3
            if  tir[1]<-8:
                self.tirs_liste.remove(tir)


    def ennemis_creation(self):
        """création aléatoire des ennemis"""

        # un ennemi par seconde
        if (pyxel.frame_count % 30 == 0):
            self.ennemis_liste.append([random.randint(0, 120), 0])
    def ennemisA_creation(self):
        """création aléatoire des ennemis"""

        # un ennemi par seconde
        if (pyxel.frame_count % 50 == 0):
            self.ennemisA_liste.append([random.randint(0, 120), 0])


    def ennemis_deplacement(self):
        """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""              

        for ennemi in self.ennemis_liste:
            ennemi[1] += 1
            if  ennemi[1]>128:
                self.ennemis_liste.remove(ennemi)
            
    def ennemisA_deplacement(self):
        """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""              

        for ennemiA in self.ennemisA_liste:
            ennemiA[1] += 2
            if  ennemiA[1]>128:
                self.ennemisA_liste.remove(ennemiA)


    def vaisseau_suppression(self):
        """disparition du vaisseau et d'un ennemi si contact"""

        for ennemi in self.ennemis_liste:
            if ennemi[0] <= self.vaisseau_x+8 and ennemi[1] <= self.vaisseau_y+8 and ennemi[0]+8 >= self.vaisseau_x and ennemi[1]+8 >= self.vaisseau_y:
                self.ennemis_liste.remove(ennemi)
                self.vies -= 1
                # on ajoute l'explosion
                self.explosions_creation(self.vaisseau_x, self.vaisseau_y)
        for ennemiA in self.ennemisA_liste:
            if ennemiA[0] <= self.vaisseau_x+8 and ennemiA[1] <= self.vaisseau_y+8 and ennemiA[0]+8 >= self.vaisseau_x and ennemiA[1]+8 >= self.vaisseau_y:
                self.ennemisA_liste.remove(ennemiA)
                self.vies -= 1
                # on ajoute l'explosion
                self.explosions_creation(self.vaisseau_x, self.vaisseau_y)


    def ennemis_suppression(self):
        """disparition d'un ennemi et d'un tir si contact"""

        for ennemi in self.ennemis_liste:
            for tir in self.tirs_liste:
                if ennemi[0] <= tir[0]+8 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1] and ennemi[1] <= tir[1]+8:
                    self.ennemis_liste.remove(ennemi)
                    self.tirs_liste.remove(tir)
                    # on ajoute l'explosion
                    self.explosions_creation(ennemi[0], ennemi[1])
                    self.score += 10
    def ennemisA_suppression(self):
        """disparition d'un ennemi et d'un tir si contact"""

        for ennemiA in self.ennemisA_liste:
            for tir in self.tirs_liste:
                if ennemiA[0] <= tir[0]+8 and ennemiA[0]+8 >= tir[0] and ennemiA[1]+8 >= tir[1] and ennemiA[1] <= tir[1]+8:
                    self.ennemisA_liste.remove(ennemiA)
                    self.tirs_liste.remove(tir)
                    # on ajoute l'explosion
                    self.explosions_creation(ennemiA[0], ennemiA[1])
                    self.score += 20


    def explosions_creation(self, x, y):
        """explosions aux points de collision entre deux objets"""
        self.explosions_liste.append([x, y, 0])


    def explosions_animation(self):
        """animation des explosions"""
        for explosion in self.explosions_liste:
            explosion[2] +=1
            if explosion[2] == 12:
                self.explosions_liste.remove(explosion)


    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        if self.vies > 0:
            # deplacement du vaisseau
            self.deplacement()

            # creation des tirs en fonction de la position du vaisseau
            self.tirs_creation()

            # mise a jour des positions des tirs
            self.tirs_deplacement()

            # creation des ennemis
            self.ennemis_creation()
            self.ennemisA_creation()

            # mise a jour des positions des ennemis
            self.ennemis_deplacement()
            self.ennemisA_deplacement()

            # suppression des ennemis et tirs si contact
            self.ennemis_suppression()
            self.ennemisA_suppression()

            # suppression du vaisseau et ennemi si contact
            self.vaisseau_suppression()

            # evolution de l'animation des explosions
            self.explosions_animation()
        else:
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.vaisseau_x = 60
                self.vaisseau_y = 60
                self.vies = 4
                self.tirs_liste = []
                self.ennemis_liste = []
                self.ennemisA_liste = []
                self.score = 0
                self.explosions_liste = []
        


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        # si le vaisseau possede des vies le jeu continue
        if self.vies > 0:

            # affichage des vies            
            pyxel.text(5,5, 'VIES:'+ str(self.vies), 7)
            pyxel.text(5,11, 'SCORE:'+ str(self.score), 7)

            # vaisseau (carre 8x8)
            pyxel.blt(self.vaisseau_x, self.vaisseau_y, 0, 0, 0, 8, 8, 0)

            # tirs
            for tir in self.tirs_liste:
                pyxel.blt(tir[0], tir[1], 0, 8, 0, 8, 8,0)

            # ennemis
            for ennemi in self.ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1], 0, 0, 8, 8, 8,0)
            for ennemiA in self.ennemisA_liste:
                pyxel.blt(ennemiA[0], ennemiA[1], 0, 8, 8, 8, 8,0)

            # explosions (cercles de plus en plus grands)
            for explosion in self.explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)


        # sinon: GAME OVER
        else:
            pyxel.text(51,61,f"GAME OVER", 1)
            pyxel.text(50, 60, f"GAME OVER", 8)
            pyxel.text(50,75, 'Score:'+ str(self.score), 7)
            pyxel.text(25, 90, 'Cliquez pour rejouer', 7)
Jeu()