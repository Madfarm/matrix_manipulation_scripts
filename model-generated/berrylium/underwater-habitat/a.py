import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import math

class UnderwaterHabitat(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Underwater Habitat Simulator")
        self.geometry("1000x600")
        
        # Initialize habitat variables
        self.depth = 0
        self.light = 0
        self.pressure = 0
        self.ecosystem_proximity = 0
        
        # Dictionary to store modules and their associated frames
        self.modules = {}
        
        # Create main frames for different tabs
        self.nb = ttk.Notebook(self)
        self.nb.pack(expand=1, fill="both")
        
        self.create_habitat_frame()
        self.create_simulation_frame()
        self.select_module_tab()  # Initial module selection

    def create_habitat_frame(self):
            habitat_frame = tk.Frame(self.nb)
            self.nb.add(habitat_frame, text="Habitat Design")
            
            # Label and entry fields for user input
            habitat_vars = [("Depth (m):", 0, 100),        ("Light intensity (lux):", 0, 10000),
                        ("Pressure (atm):", 0, 10),  ("Proximity to Ecosystem (km):", 0, 5)]
            
            for text, min_, max_ in habitat_vars:
                tk.Label(habitat_frame, text=text).grid(row=habitat_vars.index((text,min_,max_))+1, column=0)
                var = tk.DoubleVar(habitat_frame, min_value=min_, max_value=max_, value=0)
                entry = tk.Entry(habitat_frame, textvariable=var)
                entry.grid(row=habitat_vars.index((text,min_,max_))+1, column=1)
                var.trace_add("write", self.update_habitat_vars)
                self.modules["Habitat Design"][text] = var, entry

    