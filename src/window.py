import glfw
from OpenGL.GL import *
from PIL import Image
import sys

def load_texture(path):
    image = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM).convert("RGBA")
    img_data = image.tobytes()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGBA,
        image.width, image.height, 0,
        GL_RGBA, GL_UNSIGNED_BYTE, img_data
    )

    glGenerateMipmap(GL_TEXTURE_2D)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glEnable(GL_TEXTURE_2D)

    return texture_id

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

        texture = load_texture("texture.png")

        glClearColor(1,1,1,1)        

        while not glfw.window_should_close(self.window):

            glfw.poll_events()
            
            glClear(GL_COLOR_BUFFER_BIT)

            glBindTexture(GL_TEXTURE_2D, texture)

            glBegin(GL_POLYGON)
            glTexCoord2f(0.0, 0.0); glVertex2f(-0.5, -0.5)   # Abajo izquierda
            glTexCoord2f(1.0, 0.0); glVertex2f( 0.5, -0.5)   # Abajo derecha
            glTexCoord2f(1, 1.0); glVertex2f( 0.3,  0.5)  # Arriba derecha (más estrecha)
            glTexCoord2f(0, 1.0); glVertex2f(-0.3,  0.5)  # Arriba izquierda (más estrecha)
            glEnd()



            glfw.swap_buffers(self.window)

        glfw.terminate()