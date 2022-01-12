import pygame

pygame.init()
pygame.mixer.init()
f = open('csv_data/sounds.txt', encoding='utf8').readlines()


def z_bullet():
    pygame.mixer.music.load(f[0].strip())


def z_tower():
    pygame.mixer.music.load(f[1].strip())


def z_enemy():
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.load(f[2].strip())


def dead():
    pygame.mixer.music.load("z_data/dead.mp3")


def win():
    pygame.mixer.music.load()


def enemy_end():
    pygame.mixer.music.load("z_data/enmy_end.mp3")


def play():
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.08)
