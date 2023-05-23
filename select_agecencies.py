#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from adjacency_gui import AdjacencyWindow


class SelectAdjacencyWindow:
    def __init__(self, master=None, points=[]):
        # build ui
        self.points = points
        self.master = master
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_window.configure(height=200, width=300)
        self.main_frame = ttk.Frame(self.main_window)
        self.main_frame.configure(height=200, width=300)
        self.vector = ttk.Entry(self.main_frame)
        self.vector.grid(column=1,  columnspan=2, row=0, sticky="ew")
        self.vector_label = ttk.Label(self.main_frame)
        self.vector_label.configure(text='Vector')
        self.vector_label.grid(column=0, row=0)

        self.a4 = ttk.Button(self.main_frame)
        self.a4.configure(text='4 adjacency')
        self.a4.grid(column=1, columnspan=2, pady=5, row=1, sticky="ew")
        self.a4.configure(command=self.select4adjacency)
        self.a8 = ttk.Button(self.main_frame)
        self.a8.configure(text='8 adjacency')
        self.a8.grid(column=1, columnspan=2, pady=5, row=2, sticky="ew")
        self.a8.configure(command=self.select8adjacency)
        self.am = ttk.Button(self.main_frame)
        self.am.configure(text='mixed adjacency')
        self.am.grid(column=1, columnspan=2, pady=5, row=3, sticky="ew")
        self.am.configure(command=self.select_mixed_adjacency)
        self.main_frame.place(anchor="nw", relx=0.39, rely=0.25, x=0, y=0)

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def select4adjacency(self):
        vector = self.vector.get()
        AdjacencyWindow(master=self.master, points=self.points,
                        type='4', vector=vector)
        self.mainwindow.destroy()

    def select8adjacency(self):
        vector = self.vector.get()
        AdjacencyWindow(master=self.master, points=self.points,
                        type='8', vector=vector)
        self.mainwindow.destroy()

    def select_mixed_adjacency(self):
        vector = self.vector.get()
        AdjacencyWindow(master=self.master, points=self.points,
                        type='m', vector=vector)
        self.mainwindow.destroy()


if __name__ == "__main__":
    app = SelectAdjacencyWindow()
    app.run()
