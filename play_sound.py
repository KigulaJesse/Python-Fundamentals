import pygame

pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass  # Keeps the script running while the audio plays
