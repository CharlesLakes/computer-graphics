# OpenGL Textured Quad Demo

This project is a simple demonstration of rendering a textured quadrilateral using Python, OpenGL, and GLFW. It showcases basic window creation, event handling, texture loading, and rendering.

## Features

*   **Window Management**: Uses GLFW to create and manage an OpenGL window.
*   **Event Handling**: Basic keyboard input for closing the window (ESC) and toggling fullscreen (F11). Mouse cursor position is printed to the console.
*   **Texture Loading**: Loads a texture from an image file (`texture.png`) using Pillow and applies it to a 2D quad.
*   **Rendering**: Renders the textured quad using immediate mode OpenGL.

## Prerequisites

*   Python 3.x
*   An environment that supports OpenGL.

## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    Install the required packages using the `Makefile`:
    ```bash
    make install
    ```
    Alternatively, you can install them directly using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the demo, use the `Makefile`:
```bash
make run
```
Alternatively, you can run the main script directly:
```bash
python main.py
```

## Development

### Code Formatting and Linting

This project uses `autopep8` for code formatting to ensure PEP8 compliance.

*   **Check for PEP8 compliance:**
    ```bash
    make lint
    ```
*   **Automatically format code:**
    ```bash
    make format
    ```

## Project Structure

*   `main.py`: Entry point of the application. Initializes the display and input handlers.
*   `src/`: Contains the core modules.
    *   `window.py`: Manages the GLFW window, OpenGL context, and the main rendering loop (`DisplayManager` class).
    *   `events.py`: Handles user input (keyboard, mouse) via the `InputHandler` class.
    *   `face.py`: Defines the `TexturedQuad` class responsible for loading and drawing the textured quadrilateral.
*   `texture.png`: Sample texture file used for the demo. (Assumed to exist, or the user needs to provide one).
*   `requirements.txt`: Lists Python dependencies.
*   `Makefile`: Contains commands for installation, running the application, and code linting/formatting.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
