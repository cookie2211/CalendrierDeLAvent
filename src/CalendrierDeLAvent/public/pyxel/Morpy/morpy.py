import pyxel
import random
TITLE = "Morpy"
WIDTH = 50
HEIGHT = 59
pyxel.init(WIDTH, HEIGHT, title=TITLE)
pyxel.load("morpy.pyxres")
tour = 1
victoire = False
egalite = False
pyxel.mouse(True)

class case:
    '''crée une classe case avec
        - la position x de son coin supérieur gauche sur la fenetre
        - la position y de son coin supérieur gauche sur la fenetre
        - son appartenance (0 si libre, 1 si elle est au joueur 1 et 2 si elle est au joueur 2'''
    def __init__(self, a, b, c):
        self.x_window = a
        self.y_window = b
        self.player = c
    
    def attribution_case(self):
            global tour

            self.player = tour
            tour=-tour
    def retour(self):
        global tour
        tour=-tour
        self.player=0
    def __str__(self):
        return self.player
        
haut_gauche = case(0, 9, 0)
haut_milieu = case(17, 9, 0)
haut_droit = case(34, 9, 0)
milieu_gauche = case(0, 26, 0)
centre = case(17,26,0)
milieu_droit = case(34, 26, 0)
bas_gauche = case(0, 43, 0)
bas_milieu = case(17,43,0)
bas_droit = case(34, 43, 0)
sound_timer=0
proba_erreur = 0.3 # probabilité que le bot fasse une erreur 

grille = [haut_gauche, haut_milieu, haut_droit,
          milieu_gauche, centre, milieu_droit,
          bas_gauche, bas_milieu, bas_droit    ]

def test_ligne(case1, case2, case3):
    '''Test si 3 case appartienne a l'un des joueurs et si oui renvoie ce joueur'''
    if case1.player == case2.player == case3.player != 0:
        return case1.player
    else : 
        return 0
def test_grille(g):
    if test_ligne(g[0], g[1], g[2]) != 0:
        return test_ligne(g[0], g[1], g[2])
    
    if test_ligne(g[3], g[4], g[5]) != 0:
        return test_ligne(g[3], g[4], g[5])
    
    if test_ligne(g[6], g[7], g[8]) != 0:
        return test_ligne(g[6], g[7], g[8])
    
    if test_ligne(g[0], g[3], g[6]) != 0:
        return test_ligne(g[0], g[3], g[6])
    
    if test_ligne(g[1], g[4], g[7]) != 0:
        return test_ligne(g[1], g[4], g[7])
        
    if test_ligne(g[2], g[5], g[8]) != 0:
        return test_ligne(g[2], g[5], g[8])
        
    if test_ligne(g[0], g[4], g[8]) != 0:
        return test_ligne(g[0], g[4], g[8])
        
    if test_ligne(g[2], g[4], g[6]) != 0:
        return test_ligne(g[2], g[4], g[6])
    return 0
        
def test_egalite(tab):
    for case in tab:
        if case.player == 0:
            return False
    return True


def clic_sur(self, x,y)-> bool:
        if pyxel.mouse_x >= x and pyxel.mouse_x <= x+16 and pyxel.mouse_y >= y and pyxel.mouse_y <= y+16 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return True
        else:
            return False

def draw():
    global tour
    global egalite
    
    pyxel.cls(0)
    pyxel.text(16, 1, "Morpy", 7)
    pyxel.line(16, 9, 16, 59, 7)
    pyxel.line(33, 9, 33, 59, 7)
    pyxel.line(0, 25, 50, 25, 7)
    pyxel.line(0, 42, 50, 42, 7)
    
    if tour == 1:
        pyxel.blt(1,1, 0, 32,0, 8, 8)
    else :
        pyxel.blt(1,1, 0, 40,0, 8, 8)
        
    for case in grille :
        if case.player == 1:
            pyxel.blt(case.x_window, case.y_window, 0, 0, 0, 16, 16, 0)
        if case.player == -1:
            pyxel.blt(case.x_window, case.y_window, 0, 16, 0, 16, 16, 0)
            
    if victoire == True :
        pyxel.rect(2, 24, 46, 25, 13)
        p="1"
        if tour==1:
            p="2"
        pyxel.text(5, 27, "Le joueur " + p, 11)
        pyxel.text(10, 33, "a gagne !", 11)
        pyxel.text(4, 26, "Le joueur " + p, 3)
        pyxel.text(9, 32, "a gagne !", 3)

        
    elif egalite == True :
        pyxel.rect(5, 27, 40, 24, 13)
        pyxel.text(9, 30, "Egalite !", 2)
        pyxel.text(8, 31, "Egalite !", 1)
        
    if victoire == True or egalite == True:
        pyxel.blt(21, 40, 0, 32, 8, 8, 8, 0)
    
                    
def update():
    global tour
    global victoire
    global egalite
    global sound_timer
    
    if sound_timer>0:
        sound_timer-=1
    
    
    if not egalite and not victoire and tour==1 and sound_timer<=0:
        for case in grille :
            if clic_sur(case, case.x_window, case.y_window):
                if case.player == 0:
                    case.attribution_case()
                    
                    if test_grille(grille):
                        victoire=True
                        pyxel.play(1,3)
                    if test_egalite(grille):
                        pyxel.play(1,4)
                        egalite=True
                    else:
                        pyxel.play(0, 1)
                    sound_timer=15

        
    elif not egalite and not victoire and sound_timer<=0:
        grille[move(grille)].attribution_case()
        if test_grille(grille):
            victoire=True
            pyxel.play(1,3)
        if test_egalite(grille):
            pyxel.play(1,4)
            egalite=True
        else:
            pyxel.play(0, 2)
        sound_timer=15


        
        
                
    if (pyxel.mouse_x >= 21 and pyxel.mouse_x <= 28 and pyxel.mouse_y >= 40 and pyxel.mouse_y <= 47 and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) )and (victoire == True or egalite == True):
        tour = 1
        for case in grille:
            case.player=0
        victoire = False
        egalite = False
        
        

def minimax(g, p):
    if test_grille(g):
        return test_grille(g)
    elif test_egalite(g):
        return 0
    if p==1:        
        maxi=-1
        for case in g:
            if case.player==0:
                case.attribution_case()
                m=minimax(g, -p)
                if m > maxi:
                    maxi=m
                case.retour()
        return maxi
    else:
        mini=1
        for case in g:
            if case.player==0:
                case.attribution_case()
                m=minimax(g, -p)
                if m < mini:
                    mini=m
                case.retour()
        return mini

        


def move(g):
    imin=[]
    mini=2
    for i in range(9):
        if g[i].player==0:
            g[i].attribution_case()
            m=minimax(g, 1)
            if m < mini:
                mini=m
                imin=[i]
            elif m==mini:
                imin.append(i)
            g[i].retour()
            
            
    if random.random() < proba_erreur:
        i=random.randint(1,8)
        while g[i].player!=0:
            i=random.randint(1,8)
        return i
    return imin[random.randint(0, len(imin)-1)]
                
                             
pyxel.run(update, draw)