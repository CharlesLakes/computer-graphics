import glfw

# Handles user input events, such as keyboard and mouse.


class InputHandler:
    def __init__(self, display_manager):
        """
        Initializes the InputHandler.

        Args:
            display_manager (DisplayManager): The display manager instance to interact with.
                                             This is used, for example, to toggle fullscreen.
        """
        self.display_manager = display_manager

    def setup_callbacks(self):
        """
        Sets up the GLFW input callbacks for the window.
        This connects GLFW events to the handler methods in this class.
        """
        # Set the key callback
        # The window object is accessed from the display_manager
        glfw.set_key_callback(self.display_manager.window, self._key_callback)

        # Set the cursor position callback
        glfw.set_cursor_pos_callback(
            self.display_manager.window, self._cursor_callback)

    def _cursor_callback(self, window, xpos, ypos):
        """
        Callback for mouse cursor position events.

        Args:
            window: The GLFW window that received the event.
            xpos (float): The new x-coordinate, in screen coordinates, of the cursor.
            ypos (float): The new y-coordinate, in screen coordinates, of the cursor.
        """
        # Currently, this just prints the cursor position.
        # Could be extended for camera control, UI interaction, etc.
        print(f"Cursor Position: X={xpos:.2f}, Y={ypos:.2f}")

    def _key_callback(self, window, key, scancode, action, mods):
        """
        Callback for keyboard key events.

        Args:
            window: The GLFW window that received the event.
            key (int): The keyboard key that was pressed or released.
            scancode (int): The system-specific scancode of the key.
            action (int): GLFW.PRESS, GLFW.RELEASE or GLFW.REPEAT.
            mods (int): Bit field describing which modifier keys were held down.
        """
        # Example: Toggle fullscreen when F11 is pressed
        if key == glfw.KEY_F11 and action == glfw.PRESS:
            self.display_manager.toggle_fullscreen()

        # Example: Close window on ESC press
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window, True)
