from pygame import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the screen size and ball starting position
WIDTH = 800
HEIGHT = 600
BALL_X = 300
BALL_Y = 300

# Define the ball's radius and speed
BALL_RADIUS = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 3

# Initialize pygame and create the screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
running = True
while running:

    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    BALL_X += BALL_SPEED_X
    BALL_Y += BALL_SPEED_Y

    # Check for ball bouncing off walls
    if BALL_X + BALL_RADIUS > WIDTH or BALL_X - BALL_RADIUS < 0:
        BALL_SPEED_X *= -1

    if BALL_Y + BALL_RADIUS > HEIGHT or BALL_Y - BALL_RADIUS < 0:
        BALL_SPEED_Y *= -1

    # Change the ball's color each bounce
    if BALL_SPEED_X > 0:
        BALL_COLOR = RED
    elif BALL_SPEED_X < 0:
        BALL_COLOR = GREEN
    if BALL_SPEED_Y > 0:
        BALL_COLOR = BLUE

    # Fill the screen black
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (BALL_X, BALL_Y), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()

