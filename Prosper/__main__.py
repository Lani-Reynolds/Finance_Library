# This is run when you call it as a "program"
from CleanUp import PyCacheCleanUp

from tkinter import Tk, Button
from tkinter.ttk import Frame, Label, Style

from OrderRecorder import Order_Recorder
from SaleRecorder import Sale_Recorder


def Application():
    Root = Tk()
    
    Root.title('Prosper')
    Root.geometry('1000x800')

    Root.grid_columnconfigure(0, weight=1)
    Root.grid_rowconfigure(0, weight=1)

    return Root


def Main_Frame(Root):
    MainFrame = Frame(Root, style='MainMenu.TFrame')
    Title = Label(MainFrame, text='Pick a menu', anchor='center', style='Title.TLabel', padding=40)
    OrderRecorderButton = Button(MainFrame, activeforeground='#f0ead2', activebackground='#adc178', fg='#dde5b6', bg='#adc178', padx=10, pady=10, text='Record an order', command=lambda: Order_Recorder(Root))
    SaleRecorderButton = Button(MainFrame, activeforeground='#f0ead2', activebackground='#adc178', fg='#dde5b6', bg='#adc178', padx=10, pady=10, text='Record a sale', command=lambda: Sale_Recorder(Root))
    MainFrameStyle = Style()
    TitleStyle = Style()

    MainFrameStyle.configure('MainMenu.TFrame', background='#6c584c')
    TitleStyle.configure('Title.TLabel', foreground='#dde5b6', background='#a98467', font=('Calibri Light', 50))
    OrderRecorderButton.configure(font=('Calibri Light', 20))
    SaleRecorderButton.configure(font=('Calibri Light', 20))

    MainFrame.grid(column=0, row=0, sticky='nsew')
    Title.grid(column=0, row=0, sticky='ew')
    OrderRecorderButton.grid(column=0, row=1)
    SaleRecorderButton.grid(column=0, row=2, sticky='n')
    
    MainFrame.grid_columnconfigure(0, weight=1)
    MainFrame.grid_rowconfigure(1, weight=1)
    MainFrame.grid_rowconfigure(2, weight=3)


if __name__ == "__main__":
    Window = Application()
    Main_Frame(Window)
    Window.mainloop()
    PyCacheCleanUp()
