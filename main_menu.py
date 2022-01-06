import pygame
import cv2
from subprocess import Popen, run, call
import os
import sys

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

pygame.init()
screen = pygame.display.set_mode((600, 430))
clock = pygame.time.Clock()
play_btn = False
store_btn = False
sama_gifka = loader(r"data/menu_gif.gif")
fps = 1
provershit = 1
banan = True
while banan:
    provershit += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if 200 < int(event.pos[0]) < 386 and 58 < int(event.pos[1]) < 133:
                banan = False
                play_btn = True
            if 200 < int(event.pos[0]) < 386 and 192 < int(event.pos[1]) < 265:
                banan = False
                store_btn = True
            if 200 < int(event.pos[0]) < 386 and 327 < int(event.pos[1]) < 401:
                 print('Вы нажали на кнопку settings')

    res = sama_gifka[fps].get_rect(center=(300, 300))

    screen.blit(sama_gifka[fps], res)
    if provershit % 300 == 0:
        fps = (fps + 1) % len(sama_gifka)
        provershit = 1
        pygame.display.flip()

def rin(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())

if store_btn:
    rin('store.py')
    store_btn = False
elif play_btn:
    import main
    play_btn = False
