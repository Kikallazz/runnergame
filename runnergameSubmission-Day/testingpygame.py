import random
import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

hero = pygame.sprite.Sprite()
hero.image = pygame.image.load('spriteguyc.png')
hero.rect = hero.image.get_rect()
hero_group = pygame.sprite.GroupSingle(hero)

TILE_SIZE = 10  # This makes each frame 10x10px
NUM_TILES_WIDTH = 128
NUM_TILES_HEIGHT = 80

munch_sounda = pygame.mixer.Sound('noma.wav')  # Just a few sounds for the sprite eating the candy
munch_soundb = pygame.mixer.Sound('nomb.wav')  # "                                               "
munch_soundc = pygame.mixer.Sound('nomc.wav')  # "                                               "

candies = pygame.sprite.OrderedUpdates()


def add_candy(candies):  # This is the function I use to spawn the candies onto the screen
    candy = pygame.sprite.Sprite()
    candy.image = pygame.image.load('candy.png')
    candy.rect = candy.image.get_rect()
    candy.rect.left = random.randint(10, int(NUM_TILES_WIDTH) - 10) * int(TILE_SIZE)
    candy.rect.top = random.randint(10, int(NUM_TILES_HEIGHT) - 10) * int(TILE_SIZE)
    candies.add(candy)


for i in range(10):
    add_candy(candies)

iteration = 0

heropos = 0
heroposa = 0

held = []  # This is the list that will hold all of the keys that are being pressed, every time the main loop iterates
# it reads through and checks what "movements" there are and does them.
finish = False  # Main loop
win = False  # Keeps the game running and candy spawning while false
score = 0  # Setting the score variable, will be raised in intervals of 50, 50 per candy collected, will be replaced
# gold, the same basic thing will be used for exp and stuff

clock = pygame.time.Clock()
clock.tick(120)

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        if event.type == pygame.KEYDOWN:
            held.append(event.key)  # This is the held list being appended with whatever key is being held
        elif event.type == pygame.KEYUP:
            held.remove(event.key)  # "                                                                  "
        if event.type == pygame.USEREVENT:
            if not win:  # This is just seeing if the game is not over, otherwise it keeps adding candies once you win
                add_candy(candies)
    screen.fill((50, 50, 50))  # This is to avoid the hero leaving a trail
    # update hero position
    if pygame.K_UP in held:  # This checks if the UP arrow key is in the held list
        hero.rect.top -= TILE_SIZE  # This takes the amount of times that the UP arrow key is in the list and moves the
        # sprite that many times
        heroposa = hero.rect.top
    if pygame.K_DOWN in held:  # This checks if the DOWN arrow key is in the held list
        hero.rect.top += TILE_SIZE  # This takes the amount of times that the DOWN arrow key is in the list and moves
        # the sprite that many times
        heroposa = hero.rect.top
    if pygame.K_RIGHT in held:  # This checks if the RIGHT arrow key is in the the held list
        hero.rect.right += TILE_SIZE  # This takes the amount of times that the RIGHT arrow key is in the list and moves
        # the sprite that many times
        heropos = hero.rect.right
        heroposa = hero.rect.top
        hero = pygame.sprite.Sprite()
        hero.image = pygame.image.load('spriteguyc.png')
        hero.rect = hero.image.get_rect()
        hero_group = pygame.sprite.GroupSingle(hero)
        hero.rect.right = heropos
        hero.rect.top = heroposa
    if pygame.K_LEFT in held:  # This checks if the LEFT arrow key is in the held list
        hero.rect.right -= TILE_SIZE  # This takes the amount of times that the LEFT arrow key is in the list and moves
        # the sprite that many times
        heropos = hero.rect.right
        heroposa = hero.rect.top
        hero = pygame.sprite.Sprite()
        hero.image = pygame.image.load('spriteguyd.png')
        hero.rect = hero.image.get_rect()
        hero_group = pygame.sprite.GroupSingle(hero)
        hero.rect.right = heropos
        hero.rect.top = heroposa
    hero.rect.clamp_ip(screen.get_rect())  # This keeps the sprite from moving outside of the screen
    hero_group.draw(screen)  # This draws the objects in the "hero_group" to the "screen"
    if not win:  # This checks that the game is not over
        if iteration % 50 == 0:  # This is just a steady rate of spawning candies, not too fast, not too slow
            add_candy(candies)
    candies.draw(screen)
    collides = pygame.sprite.groupcollide(hero_group, candies, False, True)  # So when the sprite and the candies
    # collide the candies disappear
    if len(collides) > 0:  # This checks if the length of the value of collides is greater than 0, if it is, then a
        # collision has occurred
        score += 50  # This is the score, it is raised in lots of 50
    roll = random.randint(0, 2)  # This rolls between 3 values, 0, 1 and 2, this is used to determine the "munch" sound
    if roll == 0:
        if len(collides) > 0:
            munch_sounda.play()  # The sfx for eating the candy, variant a
    elif roll == 1:
        if len(collides) > 0:
            munch_soundb.play()  # The sfx for eating the candy, variant b
    elif roll == 2:
        if len(collides) > 0:
            munch_soundc.play()  # The sfx for eating the candy, variant c
    pygame.sprite.groupcollide(hero_group, candies, False, True)
    if len(candies) == 0:
        win = True  # Making this true, makes the candies stop spawning
    if win:  # Again, checks if "win" is true
        text_score = str(score) + " points"  # This one is just making the score into a string and then formatting it
        # how I want it
        font = pygame.font.Font(None, 36)
        text_image = font.render("You Win!   " + text_score, True, (255, 255, 255))
        text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
        screen.blit(text_image, text_rect)
    if not win:  # While the game is going
        text_score = str(score) + " points"  # same as before
        score_font = pygame.font.Font(None, 30)
        score_image = score_font.render(text_score, True, (255, 255, 255))
        score_rect = score_image.get_rect(centerx=100, centery=100)
        screen.blit(score_image, score_rect)
    pygame.display.update()  # Updates the screen with all the new changes
    iteration += 1  # This is for the candy spawning
pygame.quit()
