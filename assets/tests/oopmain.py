import pygame

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font_file = "pixel.ttf"
        self.font_game_size = 64
        self.font_score_size = 24
        self.font_score = pygame.font.Font(self.font_file, self.font_score_size)
        self.font_game = pygame.font.Font(self.font_file, self.font_game_size)
        self.background_image = pygame.image.load("bg.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))
        self.bar_color = (200, 200, 200)
        self.heart_color = (255, 0, 0)
        self.word_color = (0, 0, 0)
        self.score = 1500
        self.lives = 3
        self.words = ["Hay", "Ahi", "Ay!"]
        self.heart_image = pygame.image.load("heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (50, 50))
        self.heart_rect = self.heart_image.get_rect()
        self.blink_interval = 500  # milliseconds
        self.last_blink_time = 0
        self.heart_visible = True


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_1:
                    self.check_word(0)
                elif event.key == pygame.K_2:
                    self.check_word(1)
                elif event.key == pygame.K_3:
                    self.check_word(2)
        return True

    def check_word(self, index):
        if self.words[index] == "Apple":
            self.score += 1
        else:
            self.lives -= 1

    def update_blinking(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_blink_time >= self.blink_interval:
            self.heart_visible = not self.heart_visible
            self.last_blink_time = current_time

    def draw_score(self):
        score_text = self.font_score.render("Score: " + str(self.score), True, (0, 0, 0))
        self.screen.blit(score_text, (10, 35 - score_text.get_height()/2))

    def draw_hearts(self):
        for i in range(self.lives):
            if self.heart_visible:
                heart_x = self.screen_width - 50 * (i + 1) -i*10
                self.screen.blit(self.heart_image, (heart_x, 10))

    def draw_word_options(self):
        word_spacing = self.screen_width / len(self.words)
        for i in range(len(self.words)):
            word_text = self.font_game.render(self.words[i], True, self.word_color)
            self.screen.blit(word_text, (word_spacing * i + word_spacing/2 - word_text.get_width()/2, self.screen_height - 100))

    def run(self):
        pygame.display.set_caption("My Game")
        while True:
            if not self.handle_events():
                break
            self.update_blinking()
            self.screen.blit(self.background_image, (0, 0))
            self.draw_score()
            self.draw_hearts()
            self.draw_word_options()
            pygame.display.flip()
            pygame.quit()
