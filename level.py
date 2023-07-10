import pygame
class Level:
    def __init__ (self, background_image_path, words, correct_word, dialogue, character):
        self.background_image = pygame.image.load(background_image_path)
        self.words = words
        self.correct_word = correct_word
        self.score = 10
        self.dialogue = dialogue
        self.character = character
        self.is_complete = False