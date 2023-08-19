import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path
import requests
from io import BytesIO

root = tk.Tk()
root.title("이미지 보기")

root.overrideredirect(True)

url = 'https://raw.githubusercontent.com/Gaeduck-0908/Python_Adware_Windows_Popup/master/So_Secret_Boy.jpg'
response = requests.get(url)
image = Image.open(BytesIO(response.content))
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
    if event.keycode == 49: #1
        print('종료됨')
        root.destroy()

root.bind("<Key>", close_program) 

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
