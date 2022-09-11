from tkinter import Button
from tkinter.ttk import Frame, Label, Style

from TableBuilder import Table_Builder

import __main__

def Log_Order(container, past_frame):
    del past_frame
    OrderMainFrame = Frame(container, style='OrderMainFrameStyle.TFrame')
    OrderTitle = Label(OrderMainFrame, text="Enter order below", anchor='center', style='OrderTitleStyle.TLabel', padding=40)
    OrderTable = Table_Builder(OrderMainFrame, 5, 5)
    OrderBackButton = Button(OrderMainFrame, activeforeground='#f0ead2', activebackground='#adc178', fg='#f0ead2', bg='#adc178', padx=10, pady=10, text='Back', command=lambda: __main__.Main_Frame(container, OrderMainFrame))
    OrderMainFrameStyle = Style()
    OrderTitleStyle = Style()
    
    OrderMainFrameStyle.configure('OrderMainFrameStyle.TFrame', background='#6c584c')
    OrderTitleStyle.configure('OrderTitleStyle.TLabel', foreground='#dde5b6', background='#a98467', font=('Calibri Light', 50))
    OrderBackButton.configure(font=('Calibri Light', 20))
    
    OrderMainFrame.grid(column=0, row=0, sticky='nsew')
    OrderTitle.grid(column=0, row=0, sticky='new')
    OrderTable.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')
    OrderBackButton.grid(column=0, row=2, padx=10, pady=10, sticky='sw')
    
    OrderMainFrame.columnconfigure(0, weight=1)
    OrderMainFrame.rowconfigure(0, weight=1)
    OrderMainFrame.rowconfigure(1, weight=5)
    OrderMainFrame.rowconfigure(2, weight=1)
    