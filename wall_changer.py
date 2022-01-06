import pygame
import os
import sys

pygame.init()
width = 800
height = 697
size = width, height
screen = pygame.display.set_mode(size)

def terminate():
    # выход
    pygame.quit()
    sys.exit()

def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

running = True
scorost = 60
fps = 60
right = True
provershit = open('wall_nomer.csv', encoding='utf8').read()
provershit = int(provershit)
clock = pygame.time.Clock()
phon_image = load_image('background.png')
wall1_image = load_image('big_wall.png')
wall2_image = load_image('big_wall2.png')
wall3_image = load_image('big_wall3.png')
wall4_image = load_image('big_wall4.png')
accept_btn = load_image('accept_btn.png')
strelka = load_image('strelka.png')
nazad_v_menu = False
while running:
    screen.fill('white')
    screen.blit(phon_image, (0, 0))
    screen.blit(accept_btn, (145, 580))
    screen.blit(strelka, (650, 280))
    if not provershit:
        screen.blit(wall1_image, (300, 25))
    if provershit == 1:
        screen.blit(wall2_image, (300, 25))
    if provershit == 2:
        screen.blit(wall3_image, (300, 25))
    if provershit == 3:
        screen.blit(wall4_image, (300, 25))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if 665 < int(event.pos[0]) < 725 and 286 < int(event.pos[1]) < 316:
                provershit = int(provershit) + 1
                if provershit == 4:
                    provershit = 0
            if 144 < int(event.pos[0]) < 561 and 580 < int(event.pos[1]) < 654:
                open('wall_nomer.csv', 'w').write(str(provershit))
                running = False
                nazad_v_menu = True

    clock.tick(fps)
    pygame.display.flip()
if nazad_v_menu:
    exec(open("main_menu.py").read())
    nazad_v_menu = False