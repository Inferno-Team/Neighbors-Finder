#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from neighbor_gui import NeighborWindow


class SelectNeighobrsWindow:
    def __init__(self, master=None, points=[]):
        self.points = points
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.master = master
        self.main_window.configure(height=200, width=200)
        frame1 = ttk.Frame(self.main_window)
        frame1.configure(height=200, width=300)
        self.n4 = ttk.Button(frame1)
        self.n4.configure(text='4 neighbors')
        self.n4.grid(column=1, columnspan=2, pady=5, row=0, sticky="ew")
        self.n4.configure(command=self.select4neighbors)
        self.n8 = ttk.Button(frame1)
        self.n8.configure(text='8 neighbors')
        self.n8.grid(column=1, columnspan=2, pady=5, row=1)
        self.n8.configure(command=self.select8neighbors)
        frame1.place(anchor="nw", relx=0.39, rely=0.25, x=0, y=0)

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def select4neighbors(self):
        NeighborWindow(master=self.master, points=self.points, type='4')
        self.mainwindow.destroy()

    def select8neighbors(self):
        NeighborWindow(master=self.master, points=self.points, type='8')
        self.mainwindow.destroy()


if __name__ == "__main__":
    app = SelectNeighobrsWindow()
    app.run()
