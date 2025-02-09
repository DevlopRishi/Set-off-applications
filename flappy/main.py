import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 250)

# Load assets
BIRD = pygame.image.load("bird.png")  # Replace with a proper bird image
BIRD = pygame.transform.scale(BIRD, (40, 30))
PIPE = pygame.image.load("pipe.png")  # Replace with a proper pipe image
PIPE = pygame.transform.scale(PIPE, (70, 400))

# Game Variables
bird_x, bird_y = 50, HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -8
pipe_gap = 150
pipe_velocity = -4
pipes = []
score = 0

# Function to generate pipes
def create_pipe():
    y_top = random.randint(-300, -100)
    y_bottom = y_top + PIPE.get_height() + pipe_gap
    pipes.append([WIDTH, y_top])
    pipes.append([WIDTH, y_bottom])

# Initialize first pipe
create_pipe()

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    SCREEN.fill(BLUE)  # Background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = jump_strength

    # Bird physics
    bird_velocity += gravity
    bird_y += bird_velocity

    # Draw bird
    SCREEN.blit(BIRD, (bird_x, bird_y))

    # Move pipes
    for i in range(len(pipes)):
        pipes[i][0] += pipe_velocity

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe[0] > -PIPE.get_width()]

    # Add new pipes
    if pipes[-1][0] < WIDTH - 200:
        create_pipe()

    # Draw pipes
    for i in range(0, len(pipes), 2):
        SCREEN.blit(PIPE, (pipes[i][0], pipes[i][1]))  # Top pipe
        SCREEN.blit(pygame.transform.flip(PIPE, False, True), (pipes[i+1][0], pipes[i+1][1]))  # Bottom pipe

    # Collision detection
    for i in range(0, len(pipes), 2):
        if bird_x + BIRD.get_width() > pipes[i][0] and bird_x < pipes[i][0] + PIPE.get_width():
            if bird_y < pipes[i][1] + PIPE.get_height() or bird_y + BIRD.get_height() > pipes[i+1][1]:
                running = False  # Game Over

    # Check if bird hits ground or ceiling
    if bird_y > HEIGHT or bird_y < 0:
        running = False

    # Update screen
    pygame.display.update()
    clock.tick(30)

pygame.quit()