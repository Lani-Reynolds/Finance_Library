from tkinter import Text, Button
from tkinter.ttk import Frame, Label, Style

import __main__

def Sale_Recorder(container):
    SaleRecorderMainFrame = Frame(container, style='SaleRecorderMainFrameStyle.TFrame')
    SaleRecorderTitle = Label(SaleRecorderMainFrame, text="Enter sale below", anchor='center', style='SaleRecorderTitleStyle.TLabel', padding=40)
    SaleInputSection = Text(SaleRecorderMainFrame, background='#f0ead2')
    SaleBackButton = Button(SaleRecorderMainFrame, activeforeground='#f0ead2', activebackground='#adc178', fg='#f0ead2', bg='#adc178', padx=10, pady=10, text='Back', command=lambda: __main__.Main_Frame(container))
    SaleRecorderMainFrameStyle = Style()
    SaleRecorderTitleStyle = Style()
    
    SaleRecorderMainFrameStyle.configure('SaleRecorderMainFrameStyle.TFrame', background='#6c584c')
    SaleRecorderTitleStyle.configure('SaleRecorderTitleStyle.TLabel', foreground='#dde5b6', background='#a98467', font=('Calibri Light', 50))
    SaleBackButton.configure(font=('Calibri Light', 20))
    
    SaleRecorderMainFrame.grid(column=0, row=0, columnspan=2, sticky='nsew')
    SaleRecorderTitle.grid(column=0, row=0, columnspan=2, sticky='ew')
    SaleInputSection.grid(column=0, row=1, columnspan=2)
    SaleBackButton.grid(column=0, row=2)
    
    SaleRecorderMainFrame.grid_columnconfigure(0, weight=1)
    SaleRecorderMainFrame.grid_columnconfigure(1, weight=5)
    SaleRecorderMainFrame.grid_rowconfigure(1, weight=3)
    SaleRecorderMainFrame.grid_rowconfigure(2, weight=2)