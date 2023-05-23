#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from adjacency import AdjacencyPoint, Point


class AdjacencyWindow:
    point_size = 100

    def __init__(self, master=None, points=[], type='4', vector=''):
        # build ui
        self.points = points
        self.type = type
        self.neighbores = []
        if vector != '':
            v = [int(item) for item in vector.split(' ')]
        else:
            v = [1]
        max_x = max([point.x for point in self.points])
        max_y = max([point.y for point in self.points])
        self.max_x = max_x
        self.max_y = max_y
        width = (max_x + 1) * AdjacencyWindow.point_size + \
            (AdjacencyWindow.point_size * 0.2)
        height = (max_y + 1) * AdjacencyWindow.point_size + \
            (AdjacencyWindow.point_size * 0.2)
        self.adjacency = AdjacencyPoint(points=self.points, v=v)
        self.neighbor_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.neighbor_window.title(f'{type} agencency')
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
            neighbors8_not_mixed = []
            if self.type == '8':
                neighbores = self.adjacency.get8adjacency(point.x, point.y)
            elif self.type == '4':
                neighbores = self.adjacency.get4adjacency(point.x, point.y)
            else:
                (neighbores, neighbors8_not_mixed) = self.adjacency.get_mixed_nieghbors(
                    point.x, point.y)
            for (index, n) in enumerate(neighbors8_not_mixed):

                start_point_x = point.x * AdjacencyWindow.point_size + \
                    (AdjacencyWindow.point_size * 0.2)
                end_point_x = start_point_x + \
                    (AdjacencyWindow.point_size * 0.8)

                start_point_y = point.y * AdjacencyWindow.point_size + \
                    (AdjacencyWindow.point_size * 0.2)
                end_point_y = start_point_y + \
                    (AdjacencyWindow.point_size * 0.8)

                center_point_x = (start_point_x + end_point_x) / 2
                center_point_y = (start_point_y + end_point_y) / 2

                start_point_x = n.x * AdjacencyWindow.point_size + \
                    (AdjacencyWindow.point_size * 0.2)
                end_point_x = start_point_x + \
                    (AdjacencyWindow.point_size * 0.8)

                start_point_y = n.y * AdjacencyWindow.point_size + \
                    (AdjacencyWindow.point_size * 0.2)
                end_point_y = start_point_y + \
                    (AdjacencyWindow.point_size * 0.8)

                center_x = (start_point_x + end_point_x) / 2
                center_y = (start_point_y + end_point_y) / 2

                rect = self.canvas.create_rectangle(
                    start_point_x, start_point_y, end_point_x, end_point_y, outline='blue')
                self.neighbores.append(rect)
                dotted_line = self.canvas.create_line(
                    center_point_x, center_point_y, center_x, center_y, dash=(5, 2), fill='green')
                
                self.neighbores.append(dotted_line)
            for (index, n) in enumerate(neighbores):
                start_point_x = n.x * AdjacencyWindow.point_size + \
                    (AdjacencyWindow.point_size * 0.2)
                end_point_x = start_point_x + \
                    (AdjacencyWindow.point_size * 0.8)

                start_point_y = n.y * AdjacencyWindow.point_size + \
                    (AdjacencyWindow.point_size * 0.2)
                end_point_y = start_point_y + \
                    (AdjacencyWindow.point_size * 0.8)

                rect = self.canvas.create_rectangle(
                    start_point_x, start_point_y, end_point_x, end_point_y, outline='red')
                self.neighbores.append(rect)

    def check_if_point(self, x, y):
        for (index, point) in enumerate(self.points):
            start_point_x = point.x * AdjacencyWindow.point_size + \
                (AdjacencyWindow.point_size * 0.1)
            end_point_x = start_point_x + AdjacencyWindow.point_size

            start_point_y = point.y * AdjacencyWindow.point_size + \
                (AdjacencyWindow.point_size * 0.1)
            end_point_y = start_point_y + AdjacencyWindow.point_size
            if x >= start_point_x and x <= end_point_x and y >= start_point_y and y <= end_point_y:
                return point

    def draw_point(self, point: Point):
        start_point_x = point.x * AdjacencyWindow.point_size + \
            (AdjacencyWindow.point_size * 0.1)
        start_point_y = point.y * AdjacencyWindow.point_size + \
            (AdjacencyWindow.point_size * 0.1)
        end_point_x = start_point_x + AdjacencyWindow.point_size
        end_point_y = start_point_y + AdjacencyWindow.point_size
        center_x = (start_point_x + end_point_x) / 2
        center_y = (start_point_y + end_point_y) / 2
        self.canvas.create_rectangle(
            start_point_x, start_point_y, end_point_x, end_point_y, outline='black')
        self.canvas.create_text(center_x, center_y, text=point.value)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = AdjacencyWindow()
    app.run()
