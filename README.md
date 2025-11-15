# Working with Images in Tkinter using Pillow (PIL)
📝 Overview

This project demonstrates how to use the Pillow (PIL) library in Python to load, resize, and display images inside a Tkinter GUI application.
You will learn how to convert PIL images into Tkinter-compatible formats and render them inside a window.

# What I Learn

✔ What is Pillow (PIL)?
✔ How to install Pillow in Python
✔ How to load an image using Image.open()
✔ How to convert a PIL image into a Tkinter-compatible PhotoImage
✔ How to display the image inside Label/Canvas
✔ How to resize an image (maintaining high quality)
✔ Complete step-by-step working code

# What is Pillow (PIL)?

Pillow is a powerful image-processing library in Python.
It is the modern version (fork) of the original Python Imaging Library (PIL).

You can use Pillow to:

Open images

Resize images

Convert formats

Apply filters and effects

Integrate images into Tkinter GUIs

# Converting PIL Image to Tkinter-Compatible Format

Tkinter cannot display images directly.
You must convert the PIL image to a PhotoImage object:

from PIL import ImageTk

tk_img = ImageTk.PhotoImage(img)

# Displaying Image in Tkinter
import tkinter as tk

label = tk.Label(root, image=tk_img)
label.pack()

# Resizing Image in Pillow
Method 1: Resize (Exact Size)
resized = img.resize((300, 300))

Method 2: Thumbnail (Maintain Aspect Ratio)
img.thumbnail((400, 400))


# Possible Future Enhancements

✨ Add image rotation
✨ Implement brightness/contrast sliders
✨ Add filters (grayscale, blur, sharpen)
✨ Create a mini photo editor
✨ Build a slideshow viewer
