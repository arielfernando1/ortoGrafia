import pygame


class Game:
    def __init__(self, sw, sh):
        pygame.init()
        pygame.display.set_caption("ORTOGRAFIA")
        self.screen_width = sw
        self.screen_height = sh
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.font_file = "assets/fonts/pixel.ttf"
        self.font_game_size = 64
        self.font_score_size = 32
        self.font_score = pygame.font.Font(
            self.font_file, self.font_score_size)
        self.font_game = pygame.font.Font(self.font_file, self.font_game_size)
        self.background_image = pygame.image.load(
            "assets/backrounds/bakeryBG.png")
        self.background_image = pygame.transform.scale(
            self.background_image, (self.screen_width, self.screen_height))
        self.bar_color = (200, 200, 200)
        self.heart_color = (255, 0, 0)
        self.word_color = (0, 0, 0)
        self.game_over_color = (255, 0, 0)
        self.score = 30
        self.lives = 3
        # Words
        self.words = ["Hay", "Ahi", "Ay!"]
        self.offensive_gameover_words = ["Vuele a la escuela", "JA JA. No sabe escribir", "JAJAJA. No sabe escribir"]
        self.selected_word = 1
        self.selected_word_color = (255, 255, 255)
        self.selected_word_size = 76
        # Sounds
        self.select_word_sound = pygame.mixer.Sound("assets/sounds/click.wav")
        self.correct_word_sound = pygame.mixer.Sound(
            "assets/sounds/correct.wav")
        self.incorrect_word_sound = pygame.mixer.Sound(
            "assets/sounds/incorrect.wav")
        self.game_over_sound = pygame.mixer.Sound(
            "assets/sounds/game_over.wav")
        # Characters
        self.character_image = pygame.image.load("baker.png")
        self.character_rect = self.character_image.get_rect(
            center=(self.screen_width/2, self.screen_height/2))
        # define the dialog message and its position
        self.dialog_font_size = 32
        self.dialog_font = pygame.font.Font(
            self.font_file, self.dialog_font_size)
        self.dialog_message = "SI ? PAN!"
        self.dialog_x = self.character_rect.centerx
        self.dialog_y = self.character_rect.bottom + 10

        self.heart_image = pygame.image.load("assets/backrounds/heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (50, 50))
        self.heart_rect = self.heart_image.get_rect()
        self.blink_interval = 500  # milliseconds
        self.last_blink_time = 0
        self.heart_visible = True

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
        word_spacing = 20
        total_width = len(self.words[0]) * self.font_game_size + len(self.words[1]) * \
            self.font_game_size + \
            len(self.words[2]) * self.font_game_size + 2 * word_spacing
        x = self.screen_width/2 - total_width/2
        y = self.screen_height - self.font_game_size - 20
        for i in range(3):
            word_text = self.font_game.render(
                self.words[i], True, self.word_color)
            if self.selected_word == i:
                word_text = self.font_game.render(
                    self.words[i], True, self.selected_word_color)
            self.screen.blit(word_text, (x, y))
            x += len(self.words[i]) * self.selected_word_size + word_spacing

    def draw_dialog(self):
        # draw character image and dialog message
        self.screen.blit(self.character_image, self.character_rect)
        dialog_text = self.dialog_font.render(
            self.dialog_message, True, (255, 255, 255))
        dialog_rect = dialog_text.get_rect(
            center=(self.dialog_x, self.dialog_y))
        self.screen.blit(dialog_text, dialog_rect)
    def show_tutorial_window(self):
        # Define tutorial message
        tutorial_message = [
            "Bienvenido a ORTOGRAFIA",
            "Este es un juego para mejorar tu ortografia",
            "Presiona las teclas num3ricas para cambiar las palabras",
            "Presiona Enter para seleccionar una palabra",
            "Si seleccionas la palabra correcta, ganas puntos",
            "Si seleccionas la palabra incorrecta, pierdes una vida",
            "Pierdes el juego si te quedas sin vidas",
            "Presiona Esc para salir del juego",
            "",
            "Presiona cualquier tecla para comenzar"
        ]

        # Set up tutorial window
        tutorial_font = pygame.font.Font(self.font_file, 16)
        tutorial_window_width = 750
        tutorial_window_height = len(tutorial_message) * tutorial_font.get_height()
        tutorial_window_x = self.screen_width/2 - tutorial_window_width/2
        tutorial_window_y = self.screen_height/2 - tutorial_window_height/2
        tutorial_window_rect = pygame.Rect(
            tutorial_window_x, tutorial_window_y, tutorial_window_width, tutorial_window_height)

        # Draw tutorial window background
        tutorial_window_surface = pygame.Surface(
            (tutorial_window_width, tutorial_window_height))
        tutorial_window_surface.set_alpha(200)
        tutorial_window_surface.fill((0, 0, 0))

        # Draw tutorial message
        for i in range(len(tutorial_message)):
            tutorial_text = tutorial_font.render(
                tutorial_message[i], True, (255, 255, 255))
            tutorial_text_rect = tutorial_text.get_rect(
                center=(tutorial_window_width/2, i*tutorial_font.get_height() + tutorial_font.get_height()/2))
            tutorial_window_surface.blit(tutorial_text, tutorial_text_rect)

        # Show tutorial window until a key is pressed
        tutorial_window_open = True
        while tutorial_window_open:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    tutorial_window_open = False

            # Draw tutorial window and update display
            self.screen.blit(tutorial_window_surface, tutorial_window_rect)
            pygame.display.flip()



    def draw(self):

        self.screen.blit(self.background_image, (0, 0))
        self.draw_score()
        self.draw_words()
        self.draw_dialog()
        self.draw_lives()
        pygame.display.flip()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_1:
                    self.selected_word = 0
                    self.words[0] = "HAY"
                    self.select_word_sound.play()
                elif event.key == pygame.K_2:
                    # self.show_tutorial_window()
                    self.selected_word = 1
                    self.words[1] = "AHI"
                    self.select_word_sound.play()

                elif event.key == pygame.K_3:
                    self.selected_word = 2
                    self.words[2] = "AY!"
                    self.select_word_sound.play()
                elif event.key == pygame.K_RETURN:
                    if self.selected_word == 0 and self.words[0] == "HAY":
                        self.correct_word_sound.play()
                        self.score += 10

                    elif self.selected_word == 1 and self.words[1] == "AHI":
                        self.incorrect_word_sound.play()
                        self.lives -= 1
                        self.score -= 10

                    elif self.selected_word == 2 and self.words[2] == "AY!":
                        self.incorrect_word_sound.play()
                        self.lives -= 1
                        self.score -= 10

                    else:
                        self.lives -= 1

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
