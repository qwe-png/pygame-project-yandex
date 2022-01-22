import pygame
import cv2
from subprocess import Popen, run, call
import os
import sys
import sounds
import argparse



def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def terminate():
    # выход
    pygame.quit()
    sys.exit()

def main_preobrazovatel(file_gif):
    size = file_gif.shape[1::-1]
    file_gif[:, :, [0, 2]] = file_gif[:, :, [2, 0]]
    surface = pygame.image.frombuffer(file_gif.flatten(), size, 'RGB')
    return surface.convert()

def loader(file):
    dvizh = cv2.VideoCapture(file)
    up = []
    while True:
        n, im = dvizh.read()
        if not n:
            break
        pygameImage = main_preobrazovatel(im)
        up.append(pygameImage)
    return up


sounds.dead()
sounds.play()
pygame.init()
screen = pygame.display.set_mode((500, 519))
clock = pygame.time.Clock()
v_menu_btn = False
play_again_btn = False
na_kartu = False
sama_gifka = loader(r"data/game_over_gif.gif")
fps = 1
provershit = 1
banan = True
while banan:
    provershit += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                call(['python', 'main_menu.py'])
                terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if 179 < int(event.pos[0]) < 313 and 256 < int(event.pos[1]) < 288:
                banan = False
                play_again_btn = True
            if 179 < int(event.pos[0]) < 313 and 304 < int(event.pos[1]) < 341:
                banan = False
                na_kartu = True
            if 179 < int(event.pos[0]) < 313 and 351 < int(event.pos[1]) < 388:
                banan = False
                v_menu_btn = True

    res = sama_gifka[fps].get_rect(center=(250, 159))
    knopki_image = load_image('menu_proigrisha.png')

    screen.blit(sama_gifka[fps], res)
    screen.blit(knopki_image, (-80, 220))


    if provershit % 15 == 0:
        fps = (fps + 1) % len(sama_gifka)
        provershit = 1
        pygame.display.flip()

def rin(runfile):
    with open(runfile,"r") as rnf:
        exec(rnf.read())


if play_again_btn:
    pygame.display.quit()
    call(['python', 'main.py'])
    play_again_btn = False
    terminate()
elif v_menu_btn:
    pygame.display.quit()
    call(['python', 'main_menu.py'])
    v_menu_btn = False
    terminate()
elif na_kartu:
    pygame.display.quit()
    call(['python', 'map.py'])
    na_kartu = False
    terminate()