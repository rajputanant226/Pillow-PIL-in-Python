# pillow image processing main use hoti haii. 
# PIL discontinued in 2011.

import tkinter as tk
from PIL import Image,ImageTk

''' Tk is a class inside the tkinter module.
 tk.Tk()  creates the main application window.'''

'''
Converts a PIL image into a format tkinter can display.
Tkinter cannot show PIL images directly — they must be wrapped 
using ImageTk.PhotoImage.
'''

def main():
    root = tk.Tk() 
    root.geometry("600x600")
    image_path=r"D:\100 days\38th\original.jpg"
    pil_image=Image.open(image_path)
    pil_image=pil_image.resize((400,400))
    tk_image=ImageTk.PhotoImage(pil_image)
    l1=tk.Label(root,image=tk_image)
    l1.pack()
    root.mainloop()


if __name__=='__main__':
    main()