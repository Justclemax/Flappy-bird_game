###############################
import pygame
from objects.background import Background
from  objects.floor import Floor
from objects.column import Column
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

Column(sprites)

pygame.time.set_timer(colmn_create_event,1500)

while runnning:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            runnning = False
        if event.type == colmn_create_event:
            Column(sprites)
    screen.fill('pink')

    sprites.draw(screen)
    sprites.update()

    pygame.display.flip()

    clock.tick(configs.FPS)

pygame.quit()
