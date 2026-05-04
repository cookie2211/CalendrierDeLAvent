import pyxel
import random

WIDTH = 200
HEIGHT = 160
CASE = 10

class jeu:
    def __init__(self):
        pyxel.init(200, 160, 'Snake')
        self.snake =[[1, 3]]
        self.direction = [1, 0]
        self.score = 0
        self.nouriture = [random.randint(0, WIDTH/CASE-1),random.randint(0, HEIGHT/CASE-1)]
        self.game_over = False
        pyxel.load("snake.pyxres")
        pyxel.run(self.update, self.draw)
        
        
    def update(self):
        if self.game_over == False:

            if pyxel.frame_count % 7 == 0:
                head = [self.snake[0][0] + self.direction[0],
                        self.snake[0][1] + self.direction[1]]
                self.snake.insert(0, head)
            
            
                if head in self.snake[1:] or head[0] < 0 or head[0] > WIDTH/CASE - 1 or head[1] < 0 or head[1] > HEIGHT/CASE - 1:
                    self.game_over = True                                 #revoir le code
                
                if head == self.nouriture:
                    self.score += 1
                    while self.nouriture in self.snake:
                        self.nouriture = [random.randint(0, WIDTH/CASE-1),
                                random.randint(0, HEIGHT/CASE-1)]
                else: 
                    self.snake.pop()
            
            if pyxel.btnp(pyxel.KEY_ESCAPE):
                pyxel.quit()
            elif (pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)) and self.direction[0] != -1:
                self.direction = [1, 0]
            elif (pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)) and self.direction[0] != 1:
                self.direction = [-1, 0]
            elif (pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP)) and self.direction[1] != 1:
                self.direction = [0, -1]
            elif (pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)) and self.direction[1] != -1:
                self.direction = [0, 1]
        else:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.game_over = False
                self.snake =[[1, 3]]
                self.direction = [1, 0]
                self.score = 0
                self.nouriture = [random.randint(0, WIDTH/CASE-1),random.randint(0, HEIGHT/CASE-1)]

        
    
    def draw(self):
        pyxel.cls(0)
        x_head, y_head = self.snake[0]
        dirh = self.direction[0]
        dirv = self.direction[1]
        img_place = 16
        if dirh == 0:
            dirh = 1
        if dirv == 0:
            dirv = 1
        if self.direction[1] != 0:
            img_place = 32
        pyxel.blt(x_head*10,y_head*10,0,img_place,0,10*dirh,10*dirv)
        
        for anneau in self.snake[1:]:
            x, y = anneau[0], anneau[1]
            pyxel.blt(x*10,y*10,0,0,0,10,10)
        
        x_nouriture, y_nouriture = self.nouriture
        pyxel.blt(x_nouriture*10, y_nouriture*10,0,0,16,10,10)
        
        pyxel.text(4, 4, f"SCORE : {self.score}", 7)
        if self.game_over == True:
            pyxel.rect(0,0,200,160,0)
            pyxel.text(85,80,f"GAME OVER", 1)
            pyxel.text(84, 79, f"GAME OVER", 8)
            pyxel.text(83,100,f"score : {self.score}", 7)
            pyxel.text(65, 120, f"cliquez pour rejouer", 7)
        
        
jeu().init()
        
   