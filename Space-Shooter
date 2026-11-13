
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 65)

# Game settings
score = 0
lives = 3
game_over = False

# Ship Class
class Ship:
    def __init__(self):
        self.x = 275
        self.y = 520
        self.width = 50
        self.height = 50
        self.speed = 8

        self.rect = pygame.Rect(
            self.x, self.y,
            self.width, self.height
        )

    def move(self, direction):
        self.x += direction * self.speed

        self.x = max(0, min(self.x, 550))
        self.rect.x = self.x

    def draw(self):
        pygame.draw.polygon(
            screen, BLUE,
            [
                (self.x + 25, self.y),
                (self.x, self.y + 50),
                (self.x + 50, self.y + 50)
            ]
        )


# Bullet Class
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 10
        self.speed = 10

        self.rect = pygame.Rect(
            self.x, self.y,
            self.width, self.height
        )

    def move(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(
            screen, YELLOW, self.rect
        )


# Enemy Class
class Enemy:
    def __init__(self, x=None, y=0):
        self.width = 40
        self.height = 40

        if x is None:
            self.x = random.randint(0, 560)
        else:
            self.x = x

        self.y = y
        self.speed = 2

        self.rect = pygame.Rect(
            self.x, self.y,
            self.width, self.height
        )

    def move(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(
            screen, RED, self.rect
        )


# Create objects
ship = Ship()
bullets = []
enemies = []

# Enemy spawning event
frame_count = 0


# Display score and lives
def display_status():
    score_text = font.render(
        f"Score: {score}", True, WHITE
    )

    lives_text = font.render(
        f"Lives: {lives}", True, WHITE
    )

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (480, 10))


# Game Over screen

    
def display_game_over():
    screen.fill(BLACK)

    title = big_font.render(
        "GAME OVER", True, RED
    )

    final_score = font.render(
        f"Final Score: {score}", True, WHITE
    )

    restart = font.render(
        "Press R to Restart", True, YELLOW
    )

    exit_text = font.render(
        "Press ESC to Exit", True, WHITE
    )

    screen.blit(
        title,
        (WIDTH // 2 - title.get_width() // 2, 200)
    )

    screen.blit(
        final_score,
        (WIDTH // 2 - final_score.get_width() // 2, 280)
    )

    screen.blit(
        restart,
        (WIDTH // 2 - restart.get_width() // 2, 340)
    )

    screen.blit(
        exit_text,
        (WIDTH // 2 - exit_text.get_width() // 2, 390)
    )

    pygame.display.update()





# Main Game Loop

running = True
frame_count = 0

while running:

    frame_count += 1
    clock.tick(60)

    # Spawn enemies every 72 frames
    if frame_count % 72 == 0:
        enemies.append(Enemy())

    # Game Over
    
    if game_over:
        display_game_over()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_r:

                    score = 0
                    lives = 3
                    bullets = []
                    enemies = []
                    ship = Ship()
                    frame_count = 0
                    game_over = False

        continue


    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                ship.move(-1)

            elif event.key == pygame.K_RIGHT:
                ship.move(1)

            elif event.key == pygame.K_SPACE:

                if len(bullets) < 5:
                    bullets.append(
                        Bullet(ship.x + 22, ship.y)
                    )
                else:
                    print("Maximum 5 bullets on screen.")

    # Move bullets
    for bullet in bullets[:]:

        bullet.move()

        if bullet.y + bullet.height < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:

        enemy.move()

        if enemy.y + enemy.height >= HEIGHT:

            enemies.remove(enemy)
            lives -= 1

            if lives <= 0:
                game_over = True

    # Collision detection
    for bullet in bullets[:]:

        for enemy in enemies[:]:

            if bullet.rect.colliderect(enemy.rect):

                bullets.remove(bullet)
                enemies.remove(enemy)

                score += 10
                break

    # Draw objects
    ship.draw()

    for bullet in bullets:
        bullet.draw()

    for enemy in enemies:
        enemy.draw()

    # Display score and lives
    display_status()

    pygame.display.update()



     

    # Move bullets
    for bullet in bullets[:]:

        bullet.move()

        if bullet.y + bullet.height < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:

        enemy.move()

        # Enemy reaches bottom
        if enemy.y + enemy.height >= HEIGHT:

            enemies.remove(enemy)
            lives -= 1

            if lives <= 0:
                game_over = True

    # Collision detection
    for bullet in bullets[:]:

        for enemy in enemies[:]:

            if bullet.rect.colliderect(enemy.rect):

                bullets.remove(bullet)
                enemies.remove(enemy)

                score += 10
                break

    # Draw objects
    ship.draw()

    for bullet in bullets:
        bullet.draw()

    for enemy in enemies:
        enemy.draw()

    # Display game information
    display_status()

    pygame.display.update()


# Close game
pygame.quit()
sys.exit()
