from tkinter import *
from tkinter import ttk

class OrderRecorder:
    
    def __init__(self, root_container):
        OrderRecorderMainFrame = ttk.Frame(root_container, padding="5 5 12 12")
        OrderRecorderMainFrame.columnconfigure(0, weight=1)
        OrderRecorderMainFrame.rowconfigure(0, weight=1)
        OrderRecorderMainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    
        ttk.Label(OrderRecorderMainFrame, text="Enter order below:").grid(column=0, row=0)
