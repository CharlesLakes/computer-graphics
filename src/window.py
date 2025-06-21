import glfw
from OpenGL.GL import *
import sys
from src.face import TexturedQuad  # Updated import


# Manages the display window, OpenGL context, and main event loop.
class DisplayManager:
    def __init__(self, width, height, title):
        """
        Initializes GLFW, creates a window, and stores window properties.

        Args:
            width (int): The initial width of the window.
            height (int): The initial height of the window.
            title (str): The title of the window.
        """
        if not glfw.init():
            print("Error: GLFW cannot init")
            sys.exit(1)

        # Store original window dimensions for restoring from fullscreen
        self.original_width = width
        self.original_height = height
        self.title = title
        self.is_fullscreen = False

        # Create the GLFW window
        self.window = glfw.create_window(
            width,
            height,
            title,
            None,  # Monitor (None for windowed mode)
            None   # Share (None for no resource sharing)
        )

        if not self.window:
            print("Error: Window could not be created")
            glfw.terminate()
            sys.exit(1)

    def get_current_monitor(self):
        """
        Determines the monitor on which the window is predominantly displayed.

        This is useful for placing the fullscreen window on the correct monitor.

        Returns:
            glfw.Monitor: The monitor object.
        """
        # Get current window position and size
        win_x, win_y = glfw.get_window_pos(self.window)
        win_width, win_height = glfw.get_window_size(self.window)

        # Calculate the center of the window
        win_center_x = win_x + win_width // 2
        win_center_y = win_y + win_height // 2

        monitors = glfw.get_monitors()
        if not monitors:
            # Fallback if no monitors are detected (should not happen in normal circumstances)
            return glfw.get_primary_monitor()

        for monitor in monitors:
            # Get monitor position and video mode (which includes size)
            mon_x, mon_y = glfw.get_monitor_pos(monitor)
            video_mode = glfw.get_video_mode(monitor)
            mon_width = int(video_mode.size.width)
            mon_height = int(video_mode.size.height)

            # Check if the window's center is within the bounds of this monitor
            if (mon_x <= win_center_x < mon_x + mon_width and
                    mon_y <= win_center_y < mon_y + mon_height):
                return monitor

        # If, for some reason, the window center isn't found in any monitor,
        # default to the primary monitor.
        return glfw.get_primary_monitor()

    def toggle_fullscreen(self):
        """
        Toggles the window between fullscreen and windowed mode.

        When switching to fullscreen, it uses the monitor the window is currently on.
        When switching to windowed, it restores the original dimensions and a default position.
        """
        if self.is_fullscreen:
            # Switch to windowed mode
            glfw.set_window_monitor(
                self.window,
                None,  # Null monitor pointer for windowed mode
                100,   # X position for windowed mode
                100,   # Y position for windowed mode
                self.original_width,
                self.original_height,
                # Refresh rate (0 for default/don't care in windowed mode)
                0
            )
            self.is_fullscreen = False
            print("Switched to windowed mode.")
        else:
            # Switch to fullscreen mode on the current monitor
            monitor = self.get_current_monitor()
            if not monitor:
                print("Error: Could not determine current monitor.")
                return

            video_mode = glfw.get_video_mode(monitor)
            if not video_mode:
                print(
                    f"Error: Could not get video mode for monitor {monitor}.")
                return

            glfw.set_window_monitor(
                self.window,
                monitor,
                0,  # X position (typically 0 for fullscreen)
                0,  # Y position (typically 0 for fullscreen)
                int(video_mode.size.width),
                int(video_mode.size.height),
                int(video_mode.refresh_rate)
            )
            self.is_fullscreen = True
            print(
                f"Switched to fullscreen mode on monitor: {glfw.get_monitor_name(monitor)}.")

    def run(self):
        """
        Starts the main application loop.

        This method makes the window's OpenGL context current, sets up rendering,
        and continuously processes events, clears the screen, draws content,
        and swaps buffers until the window is closed.
        """
        glfw.make_context_current(self.window)

        # Initialize a textured quad (placeholder for actual scene objects)
        textured_quad = TexturedQuad("texture.png", [
            (0, 0.5),    # Top-left
            (0.5, 0.5),  # Top-right
            (0.5, 0),    # Bottom-right
            (0, 0)       # Bottom-left
        ])

        # Set the clear color (white in this case)
        glClearColor(1.0, 1.0, 1.0, 1.0)  # R, G, B, Alpha

        # Main loop: continues until the user closes the window
        while not glfw.window_should_close(self.window):
            # Poll for and process events (keyboard, mouse, window, etc.)
            glfw.poll_events()

            # Clear the color buffer
            glClear(GL_COLOR_BUFFER_BIT)

            # Draw the textured quad
            # This part would typically involve more complex scene rendering logic
            textured_quad.draw()

            # Swap the front and back buffers to display the rendered image
            glfw.swap_buffers(self.window)

        # Terminate GLFW when the loop exits (window is closed)
        glfw.terminate()
        print("GLFW terminated.")
