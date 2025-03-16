import tkinter as tk
from PIL import Image, ImageTk

class FullScreen:
    def __init__(self, image_path='logo.jpg'):
        self.parent = tk.Tk()
        self.parent.title("Splash Screen")
        self.parent.attributes('-fullscreen', True)

        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()

        self.image = Image.open(image_path).convert("RGBA")
        self.resized_image = self.image.resize((self.screen_width, self.screen_height), Image.Resampling.LANCZOS) #resize logo to be fullscreen
        
        # Store reference to prevent garbage collection
        self.photo = ImageTk.PhotoImage(self.resized_image) #open photo inside window
        self.label = tk.Label(self.parent, image=self.photo, bg="black")
        self.label.image = self.photo  # Important: Prevent garbage collection
        self.label.pack(fill=tk.BOTH, expand=True) #pack image in to be fullscreen

    def fade_image(self, alpha=255):
        if alpha >= 0:
            faded = self.resized_image.copy()
            faded.putalpha(alpha)
            new_photo = ImageTk.PhotoImage(faded)  # apply transparency
            self.label.config(image=new_photo)
            self.label.image = new_photo  # prevent garbage collection
            self.parent.after(10, lambda: self.fade_image(alpha - 10))

    def run(self):
        self.parent.after(50, self.fade_image)
        self.parent.after(3000, self.parent.destroy)
        self.parent.mainloop()


