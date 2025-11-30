import pyxel

TITLE = "pyBROS"
WIDTH = 200
HEIGHT = 150


class Jeu:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title=TITLE)
        
        self.p_x = 10
        self.p_y = 10
        
        self.sols = [(5,50,50), (75,50,30), (110,70, 40), (180,50,30), (230,40,30), (290,20,20),(360,40,40),
        (420,80,30), (480,70,30),(520,50,30),(470,30,30),(460,10,20),(445,-10,20),(380,-20,30)]
        self.arrivee = (380,-36)
        
        self.tirs = []
        self.grav = 1
        self.en_saut = False
        self.sens = 1
        self.win = False
        self.vies = 3
        
        pyxel.load("pyBROS.pyxres")
        pyxel.run(self.update, self.draw)

    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.p_x += 2
            self.sens = 1
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.p_x += -2
            self.sens = -1
    
    def gravite(self):
        self.test_x = self.p_x+8
        self.test_y = self.p_y+17
        
        self.en_air = True
        for s in self.sols:
            if self.test_y < s[1] or self.test_y > s[1]+8 or (self.test_x+2 < s[0] or self.test_x-2 > s[0]+s[2]):
                pass
            else:
                self.en_air = False
                self.en_saut = False
                
        if self.en_air == False:
            self.grav = 1
        else:
            self.p_y += self.grav
            self.grav += 0.3
        
    
    def sauter(self): #voir ici
        if (pyxel.btnp(pyxel.KEY_SPACE)or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y)) and self.en_air == False:
            self.en_saut = True
            pyxel.play(0,0)
        if self.en_saut == True:
            self.p_y -= 5
    
    def tombe(self):
        if self.p_y > 200:
            self.p_x = 10
            self.p_y = 10
            self.grav = 2
            self.vies -= 1
    
    def test_fin(self):
        if self.test_x > self.arrivee[0] and self.test_x < self.arrivee[0]+16 and self.test_y > self.arrivee[1] and self.test_y < self.arrivee[1]+18:
            self.win = True
            
    def tir(self):
        if pyxel.btnp(pyxel.KEY_B):
            self.tirs.append([self.p_x,self.p_y,self.sens])
        
        for tir in self.tirs:
            tir[0] += 5*tir[2]

        
    
    def update(self):
        pyxel.camera(self.p_x-WIDTH/2 + 10,
                    self.p_y-HEIGHT/2 )
        if self.win == False and self.vies > 0:
            self.deplacement()
            self.gravite()
            self.sauter()
            self.tombe()
            self.test_fin()
            self.tir()
        else:
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.win = False
                self.p_x = 10
                self.p_y = 10
                self.tirs = []
                self.grav = 1
                self.en_saut = False
                self.sens = 1
                self.vies = 3
        
    def draw(self):
        pyxel.cls(0)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            if (pyxel.frame_count % 10 < 5):
                pyxel.blt(self.p_x ,self.p_y , 0,0,0,self.sens*16,16,0)
            else:
                pyxel.blt(self.p_x ,self.p_y , 0,32,0,self.sens*16,16,0)
        else:
            pyxel.blt(self.p_x ,self.p_y , 0,0,0,self.sens*16,16,0)
            
            
        for tir in self.tirs:
            pyxel.blt(tir[0],tir[1],0,0,40,8,8,0)
        
        #pyxel.circ(self.test_x, self.test_y, 1, 15)
        
        for s in self.sols:
            pyxel.bltm(s[0], s[1], 0, 0, 0,s[2],8) #h = 8 (hauteur)
            
        for i in range(self.vies):
            pyxel.blt(self.p_x -90 + 10*i,self.p_y -75,0,0,48,9,8, 0)
        
        pyxel.blt(self.arrivee[0] ,self.arrivee[1] , 0,0,16,16,16,0)
        
        if self.vies == 0:
            pyxel.cls(0)
            pyxel.text(5,5,f"GAME OVER", 1)
            pyxel.text(4, 4, f"GAME OVER", 8)
            
        if self.win == True:
            pyxel.text(self.p_x - 4, self.p_y - 4, "VICTOIRE", 1)
            pyxel.text(self.p_x - 5, self.p_y - 5, "VICTOIRE", 10)
            pyxel.text(self.p_x - 22, self.p_y - 29,f"cliquez pour rejouer", 1)
            pyxel.text(self.p_x - 23, self.p_y - 30,f"cliquez pour rejouer", 7)

        
Jeu()