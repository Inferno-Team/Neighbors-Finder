#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from adjacency import NeighborPoint, Point


class NeighborWindow:

    point_size = 100

    def __init__(self, master=None, points=[], type='8'):
        # build ui
        self.points = points
        self.type = type
        self.neighbores = []
        self.neighbor = NeighborPoint(points=self.points)
        max_x = max([point.x for point in self.points])
        max_y = max([point.y for point in self.points])
        self.max_x = max_x
        self.max_y = max_y
        width = (max_x + 1) * NeighborWindow.point_size + \
            (NeighborWindow.point_size * 0.2)
        height = (max_y + 1) * NeighborWindow.point_size + \
            (NeighborWindow.point_size * 0.2)
        self.neighbor_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.neighbor_window.title(f'{type} neighbors')
        self.neighbor_window.configure(height=height, width=width)
        self.neighbor_frame = ttk.Frame(self.neighbor_window)
        self.neighbor_frame.configure(height=height, width=width)
        canvas1 = tk.Canvas(self.neighbor_frame)
        self.canvas = canvas1
        canvas1.configure(height=height, width=width)
        canvas1.grid(column=0, row=0, sticky="nsew")
        self.neighbor_frame.grid(column=0, row=0, sticky="nsew")

        self.rect = None
        canvas1.bind("<Button-1>", self.clicked)

        for (index, point) in enumerate(self.points):
            self.draw_point(point=point)
        # Main widget
        self.mainwindow = self.neighbor_window

    def clicked(self, event):
        x, y = event.x, event.y
        if self.rect != None:
            self.canvas.delete(self.rect)
        for rect in self.neighbores:
            self.canvas.delete(rect)
        point = self.check_if_point(x, y)
        if point != None:
            print(f"point {point} is clicked")
            if self.type == '8':
                neighbores = self.neighbor.get8neighbors(point)
            else:
                neighbores = self.neighbor.get4neighbors(point)
            for neighbor in (neighbores):
                rect = self.draw_point(neighbor, 'red', True)
                self.neighbores.append(rect)

    def check_if_point(self, x, y):
        print(f'x : {x} , y: {y}')
        for (index, point) in enumerate(self.points):
            start_point_x = point.x * NeighborWindow.point_size + \
                (NeighborWindow.point_size * 0.1)
            end_point_x = start_point_x + NeighborWindow.point_size

            start_point_y = point.y * NeighborWindow.point_size + \
                (NeighborWindow.point_size * 0.1)
            end_point_y = start_point_y + NeighborWindow.point_size
            if x >= start_point_x and x <= end_point_x and y >= start_point_y and y <= end_point_y:
                return point

    def draw_point(self, point: Point, color: str = 'black', with_padding: bool = False):
        if with_padding:
            padding_start = 0.2
            padding_end = 0.8
        else:
            padding_start = 0.1
            padding_end = 1
        start_point_x = point.x * NeighborWindow.point_size + \
            (NeighborWindow.point_size * padding_start)
        start_point_y = point.y * NeighborWindow.point_size + \
            (NeighborWindow.point_size * padding_start)
        end_point_x = start_point_x + (NeighborWindow.point_size * padding_end)
        end_point_y = start_point_y + (NeighborWindow.point_size * padding_end)
        center_x = (start_point_x + end_point_x) / 2
        center_y = (start_point_y + end_point_y) / 2

        rect = self.canvas.create_rectangle(
            start_point_x, start_point_y, end_point_x, end_point_y, outline=color)
        if not with_padding:
            self.canvas.create_text(center_x, center_y, text=point.value)
        return rect

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NeighborWindow()
    app.run()
