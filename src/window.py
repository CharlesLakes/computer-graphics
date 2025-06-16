import glfw
from OpenGL.GL import *
import sys
from src.face import Face

class Window:
    def __init__(self, width, height, title):
        if not glfw.init():
            print("Error: GLFW cannot init")
            sys.exit(1)
        
        # Original window specs
        self.original_width = width
        self.original_height = height
        self.title = title
        self.is_fullscreen = False
        
        self.window = glfw.create_window(
            width,
            height,
            title,
            None,
            None
        )
        
        if not self.window:
            print("Error: window not make")
            sys.exit(1)
            
        # Configurar callback para teclas
        glfw.set_key_callback(self.window, self.key_callback)
    
    def key_callback(self, window, key, scancode, action, mods):
        """Callback para manejar eventos de teclado"""
        if key == glfw.KEY_F11 and action == glfw.PRESS:
            self.toggle_fullscreen()
    
    def toggle_fullscreen(self):
        """Alternar entre modo ventana y pantalla completa"""
        if self.is_fullscreen:
            # Cambiar a modo ventana
            glfw.set_window_monitor(
                self.window,
                None,  # No monitor (modo ventana)
                100,   # Posición X
                100,   # Posición Y
                self.original_width,
                self.original_height,
                0      # Refresh rate (0 = don't care)
            )
            self.is_fullscreen = False
        else:
            # Cambiar a pantalla completa
            monitor = glfw.get_primary_monitor()
            video_mode = glfw.get_video_mode(monitor)
            
            glfw.set_window_monitor(
                self.window,
                monitor,
                0,  # Posición X
                0,  # Posición Y
                int(video_mode.size.width),   # width convertido a int
                int(video_mode.size.height),  # height convertido a int
                int(video_mode.refresh_rate)  # refresh_rate convertido a int
            )
            self.is_fullscreen = True
    
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