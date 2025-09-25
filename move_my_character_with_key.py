from pico2d import *

open_canvas()
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
backgrounds = load_image('TUK_GROUND.png')
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

CHAR_SIZE = 50 # 메인루프 설정
SPEED = 5 # 속도 설정

running = True
frame = 0
x, y = 400,90
dir = 0
move_dir = 0
ANIM_ROW = 100



def handle_events():
    global running ,dir, move_dir,ANIM_ROW
    global x, y #전역좌표

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir = 1; move_dir = 1; ANIM_ROW = 100
            elif event.key == SDLK_LEFT:
                dir = 1; move_dir = -1; ANIM_ROW = 0
            elif event.key == SDLK_UP:
                dir = 1; move_dir = 2; ANIM_ROW = 200
            elif event.key == SDLK_DOWN:
                dir = 1; move_dir = -2; ANIM_ROW = 300


        elif event.type == SDL_KEYUP:
            if (event.key == SDLK_RIGHT and move_dir == 1) or \
                    (event.key == SDLK_LEFT and move_dir == -1) or \
                    (event.key == SDLK_UP and move_dir == 2) or \
                    (event.key == SDLK_DOWN and move_dir == -2):
                dir = 0

while running:
    clear_canvas()



    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)