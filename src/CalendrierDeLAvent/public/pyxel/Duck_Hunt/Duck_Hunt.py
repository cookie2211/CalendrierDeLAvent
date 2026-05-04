import pyxel
import random
class Jeu:
	def init(self):
		self.score = 0
		self.coincoin = []
		self.vies = 3
		pyxel.init(400,300, title="Duck Hunt", display_scale=2)
		pyxel.load("Duck_Hunt.pyxres")
		pyxel.mouse(True) #affiche la souris
		pyxel.run(self.update, self.draw)
		
		
	def canard(self):
		en_vie = True
		if pyxel.frame_count % 20 == 0:
			self.coincoin.append([random.randint(0, 270), 0])

	def canard_bouge(self):
		for glandu in self.coincoin:
			glandu[1] += 1.5
			glandu[0] += random.randint(-1, 1)
			if  glandu[1]>400:
				self.coincoin.remove(glandu)
				self.vies -= 1
				
	def tir(self):
		if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
			for glandu in self.coincoin:
				if glandu[0] < pyxel.mouse_y < glandu[0]+30 and glandu[1] < pyxel.mouse_x < glandu[1]+30: 
					self.coincoin.remove(glandu)
					self.score += 1

	def update(self):
		if pyxel.btnp(pyxel.KEY_ESCAPE):
			pyxel.quit()
		if self.vies > 0:
			# creation des ennemis
			self.canard()
			# mise a jour des positions des ennemis
			self.canard_bouge()
			self.tir()
			self.draw()
		else:
			if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
				self.vies = 3
				self.coincoin = []
				self.score = 0
	def draw(self):
		pyxel.cls(0)
		pyxel.bltm(0,0,0,0,0,400,300)
		for glandu in self.coincoin:
			pyxel.blt(glandu[1],glandu[0],0,11,46,30,30,0)
		pyxel.text(350,0,f"score: {self.score}", 7)
		for i in range(self.vies):
			pyxel.blt(20 + 12*i,0,0,1,74,12,12, 0)
		if self.vies == 0:
			pyxel.cls(0)
			pyxel.text(180,151,f"GAME OVER", 1)
			pyxel.text(179, 150, f"GAME OVER", 8)
			pyxel.text(179,171,f"score: {self.score}", 1)
			pyxel.text(178,170,f"score: {self.score}", 7)
			pyxel.text(161,191, f"cliquez pour rejouer", 1)
			pyxel.text(160, 190, f"cliquez pour rejouer", 7)
Jeu().init()