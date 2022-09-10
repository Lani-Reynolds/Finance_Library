from tkinter import Text, Button
from tkinter.ttk import Frame, Label, Style

import __main__

def Order_Recorder(container):
    OrderRecorderMainFrame = Frame(container, style='OrderRecorderMainFrameStyle.TFrame')
    OrderRecorderTitle = Label(OrderRecorderMainFrame, text="Enter order below", anchor='center', style='OrderRecorderTitleStyle.TLabel', padding=40)
    OrderInputSection = Text(OrderRecorderMainFrame, width=60, height=15, foreground='#6c584c', background='#f0ead2', padx=10, pady=10)
    OrderBackButton = Button(OrderRecorderMainFrame, activeforeground='#f0ead2', activebackground='#adc178', fg='#f0ead2', bg='#adc178', padx=10, pady=10, text='Back', command=lambda: __main__.Main_Frame(container))
    OrderRecorderMainFrameStyle = Style()
    OrderRecorderTitleStyle = Style()
    
    OrderRecorderMainFrameStyle.configure('OrderRecorderMainFrameStyle.TFrame', background='#6c584c')
    OrderRecorderTitleStyle.configure('OrderRecorderTitleStyle.TLabel', foreground='#dde5b6', background='#a98467', font=('Calibri Light', 50))
    OrderInputSection.configure(font=('Calibri Light', 15))
    OrderBackButton.configure(font=('Calibri Light', 20))
    
    OrderRecorderMainFrame.grid(column=0, row=0, columnspan=2, sticky='nsew')
    OrderRecorderTitle.grid(column=0, row=0, columnspan=2, sticky='ew')
    OrderInputSection.grid(column=0, row=1, columnspan=2)
    OrderBackButton.grid(column=0, row=2)
    
    OrderRecorderMainFrame.grid_columnconfigure(0, weight=1)
    OrderRecorderMainFrame.grid_columnconfigure(1, weight=5)
    OrderRecorderMainFrame.grid_rowconfigure(1, weight=3)
    OrderRecorderMainFrame.grid_rowconfigure(2, weight=2)
    