import glfw
from OpenGL.GL import *
import sys
from src.face import Face

class Window:
    def __init__(self, width, height, title):
        if not glfw.init():
            print("Error: GLFW cannot init")
            sys.exit(1)
        
        # Guardar dimensiones originales de la ventana
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
    
    def get_current_monitor(self):
        """Obtener el monitor donde está actualmente la ventana"""
        # Obtener posición de la ventana
        win_x, win_y = glfw.get_window_pos(self.window)
        win_width, win_height = glfw.get_window_size(self.window)
        
        # Calcular el centro de la ventana
        win_center_x = win_x + win_width // 2
        win_center_y = win_y + win_height // 2
        
        monitors = glfw.get_monitors()
        
        for monitor in monitors:
            # Obtener posición y tamaño del monitor
            mon_x, mon_y = glfw.get_monitor_pos(monitor)
            video_mode = glfw.get_video_mode(monitor)
            mon_width = int(video_mode.size.width)
            mon_height = int(video_mode.size.height)
            
            # Verificar si el centro de la ventana está dentro de este monitor
            if (mon_x <= win_center_x < mon_x + mon_width and
                mon_y <= win_center_y < mon_y + mon_height):
                return monitor
        
        # Si no se encuentra, usar el monitor primario como fallback
        return glfw.get_primary_monitor()

    def toggle_fullscreen(self):
        """Alternar entre modo ventana y pantalla completa en el monitor actual"""
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
            # Cambiar a pantalla completa en el monitor actual
            monitor = self.get_current_monitor()
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