from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image Path
image_paths = [
    r"D:\Mobile Photo Backup\Download\WhatsApp Image 2025-03-30 at 8.57.52 PM.jpeg",
    r"D:\Mobile Photo Backup\Anjali\ChatGPT Image Mar 30, 2025, 02_27_35 PM.png",
    r"D:\Mobile Photo Backup\Anjali\ChatGPT Image Apr 1, 2025, 12_01_05 AM.png",
    r"D:\Mobile Photo Backup\Snapchat\Snapchat-18066367.jpg",
    r"D:\Mobile Photo Backup\Snapchat\Snapchat-599291956.jpg" 
]

# Resize the images to 1080x1080
image_size=(1080,1080)
images=[Image.open(path). resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root,text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()










