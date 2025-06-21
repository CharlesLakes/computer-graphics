import glfw


class Events:
    def __init__(self, window):
        self.window = window

    def events_setting(self):
        # Set up key callback
        glfw.set_key_callback(self.window.window, self.key_callback)

        # Cursor position
        glfw.set_cursor_pos_callback(self.window.window, self.cursor_callback)

    def cursor_callback(self, window, xpos, ypos):
        print("X:", xpos)
        print("Y:", ypos)

    def key_callback(self, window, key, scancode, action, mods):
        """Callback to handle keyboard events"""
        if key == glfw.KEY_F11 and action == glfw.PRESS:
            self.window.toggle_fullscreen()
