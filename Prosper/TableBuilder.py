from tkinter import Frame, Entry

class Table_Builder(Frame):
    def __init__(self, container, rows, columns):
        Frame.__init__(self, container)

        self.table = {}
        self.rows = rows
        self.columns = columns

        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = Entry(self)
                e.grid(row=row, column=column, stick="nsew")
                self.table[index] = e   
            self.grid_rowconfigure(row, weight=1)

        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
            