import glfw
from OpenGL.GL import *
import sys

class Window:
    def __init__(self,width, height, title):

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

        

        while not glfw.window_should_close(self.window):

            glfw.poll_events()
            
            glClearColor(0,0,0,1)
            glClear(GL_COLOR_BUFFER_BIT)

            

            glfw.swap_buffers(self.window)

        glfw.terminate()