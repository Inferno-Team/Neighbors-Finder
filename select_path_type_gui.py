#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from paths_gui import PathsWindow


class SelectPathApp:
    def __init__(self, master=None, points=[]):
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_window.configure(height=200, width=300)
        self.master = master
        self.points = points
        self.main_frame = ttk.Frame(self.main_window)
        self.main_frame.configure(height=200, width=200)
        self.a4 = ttk.Button(self.main_frame)
        self.a4.configure(text='4 agecency')
        self.a4.grid(column=1, columnspan=2, pady=5, row=1, sticky="ew")
        self.a4.configure(command=self.select4agecency)
        # self.a8 = ttk.Button(self.main_frame)
        # self.a8.configure(text='8 agecency')
        # self.a8.grid(column=1, columnspan=2, pady=5, row=2, sticky="ew")
        # self.a8.configure(command=self.select8agecency)
        # self.am = ttk.Button(self.main_frame)
        # self.am.configure(text='mixed agecency')
        # self.am.grid(column=1, columnspan=2, pady=5, row=3, sticky="ew")
        # self.am.configure(command=self.select_mixed_agecency)
        self.vector = ttk.Entry(self.main_frame)
        self.vector.grid(column=1, columnspan=1, row=0, sticky="ew")
        self.vector_label = ttk.Label(self.main_frame)
        self.vector_label.configure(text='Vector')
        self.vector_label.grid(column=0, row=0)
        self.main_frame.grid(column=0, row=0, sticky="nsew")

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def select4agecency(self):
        vector = self.vector.get()
        v = [1]
        if vector != '':
            v = [int(item) for item in vector.split(' ')]
        PathsWindow(master=self.master, points=self.points, v=v)
        self.mainwindow.destroy()

    # def select8agecency(self):
    #     pass

    # def select_mixed_agecency(self):
    #     pass


if __name__ == "__main__":
    app = SelectPathApp()
    app.run()
