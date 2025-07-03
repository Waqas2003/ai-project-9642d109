import pygame
from .models import SnakeGameModel

class SnakeGameView:
    def __init__(self, model):
        self.model = model
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake Game')

    def draw_snake(self):
        for pos in self.model.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 20, 20))

    def draw_food(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.model.food[0], self.model.food[1], 20, 20))

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.model.score}', True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.model.direction != Direction.DOWN:
                    self.model.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.model.direction != Direction.UP:
                    self.model.direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.model.direction != Direction.RIGHT:
                    self.model.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.model.direction != Direction.LEFT:
                    self.model.direction = Direction.RIGHT

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.model.move_snake()
            if self.model.check_collision():
                break
            if self.model.check_food_collision():
                self.model.update_food()
            self.screen.fill((0, 0, 0))
            self.draw_snake()
            self.draw_food()
            self.draw_score()
            pygame.display.flip()
            clock.tick(10)