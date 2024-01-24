import tkinter as tk
from pynput.mouse import Button, Controller
import keyboard
import threading
import time

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
       click_thread = threading.Thread(target=self.run_autoclicker)
       click_thread.start()

  def run_autoclicker(self):
       click_rate = int(self.click_rate_entry.get())
       click_delay = int(self.click_delay_entry.get())

       while True:
           self.mouse.click(Button.left)
           time.sleep(click_delay / 1000)  # Convert delay to seconds

  def stop_autoclicker(self):
       global click_thread
       if click_thread.is_alive():
           click_thread.join()  # Wait for the thread to finish

   # Make click_thread a global variable
  click_thread = None

if __name__ == "__main__":
    autoclicker = AutoClicker()

