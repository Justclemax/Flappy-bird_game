import pygame
import os

sprites = {}

def load_sprites():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        try:
            # Vérifier si le fichier a une extension d'image supportée
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))
            else:
                print(f"Format non pris en charge pour le fichier: {file}")
        except pygame.error as e:
            print(f"Erreur lors du chargement de l'image {file}: {e}")

def get_sprite(name:str):
    return sprites[name]