from numpy import true_divide
import pygame
import random

class cuerpo:
    def __init__(self,ventana):
        self.x=0
        self.y=0
        self.dir=0
        self.ventana= ventana

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255,255,255), (self.x, self.y, 10, 10))
    
    def moverse(self):
        if self.dir == 0:
            self.y += 10
        elif self.dir == 1:
            self.y -= 10
        elif self.dir == 2:
            self.x += 10
        elif self.dir == 3:
            self.x -= 10

class manzanas:
    def __init__(self,ventana):
        self.x=random.randrange(40)*10
        self.y=random.randrange(40)*10
        self.ventana=ventana 

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255,0,0), (self.x, self.y, 10, 10))
    
    def nueva_manzana(self):
         self.x=random.randrange(40)*10
         self.y=random.randrange(40)*10

def refrescar(ventana):
    ventana.fill((0,0,0))
    comida.dibujar() 
    for i in range (len(serpiente)):
        serpiente[i].dibujar()

def seguir_cabeza():
    for i in range (len(serpiente) - 1):
        serpiente[len(serpiente) - i - 1].x = serpiente[len(serpiente) - i - 2].x
        serpiente[len(serpiente) - i - 1].y = serpiente[len(serpiente) - i - 2].y
    

def main():
    global serpiente, comida
    ventana = pygame.display.set_mode((900,600))
    ventana.fill ((0,0,0))
    comida= manzanas(ventana)
    serpiente=[cuerpo(ventana)]
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    serpiente[0].dir = 0
                if event.key == pygame.K_w:
                    serpiente[0].dir = 1
                if event.key == pygame.K_d:
                    serpiente[0].dir = 2
                if event.key == pygame.K_a:
                    serpiente[0].dir = 3
        seguir_cabeza()
        serpiente[0].moverse()
        refrescar(ventana)
        pygame.display.update()
        pygame.time.delay(100)
        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            comida.nueva_manzana()
            serpiente.append(cuerpo(ventana))

if __name__ == '__main__':
    main()
    pygame.quit()