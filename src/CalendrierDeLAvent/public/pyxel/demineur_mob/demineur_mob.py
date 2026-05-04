import pyxel
from random import random

CASE = 8 # ne pas changer sans changer les dimensions des textures

LARGEUR = 20
LONGUEUR = 12
PROBA_MINE = 0.15 # probabbilité qu'une case contienne une mine
MODE_FACILE = True # si True, la première case clickée et toutes ses voisines ne contient pas de mine, permet d'éviter les situations ou l'on se base uniquement sur la chance

MOBILE = True # True si le jeu tourne sur un appareil mobile
TEMPS_MIN_DOUBLE_CLIC = 5 # en frames, temps min entre 2 clics pour être considéré comme un double clic, inutile si MOBILE = False
TEMPS_MAX_DOUBLE_CLIC = 15 # en frames, temps max entre 2 clics pour être considéré comme un double clic, inutile si MOBILE = False
TEMPS_MAINTENIR = 15 # en frames, temps min pendant lequel il faut maintenir le clic, inutile si Mobile = False


class Grille:
    def __init__(self, largeur:int, hauteur:int):
        """crée une grille de cases de dimension longueur * largeur"""
        self.larg = largeur
        self.haut = hauteur
        self.__tab = [[Case(x, y) for x in range(largeur)] for y in range(hauteur)]
        self.__premier_clic = MODE_FACILE
        self.souris = Souris(MOBILE)
    
    def afficher(self):
        """affiche la grille en affichant chaque case"""
        for ligne in self.__tab:
            for case in ligne:
                case.afficher()
                
    def calcul_voisins(self):
        """calcule le nombre de mines voisines pour chaque case"""
        for x in range(self.larg):
            for y in range(self.haut):
                self.__tab[y][x].mines_voisines = 0
                for voisin in self.voisins(x,y):
                    if voisin.mine:
                        self.__tab[y][x].mines_voisines += 1
    
    def voisins(self, x, y):
        """revoie les voisins d'une case sous forme de tableau"""
        return [self.__tab[j][i] for i in range(x-1, x+2) for j in range(y-1, y+2) if not (i==x and j==y) and 0 <= i <self.larg and 0 <= j < self.haut]


                
    def test_clic(self)->int:
        """
        gere les actions liées aux clicks du joueur
        renvoie 1 en cas de défaite, 2 en cas de victoire, 0 sinon
        """
        x, y = pyxel.mouse_x // CASE, pyxel.mouse_y // CASE # coordonées de la case clickée
        if x in range(self.larg) and y in range(self.haut):
            case = self.__tab[y][x]             
            if self.souris.clic_gauche() and not case.visible:
                if not case.drapeau:
                    #supprime les mines voisines pour le premier clic
                    if self.__premier_clic:
                        for c in [case]+self.voisins(case.x, case.y):
                            c.mine=False
                        self.calcul_voisins()
                        self.__premier_clic = False
                    
                    return self.devoiler(case)
                    
            if self.souris.clic_droit():
                case.changer_drapeau()
            
            # révele tout les voisins si clic gauche et droit sur une case déjà dévoilée sont le nombre de drapeau voisins correspond au nombre de mines voisines affichées
            if self.souris.clic_double() and case.visible:
                drapeau_voisins = 0
                for voisin in self.voisins(x,y):
                    if voisin.drapeau and not voisin.visible:
                        drapeau_voisins+=1
                if drapeau_voisins == case.mines_voisines:
                    for voisin in self.voisins(x, y):
                        if not voisin.drapeau:
                            a = self.devoiler(voisin)
                            if a != 0:
                                return a
              
                
        return 0

    def devoiler(self, case)->int:
        """
        rend la case visible
        renvoie 1 en cas de défaite, 2 en cas de victoire, 0 sinon
        """
        self.devoiler_rec(case.x, case.y)
        if case.mine:
            for ligne in self.__tab:
                for c in ligne:
                    if c.mine ^ c.drapeau:
                        c.devoiler()
            return 1
        if self.gagne():
            return 2
        return 0
    
    
    def devoiler_rec(self, x, y):
        """
        rend la case visible
        si la case n'a aucune mine voisine, dévoile toutes les cases voisines
        """
        
        if x in range(self.larg) and y in range(self.haut):
            case = self.__tab[y][x]
            if case.devoiler() and case.mines_voisines == 0 and not case.mine:
                for voisin in self.voisins(x,y):
                    voisin.drapeau = False
                    self.devoiler_rec(voisin.x, voisin.y)
    
    def gagne(self)->bool:
        """teste si la partie est gagné"""
        for ligne in self.__tab:
            for case in ligne:
                if not case.visible and not case.mine	:
                    return False
        return True
    
    
    
