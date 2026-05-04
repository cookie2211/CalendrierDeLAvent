import pyxel
import random


TITLE = "FlapPY Goat"
WIDTH = 400
HEIGHT = 300

class Jeu:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title=TITLE)
        
        self.p_x = 30
        self.p_y = 90
        self.p_w = 40
        self.p_h = 32
        
        self.murs = []
        self.taille_mur = 200
        
        
        self.grav = 1
        self.score = 0
        self.gameover = False
        self.scroll_y =960
        
        pyxel.load("FlapPY_Goat.pyxres")
        pyxel.run(self.update, self.draw)
        
    
    def saut(self):
        if self.grav < 10:
            self.grav += 1
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.grav = -10
        self.p_y += self.grav
        
    def creer_porte(self):
        if (pyxel.frame_count % 60 == 0):
            self.r = random.randint(5, 195)
            self.murs.append([WIDTH,self.r-self.taille_mur])
            self.murs.append([WIDTH,self.r+100])

    def ajt_score(self):
        if (pyxel.frame_count % 60 == 0):
            self.score += 1
            
    def sort_ecran(self):
        if self.p_y < -self.p_h or self.p_y > HEIGHT:
            self.gameover = True
    
    def collision(self):
        for mur in self.murs:
            if self.p_x+self.p_w > mur[0] and self.p_x < mur[0]+15 and self.p_y+self.p_h > mur[1] and self.p_y < mur[1]+self.taille_mur:
                self.gameover = True
                self.tmp = pyxel.frame_count
    
    
    
    def update(self):
        if self.gameover == False:
            self.saut()
            self.creer_porte()
            self.ajt_score()
            self.sort_ecran()
            self.collision()
            self.scroll()
        
            for mur in self.murs:
                mur[0] -= 5
                if mur[0] < -30:
                    self.murs.remove(mur)
                    
        if self.gameover == True:
            if pyxel.frame_count > self.tmp+10:
                if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.murs = []
                    self.p_y = 10
                    self.score = 0
                    self.gameover = False
    
    def scroll(self):
        if self.scroll_y>384:
            self.scroll_y -= 2
        else :
            self.scroll_y =960
    
    def draw(self):
        pyxel.cls(0)
        pyxel.camera()
        pyxel.bltm(-64,0,0,-((self.scroll_y) % 64)+64, 0, WIDTH+64, HEIGHT)
        
        pyxel.blt(self.p_x,self.p_y,0,0,0,self.p_w,self.p_h,11)
        
        for mur in self.murs:
            pyxel.rect(mur[0],mur[1],15,self.taille_mur,10)
            
        pyxel.text(WIDTH/2,5,str(self.score),12)
        
        if self.gameover == True:
            pyxel.blt(WIDTH/2,HEIGHT/2-2,0,0,64,32,16,0)
    
    
Jeu()