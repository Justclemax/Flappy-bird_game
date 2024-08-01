import pygame
import assets
import configs
from layer import Layer

class Floor(pygame.sprite.Sprite):

    def __init__(self, index, *groups):
        self._layer = Layer.FLOOR
        self.image = assets.get_sprite("floor2")

        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 450))

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
