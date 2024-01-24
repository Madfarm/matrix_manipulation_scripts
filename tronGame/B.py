import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
FPS = 30
VELOCITY = 5
SNAKE_SIZE = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Light Cycle Game")
clock = pygame.time.Clock()

# Define player properties
player1_pos = [100, 300]
player1_body = [player1_pos[:]]
player1_direction = "RIGHT"

player2_pos = [700, 300]
player2_body = [player2_pos[:]]
player2_direction = "LEFT"

# Game colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1_direction = "LEFT"
    if keys[pygame.K_d]:
        player1_direction = "RIGHT"
    if keys[pygame.K_w]:
        player1_direction = "UP"
    if keys[pygame.K_s]:
        player1_direction = "DOWN"

    if keys[pygame.K_LEFT]:
        player2_direction = "LEFT"
    if keys[pygame.K_RIGHT]:
        player2_direction = "RIGHT"
    if keys[pygame.K_UP]:
        player2_direction = "UP"
    if keys[pygame.K_DOWN]:
        player2_direction = "DOWN"

    # Update player positions
    if player1_direction == "LEFT":
        player1_pos[0] -= VELOCITY
    if player1_direction == "RIGHT":
        player1_pos[0] += VELOCITY
    if player1_direction == "UP":
        player1_pos[1] -= VELOCITY
    if player1_direction == "DOWN":
        player1_pos[1] += VELOCITY

    if player2_direction == "LEFT":
        player2_pos[0] -= VELOCITY
    if player2_direction == "RIGHT":
        player2_pos[0] += VELOCITY
    if player2_direction == "UP":
        player2_pos[1] -= VELOCITY
    if player2_direction == "DOWN":
        player2_pos[1] += VELOCITY

    # Check for collisions
    if player1_pos in player2_body or player1_pos in player1_body[:-1] or player1_pos[0] < 0 or player1_pos[0] > WIDTH or player1_pos[1] < 0 or player1_pos[1] > HEIGHT:
        print("Player 2 wins!")
        running = False

    if player2_pos in player1_body or player2_pos in player2_body[:-1] or player2_pos[0] < 0 or player2_pos[0] > WIDTH or player2_pos[1] < 0 or player2_pos[1] > HEIGHT:
        print("Player 1 wins!")
        running = False

    # Update the player's body
    player1_body.append(player1_pos[:])
    player2_body.append(player2_pos[:])

    # Draw everything
    screen.fill((0, 0, 0))
    for segment in player1_body:
        pygame.draw.rect(screen, BLUE, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    for segment in player2_body:
        pygame.draw.rect(screen, RED, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()