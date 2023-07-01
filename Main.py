import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

root = tk.Tk()
root.title("Title")

root.overrideredirect(True)

file_path = Path("IMG_20230117_125754_610.jpg")
image = Image.open(file_path)
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()

root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = screen_width//2 - width//2
y = screen_height//2 - height//2
root.geometry(f'+{x}+{y}')

def on_closing():
    return None


def close_program(event):
    if event.keycode == 49:
        print('종료됨')
        root.destroy()

root.bind("<Key>", close_program)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
