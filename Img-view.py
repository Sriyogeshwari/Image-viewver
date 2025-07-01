import os

import tkinter as tk  

from tkinter import filedialog

from PIL import Image, ImageTk

class ImageViewer:

    def _init_(self, root):

        self.root = root

        self.root.title("Image Viewer")

        self.image_list = []

        self.image_index = 0
        self.label = tk.Label(self.root, text="No Image Selected", font=("Arial", 14))

        self.label.pack()

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="gray")

        self.canvas.pack()

        self.prev_button = tk.Button(self.root, text="Previous", command=self.show_previous, state=tk.DISABLED)

        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.show_next, state=tk.DISABLED)

        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.load_button = tk.Button(self.root, text="Load Folder", command=self.load_images)

        self.load_button.pack(side=tk.BOTTOM, pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=root.quit)

        self.exit_button.pack(side=tk.BOTTOM, pady=10)

  def load_images(self):

        folder_path = filedialog.askdirectory()

        if folder_path:

            self.image_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

            if self.image_list:

                self.image_index = 0

                self.display_image()

                self.update_buttons()

            else:

                self.label.config(text="No images found in the folder")

   def display_image(self):

        if self.image_list:

            image_path = self.image_list[self.image_index]

            img = Image.open(image_path)

            img.thumbnail((600, 400))

            self.tk_img = ImageTk.PhotoImage(img)

            self.canvas.config(width=self.tk_img.width(), height=self.tk_img.height())

            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)

            self.label.config(text=f"Image {self.image_index + 1} of {len(self.image_list)}")

     def show_next(self):

        if self.image_index < len(self.image_list) - 1:

            self.image_index += 1

            self.display_image()

            self.update_buttons()

       def show_previous(self):

        if self.image_index > 0:

            self.image_index -= 1

            self.display_image()

            self.update_buttons()


    def update_buttons(self):

        self.prev_button.config(state=tk.NORMALif self.image_index > 0 else tk.DISABLED)

        self.next_button.config(state=tk.NORMAL if self.image_index < len(self.image_list) - 1 else tk.DISABLED)


if _name_ == "_main_":

    root = tk.Tk()

    app = ImageViewer(root)

    root.mainloop()


