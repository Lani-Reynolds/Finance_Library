from tkinter import Button
from tkinter.ttk import Frame, Label, Style

from TableBuilder import Table_Builder

import __main__

def Log_Sale(container, past_frame):
    SaleMainFrame = Frame(container, style='SaleMainFrameStyle.TFrame')
    SaleTitle = Label(SaleMainFrame, text="Enter sale below", anchor='center', style='SaleTitleStyle.TLabel', padding=40)
    SaleTable = Table_Builder(SaleMainFrame, 5, 5)
    SaleBackButton = Button(SaleMainFrame, activeforeground='#f0ead2', activebackground='#adc178', fg='#f0ead2', bg='#adc178', padx=10, pady=10, text='Back', command=lambda: __main__.Main_Frame(container, SaleMainFrame))
    SaleMainFrameStyle = Style()
    SaleTitleStyle = Style()
    
    SaleMainFrameStyle.configure('SaleMainFrameStyle.TFrame', background='#6c584c')
    SaleTitleStyle.configure('SaleTitleStyle.TLabel', foreground='#dde5b6', background='#a98467', font=('Calibri Light', 50))
    SaleBackButton.configure(font=('Calibri Light', 20))
    
    SaleMainFrame.grid(column=0, row=0, sticky='nsew')
    SaleTitle.grid(column=0, row=0, sticky='new')
    SaleTable.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')
    SaleBackButton.grid(column=0, row=2, padx=10, pady=10, sticky='sw')
    
    SaleMainFrame.columnconfigure(0, weight=1)
    SaleMainFrame.rowconfigure(0, weight=1)
    SaleMainFrame.rowconfigure(1, weight=5)
    SaleMainFrame.rowconfigure(2, weight=1)