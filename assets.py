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



audios = {}

def load_audios():
    path = os.path.join("assets", "audios")
    supported_formats = ('.wav', '.ogg')  # Formats d'audio supportés par pygame.mixer
    for file in os.listdir(path):
        try:
            # Vérifier si le fichier a une extension d'audio supportée
            if file.lower().endswith(supported_formats):
                sound = pygame.mixer.Sound(os.path.join(path, file))
                audios[file.split('.')[0]] = sound
            else:
                print(f"Format non pris en charge pour le fichier audio: {file}")
        except pygame.error as e:
            print(f"Erreur lors du chargement de l'audio {file}: {e}")

# Initialiser le module mixer de Pygame avant de charger les audios
pygame.mixer.init()

def play_audio(name):
    audios[name].play()