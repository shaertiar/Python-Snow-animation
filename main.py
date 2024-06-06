# Такое чувство, словно код написал кто-то другой, хотя я точно помню, как писал его самостоятельно. Кажеться, я исправил некоторые косяки, которые я оставил.


import pygame as pg
import random

pg.init()

# Settings
bg_color = (0, 0, 0)

speed = 200

change_mouse_cursor = False
mouse_cursor_form = random.choice(['rect', 'circle'])
mouse_cursor_size = 10
mouse_cursor_color = (255, 0, 0)

# Create window
window = pg.display.set_mode()
pg.display.set_caption('Snow animation')
WW, WH = window.get_size()

if change_mouse_cursor:
    pg.mouse.set_visible(False)

# Variables
Clock = pg.time.Clock()

snowflakes_num = WW * WH // 2000

snowflakes_list = []

# Create and add snowflakes in list
for i in range(snowflakes_num):
    x = random.randrange(0, WW)
    y = random.randrange(0, WH)

    snowflakes_list.append([x, y])

# Main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    window.fill(bg_color)

    for i in range(len(snowflakes_list)):
        pg.draw.circle(window, (255, 255, 255), snowflakes_list[i], 2)

        snowflakes_list[i][1] += 1

        if snowflakes_list[i][1] > WH:
            snowflakes_list[i][0] = random.randrange(0, WW)
            snowflakes_list[i][1] = random.randrange(-50, 10)

    if change_mouse_cursor:
        mouse_pos = pg.mouse.get_pos()
        
        if mouse_cursor_form == 'circle':
            pg.draw.circle(window, mouse_cursor_color, mouse_pos, mouse_cursor_size//2)

        elif mouse_cursor_form == 'rect':
            pg.draw.rect(window, mouse_cursor_color, (mouse_pos[0] - mouse_cursor_size/2, mouse_pos[1] - mouse_cursor_size/2, mouse_cursor_size, mouse_cursor_size))


    pg.display.update()
    # del Ненавижу когда скорость регулироют частотой кадра
    Clock.tick(speed)