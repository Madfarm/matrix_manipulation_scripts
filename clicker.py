import tkinter as tk
import threading
import time
from pynput.mouse import Button, Controller

class AutoClicker:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("Auto Clicker")

    self.click_rate_label = tk.Label(self.root, text="Click Rate (CPS):")
    self.click_rate_entry = tk.Entry(self.root)

    self.click_delay_label = tk.Label(self.root, text="Click Delay (ms):")
    self.click_delay_entry = tk.Entry(self.root)

    self.running = False  # Flag to track autoclicker state

    self.start_button = tk.Button(self.root, text="Start", command=self.toggle_autoclicker)
    self.stop_button = tk.Button(self.root, text="Stop", command=self.toggle_autoclicker)  # Use the same function
    self.click_rate_label.grid(row=0, column=0)
    self.click_rate_entry.grid(row=0, column=1)

    self.click_delay_label.grid(row=1, column=0)
    self.click_delay_entry.grid(row=1, column=1)

    self.start_button.grid(row=2, column=0)
    self.stop_button.grid(row=2, column=1)

    self.mouse = Controller()

    self.root.mainloop()

  def toggle_autoclicker(self):  # Combined functionality to start/stop
        if self.running:
            self.stop_autoclicker()
        else:
            self.start_autoclicker()

  def start_autoclicker(self):
        click_rate = int(self.click_rate_entry.get())
        click_delay = int(self.click_delay_entry.get())

        self.running = True   # Set flag to True 
        self.start_button.config(text="Stop")  # Update button text

        while self.running:  # Continue clicking only if running is True
            self.mouse.click(Button.left)
            time.sleep(1 / click_rate)

  def stop_autoclicker(self):
        self.running = False  # Set flag to False
        self.start_button.config(text="Start")  # Update button text

if __name__ == "__main__":
    autoclicker = AutoClicker()