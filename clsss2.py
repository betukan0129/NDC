# Créé par beytu, le 30/10/2024 en Python 3.7
class Jeu: # POUR LES CELULLES DU JEU.
    def _init_(self,x,y,w,h,img,mask=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img =img
        self.mask = 0
    def deplacer(self,vel,d= 0):
        if d == 1:
            return self.x-vel,self.y-vel
        if d == 2:
            return self.x+vel,self.y-vel
        if d == 3:
            return self.x-vel,self.y+vel
        if d == 4:
            return self.x+vel,self.y+vel
