# This is run when you call it as a "program"
from CleanUp import PyCacheCleanUp

import tkinter as tk
from tkinter import HORIZONTAL, ttk

from OrderRecorder import OrderRecorder

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('My Awesome App')
        self.geometry('200x200')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=1)

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.grid(column=0, row=0)
        
        self.separator_frame = ttk.Frame(self)
        self.separator_frame.grid(column=0, row=1, sticky='nsew', pady=5)

        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.OrderRecorderButton
        self.button.grid(column=0, row=2)

        self.grid(column=0, row=0)

    def OrderRecorderButton(self):
        OrderRecorder(self)


if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
# main_frame = ttk.Frame(root, width=200, height=200, style='MainMenu.TFrame')
# main_frame_style = ttk.Style()
# title = ttk.Label(main_frame, text="Pick menu:", style='Title.TLabel')
# title_style = ttk.Style()
# order_recorder_button = ttk.Button(main_frame, text="Record an order", default="active", command=OrderRecorderCallback)

# root.title("Prosper")
# root.geometry("200x200")
# main_frame_style.configure('MainMenu.TFrame', background='aquamarine', borderwidth=5, relief='raised')
# title_style.configure('Title.TLabel', background='aquamarine')

# main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
# title.grid(column=0, row=0)
# order_recorder_button.grid(column=0, row=1)


# root.mainloop()
PyCacheCleanUp()