class Souris:
    """
    gère les input de la souris en fonction de l'appareil utilisé pour jouer
    """
    
    def __init__(self, mobile=False):
        self.mobile = mobile
        self.tps_dernier_clic = 0
        self.tps_maintenu = 0
        
    def clic_gauche(self, mobile=False)->bool:
        """
        Sur PC : clic gauche
        Sur mobile : double clic
        """
        if not self.mobile:
            return pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
        else:
            self.tps_dernier_clic += 1
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if TEMPS_MIN_DOUBLE_CLIC <= self.tps_dernier_clic <= TEMPS_MAX_DOUBLE_CLIC:
                    return True
                self.tps_dernier_clic = 0              
            
        
    def clic_droit(self, mobile=False)->bool:
        """
        Sur PC : clic droit
        Sur mobile : Maintenir
        """
        if not self.mobile:
            return pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT)
        else:
            if self.tps_maintenu >= TEMPS_MAINTENIR:
                self.tps_maintenu = 0
                return True
            
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.tps_maintenu += 1
            else:
                self.tps_maintenu = 0
            return False
        
        
    def clic_double(self, mobile=False)->bool:
        """
        Sur PC : clic droit et gauche en même temps
        Sur mobile : double clic
        """
        if not self.mobile:
            return pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)
        else:
            return self.clic_gauche()




class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.mine = random() < PROBA_MINE
        self.visible = False
        self.drapeau = False
        self.mines_voisines = 0
        
    def afficher(self):
        """affiche la case"""
        coord_x, coord_y = self.x*CASE, self.y*CASE
        if self.visible:
            pyxel.rect(coord_x, coord_y, CASE, CASE, (self.x + self.y) % 2) # crée un motif d'échiquier
            if self.mine:
                pyxel.blt(coord_x, coord_y, (self.x + self.y) % 2, 0, 8, CASE, CASE) # affiche une mine
            elif self.drapeau:
                pyxel.blt(coord_x, coord_y, (self.x + self.y) % 2, 0, 16, CASE, CASE) # affiche une croix si un drapeau placée est faux a la fin de la partie
            elif self.mines_voisines != 0:
                pyxel.text(coord_x + 3, coord_y + 1, str(self.mines_voisines), 16 - self.mines_voisines) # affiche le nombre de mines voisines

        else:
            pyxel.rect(coord_x, coord_y, CASE, CASE, (self.x + self.y + 1) % 2 + 6) # crée un motif d'échiquier
            if self.drapeau:
                pyxel.blt(coord_x, coord_y, (self.x + self.y) % 2, 0, 0, CASE, CASE) # affiche un drapeau

                
    def devoiler(self)->bool:
        """rend la case visible, renvoie False si la case était déja visible, True sinon"""
        if not self.visible:
            self.visible = True
            return True
        return False
    
    def changer_drapeau(self):
        if not self.visible:
            self.drapeau = not self.drapeau
        
        


class Jeu:
    def __init__(self):
        self.grille = Grille(LONGUEUR, LARGEUR)
        
        pyxel.init(LONGUEUR*CASE, LARGEUR*CASE, title="Démineur")
        pyxel.mouse(not MOBILE) # affiche la souris si la partie est joué sur un PC
        pyxel.load("demineur_mob.pyxres")
        self.termine = False # vaut True lorque la partie est terminée
        self.win = False
        
        pyxel.run(self.update, self.draw)
        

    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        
        if not self.termine:
            a = self.grille.test_clic()
            if a == 1:
                self.termine = True
                print("game over") # à modifier pour gérer la défaite dans l'application flask
            elif a == 2:
                self.termine = True
                print("gagné")  # à modifier pour gérer la victoire dans l'application flask
                self.win = True
        else:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.termine=False
                self.grille = Grille(LONGUEUR, LARGEUR)

                
        
        

    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        self.grille.afficher()
        if self.termine== True and self.win == True:
            pyxel.cls(0)
            pyxel.text(36,71,f"You Win !",1)
            pyxel.text(35,70,f"You Win !",10)
            pyxel.text(10,80, f"cliquez pour rejouer",7)

Jeu()



        