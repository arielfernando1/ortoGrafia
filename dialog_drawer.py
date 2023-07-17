import thorpy
import pygame

class DialogDrawer:
    def __init__(self):
        pygame.init()
        self.screen = thorpy.functions.screen.set_screen()
        self.character_rect = pygame.Rect(0, 0, 100, 100)  # Replace with appropriate values
        self.character_image = pygame.Surface((100, 100))  # Replace with appropriate image
        self.dialog_font = pygame.font.Font(None, 24)  # Replace with appropriate font
        self.dialog_message = "Hello, world!"  # Replace with appropriate dialog message
        self.heart_visible = True

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

        dialog_element = thorpy.make_text(
            self.dialog_message,
            font_size=24,
            font_color=(255, 255, 255)
        )
        dialog_element.set_topleft((character_center_x, 50))

        character_element = thorpy.make_image_button(
            self.character_image,
            func=None
        )
        character_element.set_topleft(character_pos)

        # Create ThorPyApplication and add elements
        application = thorpy.Application(size=(800, 600), caption="Dialog")
        application.add_elements([dialog_element, character_element])

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            thorpy.functions.screen.fill((0, 0, 0))  # Fill the screen with a background color
            application.update()  # Update the elements
            application.render()  # Render the elements
            pygame.display.flip()

if __name__ == "__main__":
    drawer = DialogDrawer()
    drawer.draw_dialog()