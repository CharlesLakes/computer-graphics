from PIL import Image
from OpenGL.GL import *


class Face:
    def __init__(self, path, all_vertex):
        self.load_texture(path)
        self.all_vertex = all_vertex

    def load_texture(self, path):
        image = Image.open(path).transpose(
            Image.FLIP_TOP_BOTTOM).convert("RGBA")
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

        glTexParameteri(
            GL_TEXTURE_2D,
            GL_TEXTURE_MIN_FILTER,
            GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glEnable(GL_TEXTURE_2D)

        self.texture = texture_id

    def draw(self):
        texture_coords = [
            (0, 1),
            (1, 1),
            (1, 0),
            (0, 0)
        ]

        glBindTexture(GL_TEXTURE_2D, self.texture)

        glBegin(GL_POLYGON)
        for i in range(4):
            x, y = self.all_vertex[i]
            u, v = texture_coords[i]

            glTexCoord2f(u, v)
            glVertex2f(x, y)
        glEnd()
