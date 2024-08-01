import pygame
import assets
import configs


class Column(pygame.sprite.Sprite):

    def __init__(self, *groups):
        self.gap = 100

        self.sprite = assets.get_sprite("pipe-green")
        self.sprite_rect = self.sprite.get_rect()

        self.pipe_bottom = self.sprite
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(0,0))

        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(-100,0))

        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height*2 + self.gap))
        self.image.fill("cyan")
        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)
        self.image.blit(self.pipe_top, self.pipe_top_rect)

        self.rect = self.image.get_rect(topleft=(0, 0))

        super().__init__(*groups)

    #def update(self):
     #   self.rect.x -= 1
      #  if self.rect.right <= 0:
       #     self.rect.x = configs.SCREEN_WIDTH
