from pico2d import *

open_canvas()
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
backgrounds = load_image('TUK_GROUND.png')
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')



running = True
frame = 0
x, y = 400,90
dir = 0
move_dir = 0
ANIM_ROW = 1


def handle_events():
    global running ,dir, move_dir,ANIM_ROW
    global x, y #전역좌표

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100  * 1 , 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)