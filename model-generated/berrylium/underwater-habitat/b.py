from tkinter import *
import tkinter as tk
from tkinter import ttk
import math

# We will use this class as a parent class for all modules (Living, Research, Cultivation)
class Module:
    def __init__(self, name, efficiency=0.5):
        self.name = name       
        self.efficiency = efficiency # Overall efficiency of the module (can be adjusted by user)

#Different modules of habitat
class LivingModule(Module):
    def __init__(self, name, oxygen_requirement=2, water_requirement=10):
        super().__init__(name)        
        self.oxygen_requirement = oxygen_requirement
        self.water_requirement = water_requirement


class ResearchModule(Module):
    def __init__(self, name, power_consumption=15):
       super().__init__(name)        
       self.power_consumption = power_consumption       

class CultivationModule(Module):
    def __init__(self, name, seed_count=100, nutrient_requirement=20):
        super().__init__(name)        
        self.seed_count = seed_count
        self.nutrient_requirement = nutrient_requirement


class Habitat: 
    def __init__(self):
       self.modules = {}  # To store instances of different modules

       # User can add/remove modules later
       self.add_module("Living", LivingModule)
       self.add_module("Research", ResearchModule)
       self.add_module("Cultivation", CultivationModule)  

       # Default variables for habitat
       self.depth = 10  # Depth in meters
       self.light = 100  # Light intensity in lumens
       self.pressure = 1.0  # Pressure at depth (in atmospheres)
       self.marine_ecosystem_proximity = 500  # Distance from other marine ecosystems in meters

    def add_module(self, name, module_type):
        self.modules[name] = module_type(name) 

    def simulate(self): 
        # This function will run the simulation and calculate various factors.
        # We'll keep it simple for now and just calculate the total efficiency of the habitat.
        total_efficiency = 1.0
        for _, module in self.modules.items():
            total_efficiency *= module.efficiency
        
        # Calculate and display other factors based on user input
        self.calculate_stress()
        self.calculate_local_environment_impact()
        return total_efficiency

    def calculate_stress(self): 
        # A simple formula for calculating structural stress based on depth and pressure.
        # You can modify this based on more complex considerations.
        stress = 0.5 * self.depth * (self.pressure - 1.0)
        print(f"Structural Stress: {stress} bars")

    def calculate_local_environment_impact(self): 
        # A simple formula for calculating impact on local environment.
        impact = self.marine_ecosystem_proximity / (self.light + self.depth)
        print(f"Impact on Local Marine Ecosystem: {impact}")
 
        # Display more detailed results based on user input  

 
 # GUI Design:        
class HabitatDesigner(Tk): 
    def __init__(self):      
        super().__init__()
        self.title("Underwater Habitat Simulator")        
        self.habitat = Habitat() # Instantiate the Habitat class
        
        # Frame to organize widgets
        main_frame = tk.Frame(self)
        main_frame.pack(padx=20, pady=20)       

        #*********** User Input Frames ***************      
        # Frame for Habitat Variables
        habitat_var_frame = Frame(main_frame)
        habitat_var_frame.pack(fill=X, expand=1)

        # Labels and Entries for Habitat Variables
        depth_label = tk.Label(habitat_var_frame, text="Depth (in meters):")
        depth_label.grid(row=0, column=0)
        self.depth_entry = tk.Entry(habitat_var_frame, width=10)
        self.depth_entry.grid(row=0, column=1)        
        
        # Buttons to run simulation and reset values
        simulate_button = tk.Button(main_frame, text="Simulate", command=self.simulate_habitat)
        simulate_button.pack(pady=10)

        reset_button = tk.Button(main_frame, text="Reset", command=self.reset_values)      
        reset_button.pack(pady=10)         


       # *********** Results Display Frame *************
        result_frame = Frame(main_frame)
        result_frame.pack()

        self.result_label = tk.Label(result_frame, text="Habitat Efficiency: ")
        self.result_label.pack(anchor=W)      

    def simulate_habitat(self): 
        # Update habitat variables from user input
        self.habitat.depth = float(self.depth_entry.get())      
        # Run the simulation
        efficiency = self.habitat.simulate()     
        self.result_label.config(text=f"Habitat Efficiency: {efficiency * 100:.2f}%")

      # Display other results
        #........

    def reset_values(self): 
        # Reset entries and other variables
        self.depth_entry.delete(0, END)
        self.depth_entry.insert(0, "10")
        #...........

def main():  
    designer = HabitatDesigner()  
    designer.mainloop()

if __name__ == "__main__":
    main()  