###############################
import pygame
from objects.background import Background
from  objects.floor import Floor
from objects.column import Column
from objects.bird import Bird
from objects.game_start_message import GameStartMessage
from objects.game_over_message import GameOverMessage
import assets
import configs

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

colmn_create_event = pygame.USEREVENT
clock = pygame.time.Clock()

runnning = True
game_over = False
score = 0
game_start =False
assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

def create_sprites():
    Background(0,sprites)
    Background(1,sprites)
    Floor(0,sprites)
    Floor(1,sprites)
    return  Bird(sprites),GameStartMessage(sprites)

bird,game_started_message  = create_sprites()


#game_over_message =GameOverMessage(sprites)


pygame.time.set_timer(colmn_create_event,1500)


while runnning:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            runnning = False
        if event.type == colmn_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_start and not  game_over:
                game_start = True
                game_started_message.kill()
            if event.key == pygame.K_ESCAPE and game_over:
                #create_sprites()
                game_over = False
                game_start =False
                sprites.empty()
                bird, game_started_message = create_sprites()


        bird.handle_event(event)
    screen.fill(0)

    sprites.draw(screen)
    if game_start and not game_over:
        sprites.update()

    if bird.check_collision(sprites):
        game_over =True
        game_start = False
        GameOverMessage(sprites)

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score +=1
    print(score)
    pygame.display.flip()

    clock.tick(configs.FPS)

pygame.quit()
