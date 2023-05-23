from tkinter import filedialog as fd
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from my_image_processing import ImageProcessingClass


class SelectImageApp:
    def __init__(self, master=None):
        self.first_path = None
        self.second_path = None
        # build ui
        self.root_master = tk.Tk() if master is None else tk.Toplevel(master)
        # self.root_master.state("zoomed")
        self.root_master.title = "Image Processing"
        self.root_master.configure(height=500, width=500)
        self.first_image_canvas = tk.Canvas(self.root_master)
        self.first_image_canvas.configure(height=225, width=225)
        self.first_image_canvas.place(
            anchor="nw", relx=0.003, rely=0.538, x=0, y=0)
        self.second_image_canvas = tk.Canvas(self.root_master)
        self.second_image_canvas.configure(height=225, width=225)
        self.second_image_canvas.place(
            anchor="nw", relx=0.537, rely=0.538, x=0, y=0)
        self.choose_image = tk.Button(self.root_master)
        self.choose_image.configure(
            font="{Times New Roman} 14 {}",
            text='Choose Image',
            width=14,
            command=self.choose_image_clicked)
        self.choose_image.place(anchor="nw", relx=0.38, rely=0.12, x=0, y=0)
        # self.choose_image.bind("<Button>", self.choose_image_clicked, add="")
        self.close = tk.Button(self.root_master)
        self.close.configure(
            font="{Times New Roman} 14 {}",
            text='Close',
            width=14,
            command=self.close_clicked)
        self.close.place(anchor="nw",  relx=0.38, rely=0.43, x=0, y=0)
        # self.close.bind("<Button>", self.close_clicked, add="")
        self.image_processing = tk.Button(self.root_master)
        self.image_processing.configure(
            font="{Times New Roman} 14 {}",
            text='Process Images',
            width=14,
            command=self.process_images,
            state='disabled'
        )
        self.image_processing.place(
            anchor="nw", relx=0.38, rely=0.27, x=0, y=0)

        # Main widget
        self.mainwindow = self.root_master

    def run(self):
        self.mainwindow.mainloop()

    def choose_image_clicked(self):
        path = self.choose_image_function()
        if self.first_path is None:
            self.first_path = path
            self.first_image = self.show_image(self.first_path)
            self.first_image_canvas.create_image(
                0, 0, anchor=tk.NW, image=self.first_image)

        elif self.second_path is None:
            self.second_path = path
            self.second_image = self.show_image(self.second_path)
            self.second_image_canvas.create_image(
                0, 0, anchor=tk.NW, image=self.second_image)
            self.choose_image.configure(state='disabled')
            self.image_processing.configure(state='normal')

    def close_clicked(self, event=None):
        exit()

    def choose_image_function(self):
        filetypes = [('image files', ('.png', '.jpg', '.jpeg', '.tiff'))]
        path = fd.askopenfilename(
            title='Choose Image',
            initialdir='./',
            filetypes=filetypes
        )
        return path

    def show_image(self, image_path, flag=cv2.IMREAD_COLOR):
        image = cv2.imread(image_path, flag)
        image = cv2.resize(image, dsize=(225, 225))
        return ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))

    def process_images(self):
        # open it on new window and clean all images from hear

        self.first_image_canvas.delete(self.first_image)
        self.first_image = None
        self.second_image_canvas.delete(self.second_image)
        self.second_image = None
        self.first = self.first_path
        self.first_path = None
        self.second = self.second_path
        self.second_path = None
        self.choose_image.configure(state='normal')
        self.image_processing.configure(state='disabled')
        ImageProcessingClass(first_image=self.first, second_image=self.second, method='add',
                             read_flag=cv2.IMREAD_GRAYSCALE)


if __name__ == "__main__":
    app = SelectImageApp()
    app.run()
