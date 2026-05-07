import pyxel
#import random

class Frog:
    def __init__(self,x,y):
        self.direction = -1
        self.positionX = x
        self.positionY = y

    def deplacement(self):
        self.direction = -1
        if (pyxel.btnp(pyxel.KEY_LEFT) or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)):
            self.direction=3
        elif (pyxel.btnp(pyxel.KEY_RIGHT)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)):
            self.direction=1
        elif (pyxel.btnp(pyxel.KEY_DOWN)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)):
            self.direction=2
        elif (pyxel.btnp(pyxel.KEY_UP)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP)):
            self.direction=0

    def setPosition(self, x, y):
        self.positionX += x
        self.positionY += y
    
    def getPositionX(self):
        return self.positionX
    
    def getPositionY(self):
        return self.positionY
    
    def draw(self):
        pyxel.rect(self.positionX,self.positionY,1,1,8)

class Case:
    def __init__(self, x, y):
        self.coche = False
        self.caillou = False
        self.positionX = x
        self.positionY = y

    def passer(self):
        self.coche = True
        self.afficher()

    def estCoche(self)->bool:
        return self.coche
    
    def estCaillou(self)->bool:
        return self.caillou
    
    def afficher(self):
        if self.coche == False:
            pyxel.rect(self.positionX,self.positionY,1,1,1)
        else:
            pyxel.rect(self.positionX,self.positionY,1,1,12)
        
class Grille:
    def __init__(self, x, y):
        self.tailleX=x
        self.tailleY=y
        self.tab = [[Case(x, y) for x in range(x)] for y in range(y)]

    def draw(self):
        for ligne in self.tab:
            for case in ligne:
                case.afficher()
    
    def getStatus(self): #Debug function
        for ligne in self.tab:
            line = ""
            for case in ligne:
                if case.estCaillou():
                    line += "/" 
                elif case.estCoche():
                    line += "x"
                else:
                    line += " "
            print(line)
    def passer(self,x,y):
        self.tab[x][y].passer()
    
    def estCoche(self,x,y)->bool:
        return self.tab[x][y].estCoche()

    def getTailleX(self):
        return self.tailleX
    
    def getTailleY(self):
        return self.tailleY
        
    
class Jeu:
    def __init__(self):
        self.grille = Grille(6, 7)
        pyxel.init(8, 8, title="FroPYmaze")
        #self.grille.getStatus()
        self.player = Frog(2,1)
        self.grille.passer(1,2)
        pyxel.run(self.update, self.draw)

        #pyxel.load("FroPYmaze.pyxres")
    
    def draw(self):
        
        self.grille.draw()
        self.player.draw()
    
    def deplacement(self):
        self.direction = -1
        if (pyxel.btnp(pyxel.KEY_LEFT) or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)):
            if ((self.player.getPositionX() > 0) and (self.grille.estCoche(self.player.getPositionY(), self.player.getPositionX()-1)) == False):
                self.player.setPosition(-1, 0)
                self.grille.passer(self.player.getPositionY(), self.player.getPositionX())
        elif (pyxel.btnp(pyxel.KEY_RIGHT)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)):
            if ((self.player.getPositionX() <self.grille.getTailleX()-1) and (self.grille.estCoche(self.player.getPositionY(), self.player.getPositionX()+1)) == False):
                self.player.setPosition(1, 0)
                self.grille.passer(self.player.getPositionY(), self.player.getPositionX())
        elif (pyxel.btnp(pyxel.KEY_DOWN)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)):
            if ((self.player.getPositionY() < self.grille.getTailleY()-1) and (self.grille.estCoche(self.player.getPositionY()+1, self.player.getPositionX())) == False):
                self.player.setPosition(0, 1)
                self.grille.passer(self.player.getPositionY(), self.player.getPositionX())
        elif (pyxel.btnp(pyxel.KEY_UP)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP)):
            if ((self.player.getPositionY() > 0) and (self.grille.estCoche(self.player.getPositionY()-1, self.player.getPositionX())) == False):
                self.player.setPosition(0, -1)
                self.grille.passer(self.player.getPositionY(), self.player.getPositionX())

    def perdu(self) -> bool:
        playX = self.player.getPositionX()
        playY = self.player.getPositionY()

        bloque_gauche = (
            playX == 0
            or self.grille.estCoche(playY, playX - 1)
        )

        bloque_droite = (
            playX == self.grille.getTailleX() - 1
            or self.grille.estCoche(playY, playX + 1)
        )

        bloque_haut = (
            playY == 0
            or self.grille.estCoche(playY - 1, playX)
        )

        bloque_bas = (
            playY == self.grille.getTailleY() - 1
            or self.grille.estCoche(playY + 1, playX)
        )

        return (
            bloque_gauche
            and bloque_droite
            and bloque_haut
            and bloque_bas
        )

    def update(self):
        self.deplacement()
        if (self.perdu()):
            print("PERDUUU")
        
        
        

Jeu()