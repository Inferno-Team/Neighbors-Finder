#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from adjacency import AdjacencyPoint, Point, PathSeeker


class PathsWindow:
    point_size = 100

    def __init__(self, master=None, points=[], v=[1]):
        # build ui
        self.points = points
        self.type = type
        self.v = v

        max_x = max([point.x for point in self.points])
        max_y = max([point.y for point in self.points])
        self.max_x = max_x
        self.max_y = max_y
        width = (max_x + 1) * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.2)
        height = (max_y + 1) * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.2)
        self.adjacency = AdjacencyPoint(points=self.points, v=self.v)
        self.seeker = PathSeeker(points=self.points, vector=self.v)
        self.neighbor_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.neighbor_window.title(f' Shortest Path Seeker')
        self.neighbor_window.configure(height=height, width=width)
        self.neighbor_frame = ttk.Frame(self.neighbor_window)
        self.neighbor_frame.configure(height=height, width=width)
        canvas1 = tk.Canvas(self.neighbor_frame)
        self.canvas = canvas1
        canvas1.configure(height=height, width=width)
        canvas1.grid(column=0, row=0, sticky="nsew")
        self.neighbor_frame.grid(column=0, row=0, sticky="nsew")

        self.points_drawing = []
        self.start_point = None
        self.end_point = None
        canvas1.bind("<Button-1>", self.clicked)
        for (index, point) in enumerate(self.points):
            self.draw_point(point=point)
        # Main widget
        self.mainwindow = self.neighbor_window

    def clicked(self, event):
        x, y = event.x, event.y
        point = self.check_if_point(x, y)
        if point is None:
            for rect in self.points_drawing:
                self.canvas.delete(rect)
            self.start_point = None
            self.end_point = None
            return
        if self.start_point is not None and self.end_point is not None:
            # clear all paths and put selected point as start point
            for rect in self.points_drawing:
                self.canvas.delete(rect)
            self.start_point = None
            self.end_point = None
        if self.start_point is None:
            self.start_point = point
            self.draw_point_with_padding(self.start_point, color='green')
            return
        if self.end_point is None:
            self.end_point = point
            self.draw_point_with_padding(self.end_point, color='blue')
        (path, dist) = self.seeker.dijkstra(self.start_point, self.end_point)
        if dist != -1:
            for (index, point) in enumerate(path):
                if index + 1 < len(path):
                    self.draw_lin_between_points(point, path[index+1])

                if point not in [self.start_point, self.end_point]:
                    self.draw_point_with_padding(point)

    def draw_point_with_padding(self, n: Point, color='red'):
        start_point_x = n.x * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.2)
        end_point_x = start_point_x + \
            (PathsWindow.point_size * 0.8)

        start_point_y = n.y * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.2)
        end_point_y = start_point_y + \
            (PathsWindow.point_size * 0.8)

        rect = self.canvas.create_rectangle(
            start_point_x, start_point_y, end_point_x, end_point_y, outline=color)
        self.points_drawing.append(rect)

    def check_if_point(self, x, y):
        for (index, point) in enumerate(self.points):
            start_point_x = point.x * PathsWindow.point_size + \
                (PathsWindow.point_size * 0.1)
            end_point_x = start_point_x + PathsWindow.point_size

            start_point_y = point.y * PathsWindow.point_size + \
                (PathsWindow.point_size * 0.1)
            end_point_y = start_point_y + PathsWindow.point_size
            if x >= start_point_x and x <= end_point_x and y >= start_point_y and y <= end_point_y:
                return point

    def draw_lin_between_points(self, p1, p2):
        start_point_x = p1.x * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.2)
        end_point_x = start_point_x + \
            (PathsWindow.point_size * 0.8)

        start_point_y = p1.y * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.2)
        end_point_y = start_point_y + \
            (PathsWindow.point_size * 0.8)

        center_point_x = (start_point_x + end_point_x) / 2
        center_point_y = (start_point_y + end_point_y) / 2

        start_point_x = p2.x * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.2)
        end_point_x = start_point_x + \
            (PathsWindow.point_size * 0.8)

        start_point_y = p2.y * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.2)
        end_point_y = start_point_y + \
            (PathsWindow.point_size * 0.8)

        center_x = (start_point_x + end_point_x) / 2
        center_y = (start_point_y + end_point_y) / 2
        line = self.canvas.create_line(
            center_point_x, center_point_y, center_x, center_y, dash=(5, 3),  fill='orange')
        self.points_drawing.append(line)

    def draw_point(self, point: Point):
        start_point_x = point.x * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.1)
        start_point_y = point.y * PathsWindow.point_size + \
            (PathsWindow.point_size * 0.1)
        end_point_x = start_point_x + PathsWindow.point_size
        end_point_y = start_point_y + PathsWindow.point_size
        center_x = (start_point_x + end_point_x) / 2
        center_y = (start_point_y + end_point_y) / 2
        self.canvas.create_rectangle(
            start_point_x, start_point_y, end_point_x, end_point_y, outline='black')
        self.canvas.create_text(center_x, center_y, text=point.value)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = PathsWindow()
    app.run()
