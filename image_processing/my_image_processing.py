import cv2
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ImageProcessingClass:

    def __init__(self, first_image, second_image, method='add',
                 flag=cv2.COLOR_BGR2RGB, read_flag=cv2.IMREAD_ANYCOLOR):
        root = tk.Tk()
        f = Figure()

        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        canvas._tkcanvas.pack(side="top", fill="both", expand=1)
        root.state("zoomed")

        # Load images using OpenCV
        # img1 = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)
        # img2 = cv2.imread('mailgun.png', cv2.IMREAD_GRALE)
        img1 = cv2.imread(first_image)
        img2 = cv2.imread(second_image)

        # width x height
        # resize both images to max width and max height
        # first get width and height
        height1, width1, _ = img1.shape
        print(f'image 1 : {height1 , width1}')
        height2, width2, _ = img2.shape
        print(f'image 2 : {height2 , width2}')

        # second find max (width & height)
        hmax = max(height1, height2)
        wmax = max(width1, width2)
        print(f'max : {hmax , wmax}')
        # resize both images to this width & height
        final_img1 = cv2.resize(
            img1, (wmax, hmax), interpolation=cv2.INTER_CUBIC)
        final_img2 = cv2.resize(img2,  (wmax, hmax),
                                interpolation=cv2.INTER_CUBIC)

        # Create a new image by adding the processed images together
        if method == 'sub':
            result_img = cv2.subtract(final_img1, final_img2)
        else:
            result_img = cv2.add(final_img2, final_img1)

        a = f.add_subplot(131)
        a.imshow(Image.fromarray(cv2.cvtColor(final_img1, flag)))

        b = f.add_subplot(132)
        b.imshow(Image.fromarray(cv2.cvtColor(final_img2, flag)))

        c = f.add_subplot(133)
        c.imshow(Image.fromarray(cv2.cvtColor(result_img, flag)))

        root.mainloop()
