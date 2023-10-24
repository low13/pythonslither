import pygame
import sys
import time

from snake import Snake, Direction
from food import Food

class GameClass:
    def __init__(self, name: str, fps: int):
        # Create the window
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption(name)

        # Initialize the audio system
        pygame.mixer.init()

        # Setup the font
        self.font = pygame.font.Font(size=80)

        # Start rendering the snake
        self.snake = Snake()

        self.food = Food(self.screen)

        # Prepare the clock system
        clock = pygame.time.Clock()
        last_time = time.time()

        while True:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time

            # Draw a new frame
            self.update()

            clock.tick(fps)
    
    def update(self):
        self.screen.fill("black")

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if self.snake.direction != Direction.DOWN:
                        self.snake.direction = Direction.UP
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if self.snake.direction != Direction.RIGHT:
                        self.snake.direction = Direction.LEFT
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.snake.direction != Direction.UP:
                        self.snake.direction = Direction.DOWN
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.snake.direction != Direction.LEFT:
                        self.snake.direction = Direction.RIGHT

        # Get the sound effects
        try:
            game_over = pygame.mixer.Sound("sfx/gameover.wav")
            level_up = pygame.mixer.Sound("sfx/levelup.wav")
        except:
            print("Unable to find the sound effect files, make sure there is a sfx folder in the same directory as the game")

        # Draw the snake
        for square in self.snake.squares:
            rect = pygame.Rect(square[0], square[1], 40, 40)
            if square[0] > 600: square[0] = 0
            if square[0] < 0: square[0] = 600
            if square[1] > 400: square[1] = 0
            if square[1] < 0: square[1] = 400
            pygame.draw.rect(self.screen, "green", rect)

        # Check if the snake will eat food
        if self.food.rect.collidepoint(self.snake.squares[0][0], self.snake.squares[0][1]):
            # Increase the snake's length
            if level_up: level_up.play()
            self.food = Food(self.screen)
            self.should_increase_snake_length = True
        else:
            # Keep the food where it is
            self.food = Food(self.screen, (self.food.rect.x, self.food.rect.y))
            self.should_increase_snake_length = False

        # Check if the snake collides with itself
        for i in self.snake.squares:
            if self.snake.squares.count(i) > 1:
                if game_over: game_over.play()
                time.sleep(2)
                self.reset()

        # Snake movement
        if self.snake.direction == Direction.UP:
            self.snake.squares.insert(0, [self.snake.squares[0][0], self.snake.squares[0][1] - 40])
        elif self.snake.direction == Direction.RIGHT:
            self.snake.squares.insert(0, [self.snake.squares[0][0] + 40, self.snake.squares[0][1]])
        elif self.snake.direction == Direction.DOWN:
            self.snake.squares.insert(0, [self.snake.squares[0][0], self.snake.squares[0][1] + 40])
        elif self.snake.direction == Direction.LEFT:
            self.snake.squares.insert(0, [self.snake.squares[0][0] - 40, self.snake.squares[0][1]])

        if not self.should_increase_snake_length and self.snake.direction != Direction.NONE:
            self.snake.squares.pop()

        # Display the player's score
        score = self.font.render(str(len(self.snake.squares) - 1).zfill(3), True, "white")
        self.screen.blit(score, (500, 0))

        pygame.display.flip()

    def reset(self):
        self.snake.direction = Direction.NONE
        self.snake.squares = [[280, 200]]