import pyxel
import random
#import sys

class PenduGame:
    def init(self):
        self.mots = ['SAPIN','ETOILE','NOEL','BUCHE','GATEAUX','RENNES','NEIGE','CADEAUX', 'CHOCOLATS',
					 'DECORATIONS','ROUGE','VERT','GUIRLANDE','REVEILLON','BOULES','VIN CHAUD','PERE NOEL',
					 'BONNET','LUTIN','HOTTE','TRAINEAU','CHEMINEE','CRECHE','RUDOLPH','BOUGIE']
        self.mot_secret = random.choice(self.mots).upper()
        self.essais = []
        self.tirets = ["_"] * len(self.mot_secret)
        for i in range(len(self.mot_secret)):
            if self.mot_secret[i] == " ":         #au cas où y'a un espace dane le mot
                 self.tirets[i] = " "
        self.max_essais = 6
        self.essais_restants = self.max_essais
        self.win = False
        self.lettres_saisies = [""]

        pyxel.init(90,90, title="pendu")
        pyxel.load("pendu.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if self.essais_restants > 0 and self.win == False:
            self.draw()
            lettre = ""
            
            if pyxel.btnp(pyxel.KEY_A):
                lettre = "A"
            if pyxel.btnp(pyxel.KEY_B):
                lettre = "B"
            if pyxel.btnp(pyxel.KEY_C):
                lettre = "C"
            if pyxel.btnp(pyxel.KEY_D):
                lettre = "D"
            if pyxel.btnp(pyxel.KEY_E):
                lettre = "E"
            if pyxel.btnp(pyxel.KEY_F):
                lettre = "F"
            if pyxel.btnp(pyxel.KEY_G):
                lettre = "G"
            if pyxel.btnp(pyxel.KEY_H):
                lettre = "H"
            if pyxel.btnp(pyxel.KEY_I):
                lettre = "I"
            if pyxel.btnp(pyxel.KEY_J):
                lettre = "J"
            if pyxel.btnp(pyxel.KEY_K):
                lettre = "K"
            if pyxel.btnp(pyxel.KEY_L):
                lettre = "L"
            if pyxel.btnp(pyxel.KEY_M):
                lettre = "M"
            if pyxel.btnp(pyxel.KEY_N):
                lettre = "N"
            if pyxel.btnp(pyxel.KEY_O):
                lettre = "O"
            if pyxel.btnp(pyxel.KEY_P):
                lettre = "P"
            if pyxel.btnp(pyxel.KEY_Q):
                lettre = "Q"
            if pyxel.btnp(pyxel.KEY_R):
                lettre = "R"
            if pyxel.btnp(pyxel.KEY_S):
                lettre = "S"
            if pyxel.btnp(pyxel.KEY_T):
                lettre = "T"
            if pyxel.btnp(pyxel.KEY_U):
                lettre = "U"
            if pyxel.btnp(pyxel.KEY_V):
                lettre = "V"
            if pyxel.btnp(pyxel.KEY_W):
                lettre = "W"
            if pyxel.btnp(pyxel.KEY_X):
                lettre = "X"
            if pyxel.btnp(pyxel.KEY_Y):
                lettre = "Y"
            if pyxel.btnp(pyxel.KEY_Z):
                lettre = "Z"

            if not lettre in self.lettres_saisies:
                self.complete(lettre)
                self.lettres_saisies.append(lettre)
            else:
                self.lettres_saisies.append(lettre)
        else:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.mot_secret = random.choice(self.mots).upper()
                self.essais = []
                self.tirets = ["_"] * len(self.mot_secret)
                for i in range(len(self.mot_secret)):
                    if self.mot_secret[i] == " ":         #au cas où y'a un espace dane le mot
                        self.tirets[i] = " "
                self.max_essais = 6
                self.essais_restants = self.max_essais
                self.win = False
                self.lettres_saisies = [""]
    
    def complete(self, lettre):
        lettre_juste = False
        self.win = True
        for x in range(len(self.mot_secret)):
            if lettre == self.mot_secret[x]: 
                self.tirets[x] = lettre
                lettre_juste = True
            if self.tirets[x] == '_':
                self.win = False
        if lettre_juste == False:
            self.essais_restants -= 1
    
    def centre(self, mot):
        long = len(mot)*3 + len(mot) -1
        long = 45 - long // 2
        return long
    
    
    def draw(self):
        pyxel.cls(0)
        # affiche le mot secret
        affiche = " ".join(self.tirets)                #affiche le mot sans être un tableau
        pyxel.text(self.centre(affiche), 50, f"{affiche}", 7)

        # affichage des essais restants
        pyxel.text(10, 75, f"essais restants: {self.essais_restants}", 1)
        pyxel.text(10, 74, f"essais restants: {self.essais_restants}", 7)
        # Dessin du pendu
        if self.win:
            pyxel.rect(0,0,90,90,0)
            pyxel.blt(30,17,0,0,0,32,32, 0)
            pyxel.text(38,61,f"WIN", 1)
            pyxel.text(37, 60, f"WIN", 10)
            pyxel.text(8,5,f"espace pour rejouer",7)
        elif self.essais_restants == 6:
            pyxel.blt(30,17,1,0,0,32,32)
        elif self.essais_restants == 5:
            pyxel.blt(30,17,1,0,32,32,32)
        elif self.essais_restants == 4:
            pyxel.blt(30,17,1,0,64,32,32)
        elif self.essais_restants == 3:
            pyxel.blt(30,17,1,0,96,32,32)
        elif self.essais_restants == 2:
            pyxel.blt(30,17,1,0,128,32,32)
        elif self.essais_restants == 1:
            pyxel.blt(30,17,1,0,160,32,32)
        else:
            pyxel.rect(0,0,90,90,0)
            pyxel.blt(30,17,2,0,0,32,32)
            pyxel.text(28,61,f"GAME OVER", 1)
            pyxel.text(27, 60, f"GAME OVER", 8)
            pyxel.text(0,80,f"le mot etait: {self.mot_secret}",7)
            pyxel.text(8,5,f"espace pour rejouer",7)
PenduGame().init()