from pygame import *
import pygame
import random
pygame.init()


# Load the sprite sheet
spritesheet = pygame.image.load("linksprite.png")

character = Surface((19, 23), pygame.SRCALPHA)
character.blit(spritesheet, (-331, -23))
character = pygame.transform.scale(character, (19 * 2, 23 * 2))
stage = Surface((38, 46), pygame.SRCALPHA)
stage.blit(character, (0, 0))
standright = stage

character = Surface((19, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-241, -122))
character = pygame.transform.scale(character, (19 * 2, 24 * 2))
stage = Surface((38, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runright1 = stage

character = Surface((18, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-272, -122))
character = pygame.transform.scale(character, (18 * 2, 24 * 2))
stage = Surface((36, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runright2 = stage

character = Surface((19, 23), pygame.SRCALPHA)
character.blit(spritesheet, (-301, -122))
character = pygame.transform.scale(character, (19 * 2, 23 * 2))
stage = Surface((38, 46), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runright3 = stage

character = Surface((19, 23), pygame.SRCALPHA)
character.blit(spritesheet, (-331, -122))
character = pygame.transform.scale(character, (19 * 2, 23 * 2))
stage = Surface((38, 46), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runright4 = stage

character = Surface((19, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-361, -122))
character = pygame.transform.scale(character, (19 * 2, 24 * 2))
stage = Surface((38, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runright5 = stage

character = Surface((18, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-392, -122))
character = pygame.transform.scale(character, (18 * 2, 24 * 2))
stage = Surface((36, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runright6 = stage

walkloopright = [standright, runright1, runright2, runright3, runright4, runright5, runright6]

character = Surface((19, 23), pygame.SRCALPHA)
character.blit(spritesheet, (-151, -2))
character = pygame.transform.scale(character, (19 * 2, 23 * 2))
stage = Surface((38, 46), pygame.SRCALPHA)
stage.blit(character, (0, 0))
standleft = stage

character = Surface((19, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-241, -32))
character = pygame.transform.scale(character, (19 * 2, 24 * 2))
stage = Surface((38, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runleft1 = stage

character = Surface((18, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-272, -32))
character = pygame.transform.scale(character, (18 * 2, 24 * 2))
stage = Surface((36, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runleft2 = stage

character = Surface((19, 23), pygame.SRCALPHA)
character.blit(spritesheet, (-301, -32))
character = pygame.transform.scale(character, (19 * 2, 23 * 2))
stage = Surface((38, 46), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runleft3 = stage

character = Surface((19, 23), pygame.SRCALPHA)
character.blit(spritesheet, (-331, -32))
character = pygame.transform.scale(character, (19 * 2, 23 * 2))
stage = Surface((38, 46), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runleft4 = stage

character = Surface((19, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-361, -32))
character = pygame.transform.scale(character, (19 * 2, 24 * 2))
stage = Surface((38, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runleft5 = stage

character = Surface((18, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-392, -32))
character = pygame.transform.scale(character, (18 * 2, 24 * 2))
stage = Surface((36, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
runleft6 = stage

walkloopleft = [standleft, runleft1, runleft2, runleft3, runleft4, runleft5, runleft6]

character = Surface((16, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-33, -3))
character = pygame.transform.scale(character, (16 * 2, 22 * 2))
stage = Surface((32, 44), pygame.SRCALPHA)
stage.blit(character, (0, 0))
fallright = stage

character = Surface((16, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-33, -3))
character = pygame.transform.scale(character, (16 * 2, 22 * 2))
stage = Surface((32, 44), pygame.SRCALPHA)
stage.blit(character, (0, 0))
fallleft = stage

character = Surface((19, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-391, -63))
character = pygame.transform.scale(character, (19 * 2, 22 * 2))
stage = Surface((38, 44), pygame.SRCALPHA)
stage.blit(character, (0, 0))
walljumpleft = stage

character = Surface((19, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-391, -153))
character = pygame.transform.scale(character, (19 * 2, 22 * 2))
stage = Surface((38, 44), pygame.SRCALPHA)
stage.blit(character, (0, 0))
walljumpright = stage

# Attacking frames

character = Surface((18, 23), pygame.SRCALPHA)
character.blit(spritesheet, (-242, -92))
character = pygame.transform.scale(character, (18 * 2, 23 * 2))
stage = Surface((36, 46), pygame.SRCALPHA)
stage.blit(character, (0, 0))
attack1 = stage

character = Surface((26, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-268, -92))
character = pygame.transform.scale(character, (26 * 2, 24 * 2))
stage = Surface((52, 48), pygame.SRCALPHA)
stage.blit(character, (0, 0))
attack2 = stage

character = Surface((31, 21), pygame.SRCALPHA)
character.blit(spritesheet, (-295, -93))
character = pygame.transform.scale(character, (31 * 2, 21 * 2))
stage = Surface((62, 42), pygame.SRCALPHA)
stage.blit(character, (0, 0))
attack3 = stage

character = Surface((28, 21), pygame.SRCALPHA)
character.blit(spritesheet, (-327, -93))
character = pygame.transform.scale(character, (28 * 2, 21 * 2))
stage = Surface((56, 42), pygame.SRCALPHA)
stage.blit(character, (0, 0))
attack4 = stage

character = Surface((23, 31), pygame.SRCALPHA)
character.blit(spritesheet, (-359, -88))
character = pygame.transform.scale(character, (23 * 2, 31 * 2))
stage = Surface((46, 62), pygame.SRCALPHA)
stage.blit(character, (0, 0))
attack5 = stage

attackloopleft = [standleft, attack1, attack2, attack3, attack4, attack5]

# End Sprites


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Player(Entity):
    def __init__(self, x, y, right, left):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.faceRight = True
        self.onWallRight = False
        self.onWallLeft = False
        self.image = Surface((32, 32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

        self.attacking = False
        self.running = False
        self.left = left
        self.right = right

        self.walkcounter = 0
        self.standcounter = 0
        self.attackcounter = 0
        self.moving = False

    def update(self, up, down, left, right, running, space, platforms):
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
        if right and not touchBottomRange and not touchTop and touchRight:
            self.onWallRight = True
        elif left and not touchBottomRange and not touchTop and touchLeft:
            self.onWallLeft = True
        if not touchRight:
            self.onWallRight = False
        if not touchLeft:
            self.onWallLeft = False
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
            self.running = True
        if not running:
            self.running = False
        if left:
            self.xvel -= 1
            if touchLeft:
                self.yvel *= 0.9
            self.faceRight = False
            self.running = True
        if right:
            self.xvel += 1
            if touchRight:
                self.yvel *= 0.9
            self.faceRight = True
            self.running = True
        if space:
            self.attacking = True
            print("space")
        if not space:
            self.attacking = False
            print("not space")
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100:
                self.yvel = 100
            self.running = False
            self.walkcounter = 5

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

        self.animate()
        if not self.attacking:
            self.walkcounter += 1
            self.attackcounter = 0
        if self.attacking:
            self.attackcounter += 1

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

    def animate(self):
        state = []
        state.append(self.onGround)
        state.append(self.running)
        state.append(self.faceRight)
        state.append(self.onWallLeft)
        state.append(self.onWallRight)
        state.append(self.attacking)

        if self.attacking:
            self.moving = False
        else:
            if not self.onGround:
                self.moving = True
                self.standcounter = 0
            if self.xvel > 0:
                self.moving = True
                self.standcounter = 0
            if self.xvel < 0:
                self.moving = True
                self.standcounter = 0
            if self.xvel == 0:
                self.moving = True

        if state[0]:
            if state[1]:
                if not state[2]:
                    self.walkloop(walkloopleft)
                elif state[2]:
                    self.walkloop(walkloopright)
            elif not state[1]:
                if state[5] and not state[2]:
                    self.attackloop(attackloopleft)
                elif not state[2]:
                    self.updatecharacter(runleft2)
                elif state[2]:
                    self.updatecharacter(runright2)
        if not state[0]:
            if not state[1]:
                if not state[2]:
                    self.updatecharacter(runleft2)
                elif state[2]:
                    self.updatecharacter(runright2)
                if state[3]:
                    self.updatecharacter(walljumpleft)
                if state[4]:
                    self.updatecharacter(walljumpright)
            if state[1]:
                if not state[2]:
                    self.updatecharacter(standleft)
                elif state[2]:
                    self.updatecharacter(standright)

        if not self.moving and not self.attacking:
            print(self.standcounter)
            self.standcounter += 1
            if self.standcounter >= 50:
                if self.faceRight:
                    self.updatecharacter(standright)
                elif not self.faceRight:
                    self.updatecharacter(standleft)

    def walkloop(self, loop):
        if self.walkcounter == 0 or self.walkcounter == 1:
            self.standcounter = 0
            self.updatecharacter(loop[0])
        elif self.walkcounter == 5:
            self.updatecharacter(loop[1])
        elif self.walkcounter == 10:
            self.updatecharacter(loop[2])
        elif self.walkcounter == 15:
            self.updatecharacter(loop[3])
        elif self.walkcounter == 20:
            self.updatecharacter(loop[4])
        elif self.walkcounter == 25:
            self.updatecharacter(loop[5])
        elif self.walkcounter == 30:
            self.updatecharacter(loop[6])
        elif self.walkcounter == 35:
            self.updatecharacter(loop[5])
        elif self.walkcounter == 40:
            self.updatecharacter(loop[4])
        elif self.walkcounter == 45:
            self.updatecharacter(loop[3])
        elif self.walkcounter == 50:
            self.updatecharacter(loop[2])
        elif self.walkcounter == 55:
            self.updatecharacter(loop[1])
            self.walkcounter = 5
        # self.walkcounter = self.walkcounter + 1

    def attackloop(self, loop):
        if self.attackcounter == 0 or self.attackcounter == 1:
            self.standcounter = 0
            self.updatecharacter(loop[0])
        elif self.attackcounter == 10:
            self.updatecharacter(loop[1])
        elif self.attackcounter == 15:
            self.updatecharacter(loop[2])
        elif self.attackcounter == 20:
            self.updatecharacter(loop[3])
        elif self.attackcounter == 25:
            self.updatecharacter(loop[4])
        elif self.attackcounter == 30:
            self.updatecharacter(loop[5])
        elif self.attackcounter == 35:
            self.updatecharacter(loop[0])
            self.attackcounter = 5

    def updatecharacter(self, ansurf):
        self.image = ansurf


class Enemy(Entity):
    def __init__(self, x, y, right, left):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.faceRight = True
        self.onWallRight = False
        self.onWallLeft = False
        self.image = Surface((32, 32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)
        self.left = left
        self.right = right
        self.moveleft = True
        self.moveright = False
        self.counter = 15
        self.roll = random.randint(1, 10)

    def update(self, left, right, platforms):
        global charge
        if self.counter % 15 == 0:
            self.roll = random.randint(1, 10)

        # print("touch")
        touchLeft = self.collide(-1, int(self.yvel), platforms)
        touchRight = self.collide(1, int(self.yvel), platforms)
        touchTop = self.collide(int(self.xvel), -1, platforms)
        touchBottom = self.collide(int(self.xvel), 1, platforms)
        touchBottomRange = self.collide(0, 30, platforms)
        self.onGround = self.collide(0, 1, platforms)

        # if not self.onGround:
        #    print("NOT ON GROUND")

        if self.onGround and self.roll == 5:
            self.yvel -= 10
        if touchLeft:
            self.moveleft = False
            self.moveright = True
            self.xvel = 4
        if touchRight:
            self.moveright = False
            self.moveleft = True
        if self.moveleft:
            self.xvel = -4
        if self.moveright and self.onGround:
            self.xvel = 4
        if left:
            self.xvel -= 1
            if touchLeft:
                self.yvel *= 0.9
            self.faceRight = False
        if right:
            self.xvel += 1
            if touchRight:
                self.yvel *= 0.9
            self.faceRight = True
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100:
                self.yvel = 100

        if abs(self.xvel) < 0.5:
            self.xvel = 0

        self.xvel *= 0.9
        if Player.rect.left >= self.rect.left:
            self.xvel = 5
        elif Player.rect.left <= self.rect.left:
            self.xvel = -5


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

        self.counter += 1

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

    '''def animate(self):
        state = []
        state.append(self.onGround)
        state.append(self.running)
        state.append(self.faceRight)
        state.append(self.onWallLeft)
        state.append(self.onWallRight)
        state.append(self.attacking)

        if self.attacking:
            self.moving = False
        else:
            if not self.onGround:
                self.moving = True
                self.standcounter = 0
            if self.xvel > 0:
                self.moving = True
                self.standcounter = 0
            if self.xvel < 0:
                self.moving = True
                self.standcounter = 0
            if self.xvel == 0:
                self.moving = True

        if state[0]:
            if state[1]:
                if not state[2]:
                    self.walkloop(walkloopleft)
                elif state[2]:
                    self.walkloop(walkloopright)
            elif not state[1]:
                if state[5] and not state[2]:
                    self.attackloop(attackloopleft)
                elif not state[2]:
                    self.updatecharacter(runleft2)
                elif state[2]:
                    self.updatecharacter(runright2)
        if not state[0]:
            if not state[1]:
                if not state[2]:
                    self.updatecharacter(runleft2)
                elif state[2]:
                    self.updatecharacter(runright2)
                if state[3]:
                    self.updatecharacter(walljumpleft)
                if state[4]:
                    self.updatecharacter(walljumpright)
            if state[1]:
                if not state[2]:
                    self.updatecharacter(standleft)
                elif state[2]:
                    self.updatecharacter(standright)

        if not self.moving and not self.attacking:
            print(self.standcounter)
            self.standcounter += 1
            if self.standcounter >= 50:
                if self.faceRight:
                    self.updatecharacter(standright)
                elif not self.faceRight:
                    self.updatecharacter(standleft)

    def walkloop(self, loop):
        if self.walkcounter == 0 or self.walkcounter == 1:
            self.standcounter = 0
            self.updatecharacter(loop[0])
        elif self.walkcounter == 5:
            self.updatecharacter(loop[1])
        elif self.walkcounter == 10:
            self.updatecharacter(loop[2])
        elif self.walkcounter == 15:
            self.updatecharacter(loop[3])
        elif self.walkcounter == 20:
            self.updatecharacter(loop[4])
        elif self.walkcounter == 25:
            self.updatecharacter(loop[5])
        elif self.walkcounter == 30:
            self.updatecharacter(loop[6])
        elif self.walkcounter == 35:
            self.updatecharacter(loop[5])
        elif self.walkcounter == 40:
            self.updatecharacter(loop[4])
        elif self.walkcounter == 45:
            self.updatecharacter(loop[3])
        elif self.walkcounter == 50:
            self.updatecharacter(loop[2])
        elif self.walkcounter == 55:
            self.updatecharacter(loop[1])
            self.walkcounter = 5
        # self.walkcounter = self.walkcounter + 1

    def attackloop(self, loop):
        if self.attackcounter == 0 or self.attackcounter == 1:
            self.standcounter = 0
            self.updatecharacter(loop[0])
        elif self.attackcounter == 10:
            self.updatecharacter(loop[1])
        elif self.attackcounter == 15:
            self.updatecharacter(loop[2])
        elif self.attackcounter == 20:
            self.updatecharacter(loop[3])
        elif self.attackcounter == 25:
            self.updatecharacter(loop[4])
        elif self.attackcounter == 30:
            self.updatecharacter(loop[5])
        elif self.attackcounter == 35:
            self.updatecharacter(loop[0])
            self.attackcounter = 5

    def updatecharacter(self, ansurf):
        self.image = ansurf'''


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("platform.png")
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
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
