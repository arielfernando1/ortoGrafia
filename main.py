import math
import random
import pygame
import levels
import settings


class Game:
    def __init__(self, sw, sh):
        pygame.init()
        pygame.display.set_caption("ORTOGRAFIA")
        # levels
        self.levels = levels.levels
        self.current_level = 0
        self.level = self.levels[self.current_level]
        self.words = self.level.words
        # Randomize words
        random.shuffle(self.words)
        self.selected_word = 0
        self.text_visible = True
        # global settings
        self.screen_width = sw
        self.screen_height = sh
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.font_file = settings.FONT_FILE
        self.font_game_size = settings.FONT_GAME_SIZE
        self.font_score_size = settings.FONT_SCORE_SIZE
        self.font_score = pygame.font.Font(
            self.font_file, self.font_score_size)
        self.font_game = pygame.font.Font(self.font_file, self.font_game_size)
        self.bar_color = settings.COLOR_BAR
        self.heart_color = settings.COLOR_HEART
        self.word_color = settings.COLOR_WORD
        self.game_over_color = settings.COLOR_GAME_OVER
        # self.background_image = pygame.image.load(
        #     "assets/backrounds/bakeryBG.png")
        # self.background_image = pygame.transform.scale(
        #     self.level.background_image, (self.screen_width, self.screen_height))
        # game stats
        self.score = self.level.score
        self.lives = 3
        # Words
        # self.words = ["Hay", "Ahi", "Ay!"]
        # self.offensive_gameover_words = ["Vuele a la escuela", "JA JA. No sabe escribir", "JAJAJA. No sabe escribir"]
        # self.selected_word = 1
        self.selected_word_color = (255, 255, 255)
        self.selected_word_size = 76
        # Sounds
        self.select_word_sound = pygame.mixer.Sound(settings.SOUND_CLICK)
        self.correct_word_sound = pygame.mixer.Sound(settings.SOUND_CORRECT)
        self.incorrect_word_sound = pygame.mixer.Sound(
            settings.SOUND_INCORRECT)
        self.game_over_sound = pygame.mixer.Sound(settings.SOUND_GAME_OVER)
        # Characters
        self.character_image = self.level.character
        self.character_rect = self.character_image.get_rect(
            center=(self.screen_width/2, self.screen_height/2))
        # define the dialog message and its position
        self.dialog_font_size = 32
        self.dialog_font = pygame.font.Font(
            self.font_file, self.dialog_font_size)
        self.dialog_message = self.level.dialogue
        self.dialog_x = self.character_rect.centerx
        self.dialog_y = self.character_rect.bottom + 10

        self.heart_image = pygame.image.load("assets/backrounds/heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (50, 50))
        self.heart_rect = self.heart_image.get_rect()
        self.blink_interval = 500  # milliseconds
        self.last_blink_time = 0
        self.heart_visible = True
        # Animation variables
        self.shake_duration = 500  # milliseconds
        self.shake_amplitude = 8
        self.shake_start_time = 0
        self.shake_offset = (0, 0)

    def draw(self):
        self.level.background_image = pygame.transform.scale(
            self.level.background_image, (self.screen_width, self.screen_height))
        self.screen.blit(self.level.background_image, (0, 0))
        self.draw_bottom_bar()
        # self.draw_top_bar()
        self.draw_score()
        self.draw_words()
        self.draw_lives()
        self.draw_dialog()
        self.draw_character()
        pygame.display.flip()

    def change_level(self):
        self.current_level += 1
        if self.current_level >= len(self.levels):
            self.current_level = 0
        self.level = self.levels[self.current_level]
        self.words = self.level.words
        self.selected_word = 1
        self.score = self.level.score + self.score
        self.dialog_message = self.level.dialogue
        self.character_image = self.level.character

    def draw_score(self):
        score_text = self.font_score.render(
            "Puntaje: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 35 - score_text.get_height()/2))

    def draw_top_bar(self):
        pygame.draw.rect(self.screen, self.bar_color, pygame.Rect(
            0, 0, self.screen_width, 80))

    def draw_bottom_bar(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(
            0, self.screen_height - 80, self.screen_width, 80))

    def draw_lives(self):
        for i in range(self.lives):
            self.heart_rect.x = self.screen_width - 60 - i * 60
            self.screen.blit(self.heart_image, self.heart_rect)

    # Draw the three words at the bottom of the screen

    def draw_words(self):
        word_spacing = 12
        max_word_width = max(len(word)
                             for word in self.level.words) * self.font_game_size
        max_total_width = self.screen_width - 2 * word_spacing
        if max_word_width > max_total_width:
            # Words exceed the available width, perform word wrapping
            num_words_per_line = max_total_width // max_word_width
            word_width = max_total_width // num_words_per_line - word_spacing
        else:
            num_words_per_line = len(self.level.words)
            word_width = max_word_width

        x = self.screen_width / 2 - \
            (word_width * num_words_per_line +
             word_spacing * (num_words_per_line - 1)) / 2
        y = self.screen_height - self.font_game_size - 20
        for i, word in enumerate(self.level.words):
            word_text = self.font_game.render(word, True, self.word_color)
            if self.selected_word == i:
                word_text = self.font_game.render(
                    word, True, self.selected_word_color)
            self.screen.blit(word_text, (x, y))
            if (i + 1) % num_words_per_line == 0:
                x = self.screen_width / 2 - \
                    (word_width * num_words_per_line +
                     word_spacing * (num_words_per_line - 1)) / 2
                y -= self.font_game_size + 10
            else:
                x += word_width + word_spacing
# Draw the character image at the center of the screen

    def draw_character(self):
        character_center_x = self.character_rect.x + self.character_rect.width // 2
        character_center_y = self.character_rect.y + self.character_rect.height // 2
        character_pos = (
            character_center_x - self.character_image.get_width() // 2,
            character_center_y - self.character_image.get_height() // 2,
        )
        self.screen.blit(self.character_image, character_pos)

    # Draw the dialog message centered and 50 pixels from the top
    def draw_dialog(self):
        # Calculate the position of the character and dialog message
        character_center_x = self.character_rect.x + self.character_rect.width // 2
        character_center_y = self.character_rect.y + self.character_rect.height // 2
        character_pos = (
            character_center_x - self.character_image.get_width() // 2,
            character_center_y - self.character_image.get_height() // 2,
        )

        dialog_text = self.dialog_font.render(
            self.dialog_message, True, (255, 255, 255))
        dialog_width = dialog_text.get_width()
        dialog_height = dialog_text.get_height()
        dialog_pos = (
            character_center_x - dialog_width // 2,
            50 + dialog_height // 2,  # Position dialog 50 pixels from the top
        )

        # Draw the character image and dialog message
        current_time = pygame.time.get_ticks()
        if current_time - self.last_blink_time >= self.blink_interval:
            self.heart_visible = not self.heart_visible
            self.last_blink_time = current_time

        if self.heart_visible:
            self.screen.blit(self.character_image, character_pos)
            self.screen.blit(dialog_text, dialog_pos)

    def show_help_screen(self):
        help_image_path = "assets/inst.jpg"  # Replace with the path to your image

        help_image = pygame.image.load(help_image_path)
        help_image_rect = help_image.get_rect()

        help_window_width = self.screen_width
        help_window_height = self.screen_height
        help_window_x = 0
        help_window_y = 0
        help_window_rect = pygame.Rect(
            help_window_x, help_window_y, help_window_width, help_window_height)

        help_window_surface = pygame.Surface(
            (help_window_width, help_window_height))
        help_window_surface.set_alpha(200)
        help_window_surface.fill((0, 0, 0))

        help_image_rect.center = help_window_rect.center

        help_window_open = True
        while help_window_open:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    help_window_open = False

            self.screen.blit(help_window_surface, help_window_rect)
            self.screen.blit(help_image, help_image_rect)
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.selected_word = (self.selected_word - 1) % 3
                    self.select_word_sound.play()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.selected_word = (self.selected_word + 1) % 3

                    self.select_word_sound.play()
                elif event.key == pygame.K_RETURN:
                    if self.level.words[self.selected_word] == self.level.correct_word:
                        self.score += 10
                        self.correct_word_sound.play()
                        # self.dialog_message = "CORRECTO!"

                        self.change_level()
                    else:
                        self.lives -= 1
                        self.incorrect_word_sound.play()
                        self.shake_start_time = pygame.time.get_ticks()  # Start the shake animation
                        # self.dialog_message = "INCORRECTO!"
                    self.selected_word = 0
                elif event.key == pygame.K_h:
                    self.show_help_screen()

        return True

    def run(self):
        self.show_help_screen()
        running = True
        while running:
            running = self.handle_events()
            self.draw()
            if self.score <= 0:
                self.game_over_sound.play()
                game_over_text = self.font_game.render(
                    "PERDISTE!", True, self.game_over_color)
                game_over_rect = game_over_text.get_rect(
                    center=(self.screen_width/2, self.screen_height/2))
                self.screen.blit(game_over_text, game_over_rect)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False
            if self.lives <= 0:
                self.game_over_sound.play()
                game_over_text = self.font_game.render(
                    "PERDISTE!", True, self.game_over_color)
                game_over_rect = game_over_text.get_rect(
                    center=(self.screen_width/2, self.screen_height/2))
                self.screen.blit(game_over_text, game_over_rect)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False
        pygame.quit()


game = Game(800, 600)
game.run()
