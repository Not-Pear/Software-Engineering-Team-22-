import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

parent = tk.Tk()
parent.title("Splash Screen")

screen_width = parent.winfo_screenwidth()
screen_height = parent.winfo_screenheight()
# Set initial window size to fullscreen. If this is not here the window will gradually grow
parent.attributes('-fullscreen', True)

#getting window measurements
screen_width = parent.winfo_screenwidth()
screen_height = parent.winfo_screenheight()

# Load and make copy of image to fade to black
image = Image.open('logo.jpg').convert("RGBA")
image_copy = image.copy()

#set current opacity
current_alpha = 255


resized_image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS) #resize logo to be fullscreen

photo = ImageTk.PhotoImage(resized_image) #open photo inside window
label = tk.Label(parent, image = photo, bg="black") #setting window background to black which screen will fade to
label.pack(fill=BOTH, expand=True) #pack image in to be fullscreen


def fade_image(alpha=255):
    if alpha >= 0:
        faded = resized_image.copy()
        #faded = faded.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        faded.putalpha(alpha)  # apply transparency
        new_photo = ImageTk.PhotoImage(faded)
        label.config(image=new_photo)
        label.image = new_photo  # prevent garbage collection
        parent.after(50, lambda: fade_image(alpha - 10))  # reduce alpha gradually via recursion

def screenRun():
    parent.after(1000, fade_image) #fade image to black
    parent.after(5000, lambda: parent.destroy()) #cloe window after 10 seconds
    # Create the main window
    # Start the Tkinter event loop
    parent.mainloop()

