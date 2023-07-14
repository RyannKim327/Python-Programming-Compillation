import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a style object
style = ttk.Style()

# Configure the TLabelFrame element with border radius
style.configure('TLabelFrame', borderwidth=100, relief='solid', padding=10, borderradius=100)

# Create a LabelFrame widget using the configured style
label_frame = tk.LabelFrame(root, text='My Label Frame')
label_frame.pack(padx=20, pady=20)

# Add other widgets inside the LabelFrame
label = ttk.Label(label_frame, text='Hello World')
label.pack(padx=10, pady=10)

root.mainloop()