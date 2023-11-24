import pygame
import random
import serial
from pygame import mixer
import sys

class Character:
    def __init__(self, image):
        self.image = pygame.transform.scale(pygame.transform.rotate(image, 180), (80, 80))
        self.rect = self.image.get_rect()
        self.generate_random_position()

    def generate_random_position(self, x_position=0):
        if x_position != 0:
            self.rect.x = x_position
            self.rect.y = 0
        else:
            self.rect.x = random.randint(100, 700)  # Adjust the range for vehicle generation
            self.rect.y = 0

    def move_down(self):
        self.rect.y += 5

# Replace first argument of serial.Serial with the port of your Arduino
if len(sys.argv) > 1:
    ser = serial.Serial(sys.argv[1], 9600)
else:
    ser = serial.Serial('COM3', 9600)

pygame.init()
mixer.init()
mixer.music.load("car_acceleration.mp3")
mixer.music.set_volume(0.5)
s_width, s_height = 800, 600
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Car game")

available_characters = [
    pygame.image.load("images/car1.png"),
    pygame.image.load("images/motobike1.png"),
    pygame.image.load("images/motorbike2.png"),
    pygame.image.load("images/enemy_car_1.png"),
    pygame.image.load("images/enemy_car_2.png"),
    pygame.image.load("car.png")
]

selected_character_index = 0
char_img = available_characters[selected_character_index]

char_img = pygame.transform.scale(char_img, (100, 100))
char_rect = char_img.get_rect()
char_rect.center = (s_width // 2, s_height // 2)
char_rect.y = 500
clock = pygame.time.Clock()
FPS = 60
random_chars = []  # List to store multiple random characters
game_over = False

def game_over_screen():
    game_over_rect = pygame.Rect(s_width // 4, s_height // 4, s_width // 2, s_height // 2)
    pygame.draw.rect(screen, (255, 255, 255), game_over_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
    text_rect = text.get_rect(center=(s_width // 2, s_height // 2))
    screen.blit(text, text_rect)

bg = pygame.image.load("road.png")
bg = pygame.transform.scale(bg, (800, 600))
score = 0

# ... (rest of your code, including determine_number_of_vehicle_generate and win_screen)

running = True
mixer.music.play(loops=1000)
win = False
initial_position = (500, 500)

while running:
    joystick_data = ser.readline().decode().strip().split(',')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r] and game_over:
            game_over = False
            mixer.music.play(360)
            char_rect.center = (s_width // 2, s_height // 2)
            char_rect.y = 500
            random_chars = []  # Reset the list of random characters
            score = 0

    if not game_over:
        if len(joystick_data) == 2:
            joystick_x, joystick_y = map(int, joystick_data)
            print(joystick_y, joystick_x)

            if joystick_x != 514 or joystick_y != 510:
                char_rect.x += int((joystick_x - 500) / 10)
                char_rect.y += int((joystick_y - 500) / 10)
                char_rect.x = max(char_rect.x, 0)
                char_rect.x = min(char_rect.x, s_width - char_rect.width)
                char_rect.y = max(char_rect.y, 0)
                char_rect.y = min(char_rect.y, s_height - char_rect.height)

        if not random_chars or all(char.rect.y >= s_height for char in random_chars):
            n_of_vehicle_to_generate = determine_number_of_vehicle_generate(score)
            random_chars = [Character(random.choice(available_characters)) for _ in range(n_of_vehicle_to_generate)]

        for random_char in random_chars:
            random_char.move_down()

        for random_char in random_chars:
            if char_rect.colliderect(random_char.rect):
                game_over = True

        current_time = pygame.time.get_ticks()
        if current_time - score_update_time >= score_interval:
            score += 1
            score_update_time = current_time

    screen.blit(bg, (0, 0))
    screen.blit(char_img, char_rect)

    if not game_over:
        for random_char in random_chars:
            screen.blit(random_char.image, random_char.rect)

    else:
        mixer.music.stop()
        game_over_screen()

    score_count(score)
    pygame.display.flip()
    clock.tick(FPS)

    if score >= 100:
        win = True
        mixer.music.stop()
        win_screen()
        font = pygame.font.Font(None, 36)
        text = font.render("You Win! Press R to Restart", True, (0, 255, 0))
        text_rect = text.get_rect(center=(s_width // 2, s_height // 2))
        screen.blit(text, text_rect)

# Quit the game
pygame.quit()
