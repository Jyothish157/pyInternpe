import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (GRID_SIZE, 0)

    def move(self):
        x, y = self.body[0]
        x += self.direction[0]
        y += self.direction[1]
        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, new_direction):
        if new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1]:
            self.direction = new_direction

    def grow(self):
        x, y = self.body[-1]
        self.body.append((x - self.direction[0], y - self.direction[1]))

    def check_collision(self):
        x, y = self.body[0]
        return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or self.body[0] in self.body[1:]

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (*segment, GRID_SIZE, GRID_SIZE))


# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE
        y = random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE
        self.position = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (*self.position, GRID_SIZE, GRID_SIZE))


# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -GRID_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, GRID_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-GRID_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((GRID_SIZE, 0))

        snake.move()

        if snake.body[0] == food.position:
            snake.grow()
            food.randomize_position()

        if snake.check_collision():
            pygame.quit()
            sys.exit()

        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()

