from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 750
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet02.png')
character_stop = load_image('animation_sheet03.png')

def handle_events():
    global running, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT and dir_y == 0:
                dir_x = 1
            elif event.key == SDLK_LEFT and dir_y == 0:
                dir_x = -1
            elif event.key == SDLK_UP and dir_x == 0:
                dir_y = 1
            elif event.key == SDLK_DOWN and dir_x == 0:
                dir_y = -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x = 0
            elif event.key == SDLK_LEFT:
                dir_x = 0
            elif event.key == SDLK_UP:
                dir_y = 0
            elif event.key == SDLK_DOWN:
                dir_y = 0

def move_character():
    pass

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame, dir_x, dir_y = 0, 0, 0
while True:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    move_character()
    update_canvas()
    handle_events()
    x += dir_x * 10
    y += dir_y * 10
    delay(0.05)

close_canvas()
