from PIL import Image
from OpenGL.GL import *

# Represents a 2D quadrilateral (four vertices) with an applied texture.
class TexturedQuad:
    def __init__(self, texture_path, vertices):
        """
        Initializes the TexturedQuad.

        Args:
            texture_path (str): The file path to the texture image.
            vertices (list of tuples): A list of four (x, y) tuples defining the
                                       quadrilateral's vertex positions in 2D space.
                                       The order should be suitable for drawing with GL_POLYGON,
                                       typically counter-clockwise: bottom-left, bottom-right,
                                       top-right, top-left.
        """
        self.texture_id = self._load_texture(texture_path)
        self.vertices = vertices # Expects 4 vertices, e.g., [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]

        # Standard texture coordinates for a quad. These map the corners of the texture
        # to the vertices of the quad. The order here corresponds to a typical vertex order:
        # (0,0) bottom-left, (1,0) bottom-right, (1,1) top-right, (0,1) top-left of the texture.
        # This might need adjustment if vertex order is different.
        self.texture_coords = [
            (0.0, 0.0),  # Corresponds to vertices[0]
            (1.0, 0.0),  # Corresponds to vertices[1]
            (1.0, 1.0),  # Corresponds to vertices[2]
            (0.0, 1.0)   # Corresponds to vertices[3]
        ]


    def _load_texture(self, path):
        """
        Loads a texture from an image file and prepares it for OpenGL.

        Args:
            path (str): The file path to the image.

        Returns:
            int: The OpenGL texture ID.
        """
        try:
            # Open the image using Pillow, flip it vertically (OpenGL expects origin at bottom-left),
            # and convert to RGBA format.
            image = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM).convert("RGBA")
            img_data = image.tobytes() # Get image data as bytes
        except FileNotFoundError:
            print(f"Error: Texture file not found at '{path}'")
            # Consider raising an exception or returning a default texture ID
            return 0 # Or some indicator of failure

        # Generate a new texture ID
        texture_id = glGenTextures(1)
        # Bind the new texture, making it the active GL_TEXTURE_2D
        glBindTexture(GL_TEXTURE_2D, texture_id)

        # Set pixel storage mode (byte-alignment)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        # Upload the texture data to OpenGL
        glTexImage2D(
            GL_TEXTURE_2D,    # Target texture type
            0,                # Level-of-detail number (0 for base image level)
            GL_RGBA,          # Internal format (how OpenGL stores the texture)
            image.width,      # Width of the texture
            image.height,     # Height of the texture
            0,                # Border (must be 0)
            GL_RGBA,          # Format of the pixel data being supplied
            GL_UNSIGNED_BYTE, # Data type of the pixel data
            img_data          # The image data itself
        )

        # Generate mipmaps for the texture. Mipmaps are pre-calculated, lower-resolution
        # versions of the texture, which improve rendering quality and performance
        # when the texture is viewed from a distance or at an angle.
        glGenerateMipmap(GL_TEXTURE_2D)

        # Set texture filtering parameters.
        # GL_LINEAR_MIPMAP_LINEAR uses linear interpolation for minification across mipmap levels,
        # and linear interpolation within a mipmap level. This provides good quality.
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        # GL_LINEAR uses linear interpolation for magnification.
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Enable 2D texturing (though this is often enabled globally or per shader)
        # Depending on the rendering pipeline, this might not be strictly necessary here
        # if managed elsewhere (e.g., in a shader or global state).
        # glEnable(GL_TEXTURE_2D) # This is often managed by the shader or render state

        return texture_id

    def draw(self):
        """
        Draws the textured quadrilateral using immediate mode OpenGL.
        Note: Immediate mode (glBegin/glEnd) is deprecated in modern OpenGL.
              For new projects, consider using Vertex Buffer Objects (VBOs) and shaders.
        """
        if not self.texture_id: # Don't draw if texture loading failed
            return

        # Bind the quad's texture, making it active for the subsequent drawing commands.
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glEnable(GL_TEXTURE_2D) # Ensure texturing is enabled for this draw call

        glBegin(GL_POLYGON) # Begin drawing a polygon
        for i in range(len(self.vertices)):
            # Get vertex coordinates (x, y)
            vertex_x, vertex_y = self.vertices[i]
            # Get texture coordinates (u, v)
            tex_u, tex_v = self.texture_coords[i]

            # Specify the texture coordinate for the current vertex
            glTexCoord2f(tex_u, tex_v)
            # Specify the vertex position
            glVertex2f(vertex_x, vertex_y)
        glEnd() # End drawing the polygon

        glDisable(GL_TEXTURE_2D) # Disable texturing after drawing this quad
        glBindTexture(GL_TEXTURE_2D, 0) # Unbind texture
