import pygame
class Level:
    def __init__ (self, background_image_path, words, correct_word_index):
        self.background_image = pygame.image.load(background_image_path)
        self.words = words
        self.correct_word_index = correct_word_index
        self.score = 10