from tkinter import *

# toplevel window 
root = Tk() 

# Method to make Button(Widget) invisible from toplevel
def hide_button(widget): 
    # This will destroy the widget
    widget.destroy()

# Method to make Button(widget) visible
def show_button(): 
    # Recreate the button
    global B1
    B1 = Button(root, text="B1")
    B1.pack()

# Button widgets 
B1= Button(root, text="B1") 
B1.pack() 

# See, in command hide_button() function is passed to hide Button B1 
B2 = Button(root, text="Close Chat", command=lambda: hide_button(B1)) 
B2.pack() 

# In command show_button() function is passed to recover Button B1 
B3 = Button(root, text="Show Chat", command=show_button) 
B3.pack() 

root.mainloop()

