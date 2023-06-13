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
        # Test settings
        # self.dialog_offset = 0
        # self.animation_speed = 2
        # self.animation_offset = 0
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
        # Add opacity to the background image
        # self.level.background_image.set_alpha(0)
        self.screen.blit(self.level.background_image, (0, 0))
        self.draw_score()
        self.draw_words()
        self.draw_lives()
        self.draw_dialog()
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

    def draw_dialog(self):
        # draw character image and dialog message
        # self.screen.blit(self.level.character, self.character_rect)

        current_time = pygame.time.get_ticks()
        if current_time - self.last_blink_time >= self.blink_interval:
            self.text_visible = not self.text_visible
            self.last_blink_time = current_time

        if self.text_visible:
            dialog_text = self.dialog_font.render(
                self.dialog_message, True, (255, 255, 255))
            dialog_text.set_alpha(255)  # Set full opacity
            dialog_rect = dialog_text.get_rect(
                center=(self.dialog_x, self.dialog_y))
            self.screen.blit(dialog_text, dialog_rect)
        if current_time - self.shake_start_time < self.shake_duration:
            shake_progress = (
                current_time - self.shake_start_time) / self.shake_duration
            shake_angle = shake_progress * 2 * math.pi
            shake_offset_x = int(math.sin(shake_angle)
                                 * self.shake_amplitude)
            shake_offset_y = int(math.cos(shake_angle)
                                 * self.shake_amplitude)
            self.shake_offset = (shake_offset_x, shake_offset_y)
        else:
            self.shake_offset = (0, 0)

        character_pos = (self.character_rect.x +
                         self.shake_offset[0], self.character_rect.y + self.shake_offset[1])
        self.screen.blit(self.level.character, character_pos)

    def show_help_screen(self):
        help_text = [
            "Welcome to ORTOGRAFIA",
            "This is a game to improve your spelling",
            "Press the numeric keys to change the words",
            "Press Enter to select a word",
            "If you select the correct word, you earn points",
            "If you select the incorrect word, you lose a life",
            "You lose the game if you run out of lives",
            "Press Esc to exit the game",
            "",
            "Press any key to continue"
        ]

        help_font = pygame.font.Font(self.font_file, 16)
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

        for i in range(len(help_text)):
            help_text_rendered = help_font.render(
                help_text[i], True, (255, 255, 255))
            help_text_rect = help_text_rendered.get_rect(
                center=(help_window_width / 2, i * help_font.get_height() + help_font.get_height() / 2))
            help_window_surface.blit(help_text_rendered, help_text_rect)

        help_window_open = True
        while help_window_open:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    help_window_open = False

            self.screen.blit(help_window_surface, help_window_rect)
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
