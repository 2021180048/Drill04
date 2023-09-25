from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 750
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet02.png')
character_stop = load_image('animation_sheet03.png')

def handle_events():
    pass

def move_character():
    pass

while True:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    move_character()
    update_canvas()
    handle_events()
    delay(0.05)
close_canvas()
