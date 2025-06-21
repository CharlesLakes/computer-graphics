from src.window import Window
from src.events import Events


def main():
    # Create window
    window = Window(800, 800, "My window")

    # Create events
    events = Events(window)

    # Setting events
    events.events_setting()

    # Show window
    window.run()


if __name__ == "__main__":
    main()
