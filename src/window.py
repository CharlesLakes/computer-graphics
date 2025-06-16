import glfw
from OpenGL.GL import *
import sys
from src.face import Face

class Window:
    def __init__(self, width, height, title):
        if not glfw.init():
            print("Error: GLFW cannot init")
            sys.exit(1)
        
        # Store original window dimensions
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
            
        # Set up key callback
        glfw.set_key_callback(self.window, self.key_callback)
    
    def key_callback(self, window, key, scancode, action, mods):
        """Callback to handle keyboard events"""
        if key == glfw.KEY_F11 and action == glfw.PRESS:
            self.toggle_fullscreen()
    
    def get_current_monitor(self):
        """Get the monitor where the window is currently located"""
        # Get window position
        win_x, win_y = glfw.get_window_pos(self.window)
        win_width, win_height = glfw.get_window_size(self.window)
        
        # Calculate window center
        win_center_x = win_x + win_width // 2
        win_center_y = win_y + win_height // 2
        
        monitors = glfw.get_monitors()
        
        for monitor in monitors:
            # Get monitor position and size
            mon_x, mon_y = glfw.get_monitor_pos(monitor)
            video_mode = glfw.get_video_mode(monitor)
            mon_width = int(video_mode.size.width)
            mon_height = int(video_mode.size.height)
            
            # Check if window center is within this monitor
            if (mon_x <= win_center_x < mon_x + mon_width and
                mon_y <= win_center_y < mon_y + mon_height):
                return monitor
        
        # If not found, use primary monitor as fallback
        return glfw.get_primary_monitor()

    def toggle_fullscreen(self):
        """Toggle between windowed and fullscreen mode on current monitor"""
        if self.is_fullscreen:
            # Switch to windowed mode
            glfw.set_window_monitor(
                self.window,
                None,  # No monitor (windowed mode)
                100,   # X position
                100,   # Y position
                self.original_width,
                self.original_height,
                0      # Refresh rate (0 = don't care)
            )
            self.is_fullscreen = False
        else:
            # Switch to fullscreen on current monitor
            monitor = self.get_current_monitor()
            video_mode = glfw.get_video_mode(monitor)
            
            glfw.set_window_monitor(
                self.window,
                monitor,
                0,  # X position
                0,  # Y position
                int(video_mode.size.width),   # width converted to int
                int(video_mode.size.height),  # height converted to int
                int(video_mode.refresh_rate)  # refresh_rate converted to int
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