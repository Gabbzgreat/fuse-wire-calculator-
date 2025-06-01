import tkinter
from tkinter import messagebox,ttk



WIRE_CURRENT_RATINGS = {
    0.75: 4,
    1.0: 6,
    1.5: 10,
    2.5: 15,
    4.0: 25,
    6.0: 40,
    10.0: 60
}

VOLTAGE_DROP_PERCENT = {
    'charging': 3.5,
    'starting': 6.0,
    'other': 10.0
}

# Constants
COPPER_RESISTIVITY = 0.0178  # Ωmm²/m
ALUMINIUM_RESISTIVITY = 0.0283  # Ωmm²/m
VOLTAGE_DROP_COEFFICIENT = 1.3  # Middle of 1.1-1.6 range
SYSTEM_VOLTAGE = 12  #


TYPE_LIST = ['charging','starting','other']
WIRE_MATERIAL = ["copper","aluminium"]

root = tkinter.Tk()



def OnClick_Submit():
    LoadC = LoadC_textbox.get()
    CircuitType = CircuitType_dropdown.get()
    WireMaterial = WireMaterial_dropdown.get()
   
    
    if LoadC and CircuitType and WireMaterial :
        try:
         load_current = int(LoadC)
         if load_current > 60:
            messagebox.showwarning("Overcurrent", "Overcurrent, Your current is above 60Amps.")

         elif CircuitType.lower() not in TYPE_LIST:
            messagebox.showwarning("Invalid" ," Invalid  Circuit Type")

         elif WireMaterial.lower() not in WIRE_MATERIAL:
            messagebox.showwarning("Invalid","Invalid Wire Material")
         else:
            voltage_drop_percent = VOLTAGE_DROP_PERCENT[CircuitType]
            
             # resistivity based on material
            resistivity = COPPER_RESISTIVITY if WireMaterial == 'copper' else ALUMINIUM_RESISTIVITY
             
           
            recommended_wire = None
            for size, max_current in sorted(WIRE_CURRENT_RATINGS.items()):
               if max_current >= load_current :
                   recommended_wire = size
                   break
               
            # 2. Calculating maximum wire length with selected material
            max_length = (voltage_drop_percent * SYSTEM_VOLTAGE * recommended_wire) / \
                    (100 * VOLTAGE_DROP_COEFFICIENT * load_current * resistivity)
            
             # 3. Calculate fuse rating
            fuse_rating = load_current / 0.75

            # Round up fuse to standard values
            standard_fuses = [6, 10, 16, 25, 32, 40, 50, 60, 80, 100]
            recommended_fuse = min((f for f in standard_fuses if f >= fuse_rating), default=100)
         
        
        
           # message = f"Load Current: {load_current}\nCircuit Type: {CircuitType}\nWire Material: {WireMaterial}"
            message = (
               f"Recommended wire size:  {recommended_wire} mm²\n"
               f"Wire material: {WireMaterial.capitalize()}\n"
               f"Maximum wire length: {max_length:.2f} meters\n"
               f"Minimum fuse rating: {fuse_rating:.1f}A\n"
               f"Recommended standard fuse: {recommended_fuse}A"
            )
            messagebox.showinfo("Captured Data", message)
        except ValueError:
           messagebox.showwarning("Invalid Input", "Please enter a valid integer for Load Current.")

    else:
        messagebox.showwarning("Incomplete Data", "Please fill all the boxes.")

   
   # if LoadC and CircuitType and WireMaterial :
   # message = f"Load Current: {LoadC}\nCircuit Type: {CircuitType}\nWire Material: {WireMaterial}"
    # messagebox.showinfo("Captured Data", message)

    #else:
      #  messagebox.showwarning("Incomplete Data", "Please fill all the boxes.")'''



root.geometry("500x400")
root.title("Car Fuse + Wire Calculator")


# Load current
LoadC_label = tkinter.Label(root, text="Enter Load Current")
LoadC_label.pack(anchor=tkinter.W, padx=10)

LoadC_textbox = tkinter.Entry(root)
LoadC_textbox.pack(anchor=tkinter.W, padx=10)

#drop down circuit type
choices=['charging','starting','other']
CircuitType_label = tkinter.Label(root,text='select a circuit type')
CircuitType_label.pack(anchor=tkinter.W,padx=10)
CircuitType_dropdown=ttk.Combobox(root,values=choices)
CircuitType_dropdown.pack(anchor=tkinter.W, padx=10)


# drop down Wire material
choices2=['copper','aluminium']
WireMaterial_label = tkinter.Label(root,text='select  wire material')
WireMaterial_label.pack(anchor=tkinter.W,padx=10)
WireMaterial_dropdown=ttk.Combobox(root,values=choices2)
WireMaterial_dropdown.pack(anchor=tkinter.W, padx=10)


# Submit Button
Calculate_button = tkinter.Button(root, text="Calculate", command=OnClick_Submit)
Calculate_button.pack(anchor=tkinter.W, padx=10)


root.mainloop()