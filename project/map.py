import pygame
import os
import sys
from subprocess import Popen, run, call



pygame.init()
width = 1000
height = 563
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
provershit = open('csv_data/pole_nomer.csv', encoding='utf8').read()
provershit = int(provershit)
clock = pygame.time.Clock()
map_image = load_image('map.png')
nazad_v_menu = False
while running:
    screen.fill('white')
    screen.blit(map_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if 206 < int(event.pos[0]) < 412 and 152 < int(event.pos[1]) < 421:
                open('csv_data/slozhnost.csv', 'w').write('0')
                pygame.display.quit()
                call(['python', 'main.py'])
                terminate()
            elif 609 < int(event.pos[0]) < 812 and 152 < int(event.pos[1]) < 421:
                open('csv_data/slozhnost.csv', 'w').write('1')
                pygame.display.quit()
                call(['python', 'main.py'])
                terminate()


    clock.tick(fps)
    pygame.display.flip()
