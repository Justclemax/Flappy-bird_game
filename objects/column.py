import random

import pygame
import assets
import configs


class Column(pygame.sprite.Sprite):

    def __init__(self, *groups):
        self.gap = 100

        self.sprite = assets.get_sprite("pipe-green")
        self.sprite_rect = self.sprite.get_rect()

        self.pipe_bottom = self.sprite
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(0,self.sprite_rect.height + self.gap))

        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(0,5))

        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height*2 + self.gap),
                                            pygame.SRCALPHA)

        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)
        self.image.blit(self.pipe_top, self.pipe_top_rect)
        self
        sprite_floor_height = assets.get_sprite("floor2").get_rect().height

        min_y = 80
        max_y = configs.SCREEN_HEIGHT- sprite_floor_height


        self.rect = self.image.get_rect(midleft=(configs.SCREEN_WIDTH, random.uniform(min_y, max_y)))

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 3
        if self.rect.right <= 0:
            self.kill()
