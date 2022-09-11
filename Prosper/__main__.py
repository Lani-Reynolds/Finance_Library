# This is run when you call it as a "program"
from CleanUp import PyCacheCleanUp

from tkinter import Tk, Button, Menubutton, Menu, IntVar
from tkinter.ttk import Frame, Label, Style

from LogOrder import Log_Order
from LogSale import Log_Sale


def Application():
    Root = Tk()
    
    Root.title('Prosper')
    Root.geometry('1000x800')

    Root.grid_columnconfigure(0, weight=1)
    Root.grid_rowconfigure(0, weight=1)
    
    MenuBar = Menu(Root)
    
    FileMenu = Menu(MenuBar, tearoff=0, bg='#333d29')
    MenuBar.add_cascade(label="File", menu=FileMenu)
    FileMenu.add_command(label="New")
    FileMenu.add_command(label="Open")
    FileMenu.add_command(label="Save")
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=Root.quit)

    HelpMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    HelpMenu.add_command(label="Help Index")
    HelpMenu.add_command(label="About...")

    Root.config(menu=MenuBar)

    return Root


def Main_Frame(Root, past_frame):
    del past_frame
    MainFrame = Frame(Root, style='MainMenu.TFrame')
    Title = Label(MainFrame, text='Pick a menu', anchor='center', style='Title.TLabel', padding=40)
    OrderRecorderButton = Button(MainFrame, activeforeground='#f0ead2', activebackground='#adc178', fg='#dde5b6', bg='#adc178', padx=10, pady=10, text='Order Log', command=lambda: Log_Order(Root, MainFrame))
    SaleRecorderButton = Button(MainFrame, activeforeground='#f0ead2', activebackground='#adc178', fg='#dde5b6', bg='#adc178', padx=10, pady=10, text='Sale Log', command=lambda: Log_Sale(Root, MainFrame))
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
    Main_Frame(Window, past_frame=None)
    Window.mainloop()
    PyCacheCleanUp()
