from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
backgrounds = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running
    global  x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.ky == SDLK_ESCAPE:
            running = False


open_canvas()