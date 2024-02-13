import tkinter as tk
from PIL import Image, ImageTk
import pyautogui

def overlay_image(image_path):
    """Overlays the image at the specified path on top of all windows."""

    # Set up a transparent window using Tkinter
    root = tk.Tk()
    root.attributes('-topmost', True)


    # Open the image using PIL
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Use a label to display the image in the transparent window
    label = tk.Label(root, image=photo, bg='white')
    label.pack()

    # Get screen dimensions and calculate position to center the image
    screen_width, screen_height = pyautogui.size()
    image_width, image_height = image.size
    x = (screen_width - image_width) // 2
    y = (screen_height - image_height) // 2

    # Position the window and run
    root.geometry(f'+{x}+{y}')
    root.mainloop()

# Example usage:
overlay_image("image.png")