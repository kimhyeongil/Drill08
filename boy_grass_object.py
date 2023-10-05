import random

from pico2d import *


# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    grass = Grass()
    team =[Boy() for i in range(11)]
    running = True


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()


def update_world():
    grass.update()
    for boy in team:
        boy.update()


class Grass:
    def __init__(self):
        self.img = load_image('grass.png')

    def draw(self):
        self.img.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.img = load_image('run_animation.png')

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.img.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
