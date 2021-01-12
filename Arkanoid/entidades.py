import pygame as pg
from Arkanoid import GAME_DIMENSIONS

import random
import sys

pg.init()

class Pelota:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.imagen_act = 0
        self.imagenes = self.cargaImagenes()
        self.imagen = self.imagenes[self.imagen_act]
        
    def cargaImagenes(self):
        lista_imagenes = []
        for img in self.imagenes_files:
            lista.imagenes.append(pg.image.load(f"resources/images/{img}"))
            
        return lista_imagenes

    @property
    def rect(self):
        return self.imagen.get_rect(topleft=(self.x, self.y))
    
    def avanzar(self):
        """Gestionar posicion de pelota"""
        if self.rect.left <= 0 or self.rect.right >= GAME_DIMENSIONS[0]:
            self.vx = -self.vx

        if self.rect.top <= 0 or self.rect.bottom >= GAME_DIMENSIONS[1]:
            self.vy = -self.vy
        
        self.x += self.vx
        self.y += self.vy
        
        """Gestionar imagen activa (disfraz) pelota"""
        self.imagen_act += 1
        if self.imagen_act >= len(self.imagenes):
            self.imagen_act = 0
        self.imagen = self.imagenes[self.imagen_act]
        
class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode(GAME_DIMENSIONS)
        pg.display.set_caption("Futuro Arkanoid")
        self.pelota = Pelota(400, 300, 10, 10)


    def bucle_principal(self):
        game_over = False
        
        while not game_over:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.pelota.avanzar()

            self.pantalla.fill((0,0,255))
            self.pantalla.blit(self.pelota.imagen, (self.pelota.x, self.pelota.y))

            pg.display.flip()


