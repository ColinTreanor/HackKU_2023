import pygame
import time, math

# Initialize Pygame
pygame.init()

# Set window size
screen_info = pygame.display.Info()
sw = screen_info.current_w
sh = screen_info.current_h
window_size = (int(sw - sw/2), int(sh - sh/2))

# Create window
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("crazy8")

# Fill background color
background_color= (0,0,0)
window.fill(background_color)

# Set font and font size
font_size = 72
font = pygame.font.Font(None, font_size)

# Define font properties
button_font_size = 24
button_font = pygame.font.Font(None, button_font_size)

# Create function to display text on window
def display_text(text, seconds, x=None, y=None):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()

    # If x and y are given, use them as the center position
    if x is not None and y is not None:
        text_rect.center = (x, y)
    else:
        text_rect.center = (window_size[0] // 2, window_size[1] // 2)

    window.blit(text_surface, text_rect)
    pygame.display.flip()
    time.sleep(seconds)
    #window.fill((0,0,0))
    # Fill the background color only around the text
    background_rect = pygame.Rect(text_rect.left, text_rect.top, text_rect.width, text_rect.height)
    pygame.draw.rect(window, background_color, background_rect)

    # Update the screen to show the cleared background
    pygame.display.update()

# Create function to display button on window
def display_button(text, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Check if mouse is over button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, active_color, (x, y, w, h))
        if click[0] == 1:
            return True  # button clicked
    else:
        pygame.draw.rect(window, inactive_color, (x, y, w, h))

    # Draw button text
    text_surface = button_font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x + w // 2, y + h // 2)
    window.blit(text_surface, text_rect)

def display_persistent_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (x, y)
    window.blit(text_surface, text_rect)

def updateHand(handSize):
    colorTemp = (0,255,0)
    
    for i in range(handSize):
        size = (100,140)
        pos = (300 + ((50 + size[0]) * i), window_size[1] - 150)
        attr = pygame.Rect(pos, size)
        pygame.draw.rect(window, colorTemp, attr)
    pygame.display.flip()

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            return running
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
        pygame.quit()
        return running

# Main game loop
running = True
move = 0
while running:
    # Handle events
    handleEvents()

    # Display welcoming text and button
    if move == 0:
        display_text("Hello, Player!", 3)
        display_persistent_text("Hand:", 150, window_size[1] - 50)
        updateHand(7)
        move += 1

    if display_button("Play card", 150, window_size[1] - 200, 100, 50, (255, 0, 0), (200, 0, 10)):
        display_text("Card played!", 1.5)
        updateHand(7)
    
    if display_button("Draw card", 250, window_size[1] - 200, 100, 50, (255, 0, 0), (200, 0, 10)):
        display_text("Card drawn!", 1.5)
        updateHand(7)
    


    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
