import pygame
import os
import sys

pygame.init()
width = 660
height = 450
size = width, height
screen = pygame.display.set_mode(size)

def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

running = True
x = 0
y = 0
scorost = 60
fps = 60
right = True
clock = pygame.time.Clock()
phon_image = load_image('castomize_for_store.png')
nazad_image = load_image('nazad_btn_store.png')
menu_izmeneniy_image = load_image('castomize_for_store_2.png')
nadpis_image = load_image('store_opisanie.png')
nazad_v_menu = False
while running:
    screen.fill('white')
    screen.blit(phon_image, (x, y))
    screen.blit(nazad_image, (570, 10))
    screen.blit(menu_izmeneniy_image, (100, 100))
    screen.blit(nadpis_image, (0, -10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if 571 < int(event.pos[0]) < 636 and 9 < int(event.pos[1]) < 75:
                running = False
                nazad_v_menu = True

    clock.tick(fps)
    pygame.display.flip()
if nazad_v_menu:
    import main_menu
    nazad_v_menu = False