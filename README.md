# 📷 Image Viewer Application (Tkinter GUI)

This is a simple **Image Viewer** application built using **Python's Tkinter GUI framework** and the **Pillow** library. It allows users to load images from a folder and navigate through them using Previous and Next buttons.

---

## 🚀 Features

* Load images (`.jpg`, `.png`, `.jpeg`, `.bmp`) from any local folder
* Display images in a fixed-size canvas (`600x400`)
* Navigate between images using **Previous** and **Next** buttons
* Displays current image index
* Exit the application with a single click

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – for GUI components
* **Pillow (PIL)** – for image handling and rendering

---

## 📦 Installations 
1. Install dependencies:

```bash
pip install Pillow
```

---

## ▶️ How to Run

```bash
python image_viewer.py
```

A GUI window will open. Use the **"Load Folder"** button to select a folder containing images.

---

## ⚠️ Known Issues

* Incorrect constructor name: Replace `def _init_` with `def __init__`
* Replace `_name_` with `__name__` and `_main_` with `__main__` in the `if` condition
* Fix syntax typo: `tk.NORMALif` → `tk.NORMAL if`

---


