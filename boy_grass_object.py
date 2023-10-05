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
    global balls
    global world
    world = []
    grass = Grass()
    balls = [Ball() for i in range(20)]
    team = [Boy() for i in range(11)]
    world.append(grass)
    world += team
    world += balls
    running = True


def render_world():
    clear_canvas()
    for object in world:
        object.draw()
    update_canvas()


def update_world():
    for object in world:
        object.update()

class Ball:
    def __init__(self):
        self.img = load_image('ball21x21.png') if random.randint(0,1) else load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 800), 599

    def draw(self):
        self.img.draw(self.x,self.y)

    def update(self):
        if(self.y <= self.img.h // 2 + 50):
            self.y = 50 + self.img.h // 2
            pass
        else:
            self.y -= random.randint(2,10)
class Grass:
    def __init__(self):
        self.img = load_image('grass.png')

    def draw(self):
        self.img.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
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
