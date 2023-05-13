import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load a custom font
font_file = "pixel.ttf"
font_game_size = 64
font_score_size = 24
fontScore = pygame.font.Font(font_file, font_score_size)
fontGame = pygame.font.Font(font_file, font_game_size)

# Set up background image
background_image = pygame.image.load("bg.jpg")
print(pygame.image.get_extended())  # Print if extended image formats are supported
print(pygame.image.get_extended())  # Print if extended image formats are supported
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


# Set the window caption
pygame.display.set_caption("My Game")

# Set up the font for the score display and word options
score_font = fontScore
word_font = fontGame

# Set up the colors for the top bar, hearts, and word options
bar_color = (200, 200, 200)
heart_color = (255, 0, 0)
word_color = (0, 0, 0)

# Set up the score, lives, and word options
score = 1500
lives = 3
words = ["Hay", "Ahi", "Ay!"]

# Set up the hearts
heart_image = pygame.image.load("heart.png")
heart_image = pygame.transform.scale(heart_image, (50, 50))
heart_rect = heart_image.get_rect()

# Set up the blinking timer
blink_interval = 500  # milliseconds
last_blink_time = 0
heart_visible = True

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_1:
                if words[0] == "Apple":
                    score += 1
                else:
                    lives -= 1
            elif event.key == pygame.K_2:
                if words[1] == "Apple":
                    score += 1
                else:
                    lives -= 1
            elif event.key == pygame.K_3:
                if words[2] == "Apple":
                    score += 1
                else:
                    lives -= 1

    # Update blinking timer
    current_time = pygame.time.get_ticks()
    if current_time - last_blink_time >= blink_interval:
        heart_visible = not heart_visible
        last_blink_time = current_time

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))

    # Draw the top bar
    pygame.draw.rect(screen, bar_color, (0, 0, screen_width, 70))

    # Draw the vertically centered score and align it to the left
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 35 - score_text.get_height()/2))

    # Draw the hearts
    for i in range(lives):
        if heart_visible:
            heart_x = screen_width - 50 * (i + 1) -i*10
            screen.blit(heart_image, (heart_x, 10))
    # Draw the selectable word options proportionally spaced out
    word_spacing = screen_width / len(words)
    for i in range(len(words)):
        word_text = word_font.render(words[i], True, word_color)
        word_x = word_spacing * (i + 0.5) - word_text.get_width()/2
        word_y = screen_height - 100
        screen.blit(word_text, (word_x, word_y))
        
        

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

