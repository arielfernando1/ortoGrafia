import pygame
import pygame_menu

class Menu:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Menu")
        self.background_image = pygame.image.load("assets/backrounds/default.jpg")  # Replace with the path to your background image
        self.menu = pygame_menu.Menu(self.height, self.width, "Main Menu", theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button("New Game", self.start_game)
        self.menu.add.button("Settings", self.show_settings)
        self.menu.add.button("Exit", pygame_menu.events.EXIT)

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background_image, (0, 0))
            self.menu.mainloop(self.screen)

        pygame.quit()

    def start_game(self):
        print("Starting a new game...")
        # Add your game logic here

    def show_settings(self):
        print("Showing settings...")
        # Add your settings logic here


menu = Menu(800, 600)
menu.run()
