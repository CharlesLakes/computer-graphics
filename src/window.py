import glfw
from OpenGL.GL import *
import sys
from src.face import Face


class Window:
    def __init__(self, width, height, title):

        if not glfw.init():
            print("Error: GLFW cannot init")
            sys.exit(1)

        self.window = glfw.create_window(
            width,
            height,
            title,
            None,
            None
        )

        if not self.window:
            print("Error: window not make")

    def run(self):
        glfw.make_context_current(self.window)

        face = Face("texture.png", [
            (0, 0.5),
            (0.5, 0.5),
            (0.5, 0),
            (0, 0)
        ])

        glClearColor(1, 1, 1, 1)

        while not glfw.window_should_close(self.window):

            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT)

            face.draw()

            glfw.swap_buffers(self.window)

        glfw.terminate()
