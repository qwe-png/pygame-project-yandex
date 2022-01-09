import pygame

pygame.init()
pygame.mixer.init()
f = open('csv_data/sounds.csv', encoding='utf8').read().split(";")
print(f)

def z_bullet():
    pygame.mixer.music.load(f[0])


def z_tower():
    pygame.mixer.music.load(f[1])


def z_enemy():
    pygame.mixer.music.load(f[2])


def z_click():
    pygame.mixer.music.load(f[3])


def play():
    pygame.mixer.music.play()
