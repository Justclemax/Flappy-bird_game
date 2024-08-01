###############################
import pygame
from objects.background import Background
from  objects.floor import Floor
from objects.column import Column
from objects.bird import Bird
import assets
import configs

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

colmn_create_event = pygame.USEREVENT
clock = pygame.time.Clock()
runnning = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()


Background(0,sprites)
Background(1,sprites)
Floor(0,sprites)
Floor(1,sprites)

bird = Bird(sprites)


pygame.time.set_timer(colmn_create_event,1500)
game_over = False
while runnning:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            runnning = False
        if event.type == colmn_create_event:
            Column(sprites)
        bird.handle_event(event)
    screen.fill(0)

    sprites.draw(screen)
    if not game_over:
        sprites.update()

    if bird.check_collision(sprites):
        game_over =True


    pygame.display.flip()

    clock.tick(configs.FPS)

pygame.quit()
