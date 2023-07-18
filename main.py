import math
import random
import pygame
import pygame_menu
import levels
import settings
import thorpy as tp


class Game:
    def __init__(self, sw, sh):
        pygame.init()
        pygame.display.set_caption("Test")
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        # levels
        self.levels = levels.levels
        self.current_level = 0
        self.level = self.levels[self.current_level]
        self.words = self.level.words
        self.level_time = 10
        # Randomize words
        random.shuffle(self.words)
        self.selected_word = 0
        self.text_visible = True
        # self.screen = MyMenu(800, 600)
        # Buttons
        # screen settings
        self.screen_width = sw
        self.screen_height = sh
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        tp.init(self.screen,tp.theme_classic)
        # Others
        # button = tp.Button("Hello world")
        # ui_elements = tp.Group([button])
        # self.updater = ui_elements.get_updater()
        
        # font settings
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
        #Pygame menu
        self.menu = pygame_menu.Menu(
            'Game', sw, sh, theme=pygame_menu.themes.THEME_DARK)
        # self.menu.add.text_input('Nombre: ', default='Jugador')
        # self.menu.add.selector('Dificultad: ', [('Fácil', 1), ('Difícil', 3)], onchange=self.set_difficulty())
        self.menu.add.button('Jugar', self.start_game)
        self.menu.add.button('Ayuda', self.show_help_screen)
        self.menu.add.button('Salir', pygame_menu.events.EXIT)
        
        self.score = self.level.score
        self.lives = 3
        self.selected_word_color = (255, 255, 255)
        self.selected_word_size = 76
        self.select_word_sound = pygame.mixer.Sound(settings.SOUND_CLICK)
        self.correct_word_sound = pygame.mixer.Sound(settings.SOUND_CORRECT)
        self.tick_sound = pygame.mixer.Sound(settings.SOUND_TICK)
        self.incorrect_word_sound = pygame.mixer.Sound(
            settings.SOUND_INCORRECT)
        self.game_over_sound = pygame.mixer.Sound(settings.SOUND_GAME_OVER)
        self.character_image = self.level.character
        self.character_rect = self.character_image.get_rect(
            center=(self.screen_width/2, self.screen_height/2))
        self.dialog_font_size = 32
        self.alternative_font_size = 16
        self.dialog_font = pygame.font.Font(
            self.font_file, self.dialog_font_size)
        self.alternative_font = pygame.font.Font(
            self.font_file, self.alternative_font_size)
        self.dialog_message = self.level.dialogue
        self.dialog_x = self.character_rect.centerx
        self.dialog_y = self.character_rect.bottom + 10

        self.heart_image = pygame.image.load("assets/backrounds/heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (50, 50))
        self.heart_rect = self.heart_image.get_rect()
        self.blink_interval = 1000  # milliseconds
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
        self.draw_top_bar()
        self.draw_bottom_bar()
        self.draw_score()
        self.draw_timer()
        self.draw_words()
        self.draw_lives()
        self.draw_dialog()
        self.draw_character()
        # self.screen.draw()
        # self.updater.update()
        pygame.display.flip()
        
    def set_difficulty(self):
        # Get selected difficulty
        pass
        
    def start_game(self):
        self.score = 0
        self.lives = 1
        self.level_time = 10
        self.change_level()
        self.run()
        tp_input = tp.TextInput("Enter your name: ", placeholder="Name")
        tp_input.launch_alone()
        
        
    def show_menu(self):
        self.menu.mainloop(self.screen)

    def change_level(self):
        self.level.is_complete = True
        self.current_level = self.levels.index(self.level)
        print("Level " + str(self.current_level) + " completed")
        print(str(len(self.levels)) + " levels remaining")
        self.levels = [level for level in self.levels if not level.is_complete] 
        if len(self.levels) == 0:
            print("Game completed")
        random_index = random.randint(0, len(self.levels)-1)    
        self.level = self.levels[random_index]
        self.words = self.level.words
        self.selected_word = 1
        self.score = self.level.score + self.score
        self.dialog_message = self.level.dialogue
        self.character_image = self.level.character

    def draw_score(self):
        score_text = self.font_score.render(
            "Puntaje: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 35 - score_text.get_height()/2))
        
    # def draw_time_bar(self):
        

    def draw_top_bar(self):
        pygame.draw.rect(self.screen, self.bar_color, pygame.Rect(
            0, 0, self.screen_width, 60))

    def draw_bottom_bar(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(
            0, self.screen_height - 150, self.screen_width, 150))

    # draw countdown timer
    def draw_timer(self):
        timer_text = self.font_score.render(
            str(self.level_time), True, (255, 255, 255))
        self.screen.blit(timer_text, (self.screen_width -
                         (self.screen_width/2), 35 - timer_text.get_height()/2))

    def draw_lives(self):
        for i in range(self.lives):
            self.heart_rect.x = self.screen_width - 60 - i * 60
            self.screen.blit(self.heart_image, self.heart_rect)
            if self.lives == 0:
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
                

    def draw_character(self):
        character_center_x = self.character_rect.x + self.character_rect.width // 2
        character_center_y = self.character_rect.y + self.character_rect.height // 2
        character_pos = (
            character_center_x - self.character_image.get_width() // 2,
            character_center_y - self.character_image.get_height() // 2,
        )
        self.screen.blit(self.character_image, character_pos)

    def draw_dialog(self):
        dialog_text = self.dialog_font.render(
            self.dialog_message, True, (255, 255, 255))
        dialog_width = dialog_text.get_width()
        dialog_pos = (
            (self.screen_width - dialog_width) // 2,
            460
        )

        if dialog_width > self.screen_width - 20:
            alternative_dialog_text = self.alternative_font.render(
                self.dialog_message, True, (255, 255, 255))
            alternative_dialog_width = alternative_dialog_text.get_width()
            alternative_dialog_pos = (
                (self.screen_width - alternative_dialog_width) // 2,
                460
            )
            self.screen.blit(alternative_dialog_text, alternative_dialog_pos)
        else:
            self.screen.blit(dialog_text, dialog_pos)
            
            

    def draw_character(self):
        character_center_x = self.character_rect.x + self.character_rect.width // 2
        character_center_y = self.character_rect.y + self.character_rect.height // 2

        # Calculate the new image dimensions while preserving aspect ratio
        max_width = 200  # Define the maximum width for the character image
        max_height = 200  # Define the maximum height for the character image
        image_width = self.character_image.get_width()
        image_height = self.character_image.get_height()

        if image_width > max_width or image_height > max_height:
            # Calculate the scaling factor for width and height
            width_ratio = max_width / image_width
            height_ratio = max_height / image_height

            # Choose the smaller scaling factor to maintain aspect ratio
            scaling_factor = min(width_ratio, height_ratio)

            # Calculate the new dimensions based on the scaling factor
            new_width = int(image_width * scaling_factor)
            new_height = int(image_height * scaling_factor)

            # Scale down the character image
            scaled_image = pygame.transform.scale(self.character_image, (new_width, new_height))

            # Recalculate the character position based on the scaled image dimensions
            character_pos = (
                character_center_x - new_width // 2,
                character_center_y - new_height // 2,
            )

            self.screen.blit(scaled_image, character_pos)
        else:
            # If the image doesn't exceed the maximum dimensions, draw it as is
            character_pos = (
                character_center_x - image_width // 2,
                character_center_y - image_height // 2,
            )
            self.screen.blit(self.character_image, character_pos)

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

    def handle_word_click(self, word_index):
        if self.level.words[word_index] == self.level.correct_word:
            self.score += 10
            self.correct_word_sound.play()
            self.change_level()
        else:
            self.lives -= 1
            self.incorrect_word_sound.play()
            self.selected_word = 0

    def handle_events(self):
        event_actions = {
            pygame.QUIT: self.quit_game,
            pygame.KEYDOWN: {
                pygame.K_ESCAPE: self.show_menu,
                pygame.K_LEFT: lambda: self.update_selected_word(-1),
                pygame.K_a: lambda: self.update_selected_word(-1),
                pygame.K_RIGHT: lambda: self.update_selected_word(1),
                pygame.K_d: lambda: self.update_selected_word(1),
                pygame.K_RETURN: self.check_selected_word,
                pygame.K_h: self.show_help_screen
            },
            pygame.MOUSEBUTTONDOWN: {
                1: lambda: print("Left key pressed"),
                0: lambda: print("Middle key pressed")
            }
        }

        for event in pygame.event.get():
            event_type = event.type
            event_key = None

            if event_type == pygame.KEYDOWN:
                event_key = event.key
            elif event_type == pygame.MOUSEBUTTONDOWN:
                event_key = event.button
            action = event_actions.get(event_type)

            if action:
                if isinstance(action, dict):
                    action = action.get(event_key)
                    if action:
                        action()
                else:
                    action()

        return True

    def quit_game(self):
        return False

    def update_selected_word(self, increment):
        self.selected_word = (self.selected_word + increment) % 3
        self.select_word_sound.play()

    def check_selected_word(self):
        if self.level.words[self.selected_word] == self.level.correct_word:
            self.correct_word_sound.play()
            self.score += 10
            self.level_time = 10
            self.draw()
            # mark current level as completed
            self.level.is_completed = True
            pygame.time.delay(1000)
            self.change_level()

        else:
            self.incorrect_word_sound.play()
            self.score -= 10
            self.level_time = 10
            self.lives -= 1
            self.draw()
            pygame.time.delay(1000)
            self.change_level()
        self.selected_word = 0

    def show_menu_screen(self):
        return False

    def run(self):
        running = True
        self.show_help_screen()
        while running:
            running = self.handle_events()
            self.draw()
            current_time = pygame.time.get_ticks()
         
            if current_time - self.last_blink_time >= self.blink_interval:
                self.level_time -= 1
                self.tick_sound.play()
                if self.level_time <= 0:
                    self.lives -= 1
                    self.change_level()
                    self.level_time = 10
                self.last_blink_time = current_time

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
                self.draw()
                pygame.time.wait(1000)
                title = "Perdiste :("
                message = "¿Quieres jugar de nuevo?"
                choice = tp.AlertWithChoices(title, ("Nuevo juego","Salir"), message)
                choice.launch_alone()
                if choice.get_value() == "Nuevo juego":
                    self.lives = 3
                    print("Nuevo juego")
                else:
                    running = False
        pygame.quit()


game = Game(800, 600)
game.run()
