from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class SnakeGameModel:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = Direction.RIGHT
        self.food = (400, 300)
        self.score = 0

    def move_snake(self):
        head = self.snake[0]
        if self.direction == Direction.UP:
            new_head = (head[0], head[1] - 20)
        elif self.direction == Direction.DOWN:
            new_head = (head[0], head[1] + 20)
        elif self.direction == Direction.LEFT:
            new_head = (head[0] - 20, head[1])
        elif self.direction == Direction.RIGHT:
            new_head = (head[0] + 20, head[1])
        self.snake.insert(0, new_head)

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:]:
            return True
        if head[0] < 0 or head[0] > 800 or head[1] < 0 or head[1] > 600:
            return True
        return False

    def check_food_collision(self):
        head = self.snake[0]
        if head == self.food:
            self.score += 1
            return True
        return False

    def update_food(self):
        import random
        self.food = (random.randint(0, 39) * 20, random.randint(0, 29) * 20)