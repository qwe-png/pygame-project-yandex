print("Настройки")
import pygame

class Sounds:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()


    def z_bullet(self):
        pygame.mixer.music.load("звук")


    def z_tower(self):
        pygame.mixer.music.load("звук")


    def z_enemy(self):
        pygame.mixer.music.load("звук")


    def z_click(self):
        pygame.mixer.music.load("звук")

    def play(self):
        pygame.mixer.music.play()
