# main.py
# Entry point for the application.
# This script initializes the display, sets up input handling, and runs the main loop.

from src.window import DisplayManager  # Renamed from Window
from src.events import InputHandler    # Renamed from Events


def main():
    """
    Main function to set up and run the application.
    """
    # Application settings
    window_width = 800
    window_height = 800
    window_title = "OpenGL Textured Quad Demo"

    # Initialize the display manager
    # This creates the window and OpenGL context.
    display = DisplayManager(window_width, window_height, window_title)

    # Initialize the input handler
    # This sets up keyboard and mouse event callbacks.
    # It needs a reference to the display manager to interact with the window (e.g., for fullscreen toggle).
    input_handler = InputHandler(display)

    # Set up the input callbacks
    # This connects GLFW's input events to our InputHandler's methods.
    input_handler.setup_callbacks()  # Renamed from events_setting()

    # Start the main application loop
    # This will handle rendering and event processing until the window is closed.
    display.run()


if __name__ == "__main__":
    # This ensures main() is called only when the script is executed directly
    main()
