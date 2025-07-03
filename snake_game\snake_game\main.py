from .views import SnakeGameView
from .models import SnakeGameModel

def main():
    model = SnakeGameModel()
    view = SnakeGameView(model)
    view.run()

if __name__ == '__main__':
    main()