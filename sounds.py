import pygame

pygame.init()
pygame.mixer.init()
f = open('csv_data/sounds.txt', encoding='utf8').readlines()
print(f)

def z_bullet():
    pygame.mixer.music.load(f[0].strip())


def z_tower():
    pygame.mixer.music.load(f[1].strip())


def z_enemy():
    pygame.mixer.music.load(f[2].strip())


def play():
    pygame.mixer.music.set_volume(0.08)
    pygame.mixer.music.play()

