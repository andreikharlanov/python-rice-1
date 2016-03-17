# My version of RiceRocks game
# http://www.codeskulptor.org/#user41_b4nrSBkps4_17.py
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False
rocks = set([])
missiles = set([])

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def draw(self,canvas):
        if not self.thrust:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel

        # compute the forward vector pointing in the direction the ship is facing
        forward_vector = angle_to_vector(self.angle)

        # accelerate the ship in the direction of forward vector when the ship is thrusting
        if self.thrust:
            self.vel[0] += forward_vector[0] * 0.1
            self.vel[1] += forward_vector[1] * 0.1

        # make ship's position to wrap around the screen when the ship goes off the edge
        if self.pos[0] < 0:
            self.pos[0] = WIDTH
        elif self.pos[0] > WIDTH:
            self.pos[0] = 0
        elif self.pos[1] < 0:
            self.pos[1] = HEIGHT
        elif self.pos[1] > HEIGHT:
            self.pos[1] = 0

        # add friction
        self.vel[0] *= 0.997
        self.vel[1] *= 0.997

    def change_angle(self, new_angle_vel):
        self.angle_vel = new_angle_vel

    def turn_thrust_on(self, on_off):
        self.thrust = on_off

        if on_off == True:
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()

    def shoot(self):
        global a_missile

        # compute the forward vector pointing in the direction the ship is facing
        forward_vector = angle_to_vector(self.angle)

        # compute missile position
        missile_pos = [self.pos[0] + forward_vector[0] * 40,self.pos[1] + forward_vector[1] * 40]

        # compute missile velocity
        missile_vel = [self.vel[0] + forward_vector[0] * 3, self.vel[1] + forward_vector[1] * 3]

        new_missile = Sprite(missile_pos, missile_vel, 0, 0, missile_image, missile_info, missile_sound)

        missiles.add(new_missile)

    def get_radius(self):
        return self.radius

    def get_pos(self):
        return self.pos

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel

        self.age += 1

        # make sprite's position to wrap around the screen when the sprite goes off the edge
        if self.pos[0] < 0:
            self.pos[0] = WIDTH
        elif self.pos[0] > WIDTH:
            self.pos[0] = 0
        elif self.pos[1] < 0:
            self.pos[1] = HEIGHT
        elif self.pos[1] > HEIGHT:
            self.pos[1] = 0

    def get_radius(self):
        return self.radius

    def get_pos(self):
        return self.pos

    def collide(self, other_object):
        distance = math.sqrt((self.pos[0] - other_object.get_pos()[0]) ** 2 + (self.pos[1] - other_object.get_pos()[1]) ** 2)

        if distance <= (self.radius + other_object.get_radius()):
            return True
        else:
            return False

# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)

    if (not started) and inwidth and inheight:
        lives = 3
        score = 0
        started = True
        soundtrack.rewind()
        soundtrack.play()


def draw(canvas):
    global time, score, lives, started, rocks, missiles

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw and update ship
    my_ship.draw(canvas)
    my_ship.update()

    # draw and update sprite groups
    process_sprite_group(rocks, canvas)
    process_sprite_group(missiles, canvas)

    # check if ship collided with rocks
    if group_collide(rocks, my_ship):
        lives -= 1

    # check if missile collided with rocks, add score if collided
    for missile in missiles:
        if group_collide(rocks, missile):
            score += 10

    # draw scores and lives
    canvas.draw_text("You have " + str(lives) + " lives", (20, 30), 20, 'White')
    canvas.draw_text("Your score is: " + str(score), (650, 30), 20, 'White')

    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())

    # stop game is all lives are lost
    if lives == 0:
        rocks = set([])
        started = False

# sprite group processing helper
def process_sprite_group(group, canvas):
    group_copy = group.copy()

    for item in group_copy:
        item.draw(canvas)
        item.update()

        if item.age >= item.lifespan:
            group.discard(item)

# helper function to check collision of a group and a sprite
def group_collide(group, other_object):
    new_group = group.copy()
    collision = False

    for item in new_group:
        if item.collide(other_object) == True:
            collision = True
            group.discard(item)

    if collision:
        return True
    else:
        return False

# timer handler that spawns a rock
def rock_spawner():
    global rocks, started, WIDTH, HEIGHT

    # generate random position for a sprite
    pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]

    # generate random velocity for a sprite
    vel = [random.randrange(40, 200) / 100.0 * random.choice([1, -1]), random.randrange(40, 200) / 100.0 * random.choice([1, -1])]

    # generate random angular velocity for a sprite
    ang_vel = random.randrange(5, 10) / 100.0 * random.choice([1, -1])

    new_rock = Sprite(pos, vel, 0, ang_vel, asteroid_image, asteroid_info)

    if started and len(rocks) < 12:
        rocks.add(new_rock)

# keyboard handler
def keydown(key):
    if key == simplegui.KEY_MAP['right']:
        my_ship.change_angle(0.2)
    elif key == simplegui.KEY_MAP['left']:
        my_ship.change_angle(-0.2)
    elif key == simplegui.KEY_MAP['up']:
        my_ship.turn_thrust_on(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()


def keyup(key):
    if key == simplegui.KEY_MAP['right']:
        my_ship.change_angle(0)
    elif key == simplegui.KEY_MAP['left']:
        my_ship.change_angle(0)
    elif key == simplegui.KEY_MAP['up']:
        my_ship.turn_thrust_on(False)

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

# register handlers
frame.set_draw_handler(draw)

frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
