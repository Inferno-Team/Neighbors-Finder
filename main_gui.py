

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from select_neighbors import SelectNeighobrsWindow
from select_agecencies import SelectAdjacencyWindow
from select_path_type_gui import SelectPathApp
from adjacency import Point


class MainApplication:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk()
        self.main_window.configure(background="#ffffff", height=360, width=480)
        self.main_window.title('main application window')
        self.main_frame = ttk.Frame(self.main_window)
        self.main_frame.configure(height=360, width=480)
        self.main_frame.grid(column=0, row=0, sticky="nsew")

        self.config_label()
        self.config_choose_file_button()
        self.config_neighbor_button()
        self.config_agencecies_button()
        self.config_close_button()

        # Main widget
        self.mainwindow = self.main_window

    def config_label(self):
        self.label2 = ttk.Label(self.main_frame)
        self.label2.configure(
            font="{Arial Baltic} 16",
            text='Hello To Neighbors Finder')
        self.label2.place(relx=0.29, rely=0.1)

    def config_choose_file_button(self):
        self.choose_file = ttk.Button(self.main_frame)
        self.choose_file.configure(text='Choose File', width=20)
        self.choose_file.place(relx=0.40, rely=0.30)
        self.choose_file.configure(command=self.choose_file_on_click)

    def config_neighbor_button(self):
        self.neighbor_button = ttk.Button(self.main_frame)
        self.neighbor_button.configure(
            state="disabled", text='Neighbor', width=20)
        self.neighbor_button.place(relx=0.40, rely=0.45)
        self.neighbor_button.configure(command=self.neighbor_button_clicked)

    def config_agencecies_button(self):
        self.agencecies_button = ttk.Button(self.main_frame)
        self.agencecies_button.configure(
            state="disabled", text='Agencecies', width=20)
        self.agencecies_button.place(relx=0.4, rely=0.6)
        self.agencecies_button.configure(
            command=self.agencecies_button_clicked)

    def config_close_button(self):
        self.close_button = ttk.Button(self.main_frame)
        self.close_button.configure(state="normal", text='Close', width=20)
        self.close_button.place(relx=0.4, rely=0.75)
        self.close_button.configure(command=self.close_on_click)

    # def config_path_selector_button(self):
    #     self.paths = ttk.Button(self.main_frame)
    #     self.paths.configure(state="disabled", text='Paths', width=20)
    #     self.paths.place(anchor="nw", relx=0.4, rely=0.75, x=0, y=0)
    #     # self.close_button.place(anchor="nw", relx=0.4, rely=0.90, x=0, y=0)
    #     self.paths.configure(command=self.on_paths_clicked)

    def run(self):
        self.mainwindow.mainloop()

    def neighbor_button_clicked(self):
        lines = read_from_file(self.filename)
        points = convert_lines2points(lines=lines)
        SelectNeighobrsWindow(master=self.main_window, points=points)

    def agencecies_button_clicked(self):
        lines = read_from_file(self.filename)
        points = convert_lines2points(lines=lines)
        SelectAdjacencyWindow(master=self.main_window, points=points)

    def choose_file_on_click(self):
        filetypes = (('text files', '*.txt'),)
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='./',
            filetypes=filetypes
        )
        if self.filename != '':
            self.agencecies_button.configure(state='normal')
            self.neighbor_button.configure(state='normal')
            # self.paths.configure(state='normal')

    def close_on_click(self):
        exit()

    def on_paths_clicked(self):
        lines = read_from_file(self.filename)
        points = convert_lines2points(lines=lines)
        SelectPathApp(master=self.main_window, points=points)


def read_from_file(file_name='matrix.txt'):
    f = open(file_name, "r")
    return f.read()


def convert_lines2points(lines="", separator=" ", line_separator="\n"):
    lines_numbers = lines.split(line_separator)
    numbers = []
    for (x, line) in enumerate(lines_numbers):
        _numbers = line.split(separator)
        for (y, number) in enumerate(_numbers):
            point = Point(y, x, int(number))
            numbers.append(point)
    return numbers


if __name__ == "__main__":
    app = MainApplication()
    app.run()
