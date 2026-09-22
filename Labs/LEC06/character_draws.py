# 실습 과제 진행

from pico2d import *

open_canvas()

character = load_image('character.png')

def draw_circle():
    print('CIRCLE')
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    pass

def draw_rectangle():
    print('RECTANGLE')
    pass    

def draw_triangle():
    print('TRIANGLE')
    pass


while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()
    pass

close_canvas()
