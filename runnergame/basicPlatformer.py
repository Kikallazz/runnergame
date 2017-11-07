#! /usr/bin/python

import pygame
from pygame import *

WIN_WIDTH = 600
WIN_HEIGHT = 480
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30
charge = 0

# Sprites

# Load the sprite sheet
spritesheet =pygame.image.load("linksprite.png")

character = Surface((16, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-33, -3))
character = pygame.transform.scale(character, (16*2, 22*2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
standfront = stage

background = pygame.sprite.Sprite()
backgroundo = pygame.image.load('backgroundo.png')


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("hey now, ur a keemstar")
    timer = pygame.time.Clock()
    timer.tick(60)

    up = down = left = right = running = False
    bg = Surface((WIN_WIDTH, WIN_HEIGHT)).convert()
    entities = pygame.sprite.Group()
    player = Player(64, 64)
    platforms = []

    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                    P         P           P",
        "P                                          P",
        "P        IIP                               P",
        "P          P         I I  E  I I           P",
        "P          P                               P",
        "P          P                               P",
        "P    IIIIIIP                               P",
        "P                           PIIIIII        P",
        "P                           P              P",
        "P                                          P",
        "P                  II                      P",
        "P                    I                     P",
        "P         IIII         III                 P",
        "P       II    IIIIIIII                     P",
        "P                                    IIII  P",
        "P                                          P",
        "P                      IIII                P",
        "P                           II             P",
        "P                                   III    P",
        "P                                          P",
        "P                                          P",
        "PGGGGGGGGGGGGGGGGGGGGGGGGD O O B GGGGGGGGGGP",
        "PHHHHHHHHHHHHHHHHHHHHHHHHKKKKKKKKHHHHHHHHHHP",
        "PWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWP",]

    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = PlatformBlank(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "I":
                i = Platform(x, y)
                platforms.append(i)
                entities.add(i)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "G":
                g = GroundPlatform(x, y)
                platforms.append(g)
                entities.add(g)
            if col == "H":
                h = GroundPlatform2(x, y)
                platforms.append(h)
                entities.add(h)
            if col == "W":
                w = GroundPlatform3(x, y)
                platforms.append(w)
                entities.add(w)
            if col == "B":
                b = BridgePlatform(x, y)
                platforms.append(b)
                entities.add(b)
            if col == "D":
                d = BridgePlatform2(x, y)
                platforms.append(d)
                entities.add(d)
            if col == "K":
                k = WatterPlatform(x, y)
                platforms.append(k)
                entities.add(k)
            if col == "O":
                o = MidBridgePlatform(x, y)
                platforms.append(o)
                entities.add(o)
            x += 64
        y += 64
        x = 0

    total_level_width = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                raise(SystemExit, "QUIT")
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise(SystemExit, "ESCAPE")
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        # draw background

        # screen.blit(bg, (0, 0))
        screen.blit(backgroundo, (0, 0))

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)


def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                            # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)    # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t)  # stop scrolling at the bottom
    t = min(0, t)                            # stop scrolling at the top
    return Rect(l, t, w, h)


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32,32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self, up, down, left, right, running, platforms):
        global charge

        # print("touch")
        touchLeft = self.collide(-1, int(self.yvel), platforms)
        touchRight = self.collide(1, int(self.yvel), platforms)
        touchTop = self.collide(int(self.xvel), -1, platforms)
        touchBottom = self.collide(int(self.xvel), 1, platforms)
        touchBottomRange = self.collide(0, 30, platforms)
        self.onGround = self.collide(0, 1, platforms)

        # if not self.onGround:
        #    print("NOT ON GROUND")

        if up:  # only jump if on the ground
            if self.onGround:
                self.yvel -= 10
            if right and not touchBottomRange and not touchTop:
                if touchRight:
                    if up:
                        self.yvel = -10
                        self.xvel = -20
            elif left and not touchBottomRange and not touchTop:
                if touchLeft:
                    if up:
                        self.yvel = -10
                        self.xvel = 20
        if down:
            if self.onGround:
                charge += 0.25
                print(charge)
                if charge > 10:
                    charge = 10
                if up:
                    self.yvel = -10 - charge
                    charge = 0
        if not down:
            charge = 0
        if running:
            self.xvel = 8
        if left:
            self.xvel -= 1
            if touchLeft:
                self.yvel *= 0.9
        if right:
            self.xvel += 1
            if touchRight:
                self.yvel *= 0.9
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100:
                self.yvel = 100

        if abs(self.xvel) < 0.5:
            self.xvel = 0

        self.xvel *= 0.9
        
        # print("collision")
        if self.collide(int(self.xvel), 0, platforms):
            movex = 1 if self.xvel > 0 else -1
            while not self.collide(movex, 0, platforms):
                self.rect.left += movex
            self.xvel = 0

        self.rect.left += int(self.xvel)

        if self.collide(0, int(self.yvel), platforms):
            # print("START STOPPING", self.rect.top)
            movey = 1 if self.yvel > 0 else -1
            while not self.collide(0, movey, platforms):
                self.rect.top += movey
            # print("STOPPING", self.rect.top)
            self.yvel = 0

        self.rect.top += int(self.yvel)

    def collide(self, mx, my, platforms):
        coll = False
        self.rect.left += mx
        self.rect.top += my
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                coll = True
                break
            '''if self.rect.right == p.rect.left:
                print("collide right")
            if self.rect.left == p.rect.right:
                print("collide left")
            if self.rect.top == p.rect.bottom:
                print("collide top")
            if self.rect.bottom == p.rect.top:
                print("collide bottom")'''
        self.rect.left -= mx
        self.rect.top -= my
        return coll


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("platform.png")
        self.image.convert()
        self.image = pygame. transform.scale(self.image, (64, 64))
        self.rect = Rect(x, y, 64, 64)

    def update(self):
        pass


class PlatformBlank(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((64, 64))
        self.image.convert()
        self.image.fill(Color("#404040"))
        self.rect = Rect(x, y, 64, 64)

    def update(self):
        pass


class GroundPlatform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("ground.png")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = Rect(x, y, 64, 64)

    def update(self):
        pass


class GroundPlatform2(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("ground2.png")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = Rect(x, y, 64, 64)

    def update(self):
        pass


class GroundPlatform3(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("ground3.png")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = Rect(x, y, 64, 64)

    def update(self):
        pass


class BridgePlatform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("bridgo.png")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (128, 64))
        self.rect = Rect(x, y, 128, 64)

    def update(self):
        pass


class BridgePlatform2(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("bridgoreverse.png")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (128, 64))
        self.rect = Rect(x, y, 128, 64)

    def update(self):
        pass


class WatterPlatform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("watter.png")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = Rect(x, y, 64, 64)


class MidBridgePlatform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("bridge.png")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = Rect(x, y, 128, 64)

    def update(self):
        pass


class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))


if __name__ == "__main__":
    main()
