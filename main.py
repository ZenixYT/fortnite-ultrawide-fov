import win32gui
import win32con
import win32api
from time import sleep
import tkinter as tk
from tkinter import ttk
import utils

def find_and_resize_window(new_width: int, new_height: int, new_x: int, new_y: int):
    hwnd = win32gui.FindWindow(None, "Fortnite  ")
    if hwnd == 0:
        print("Could not find")

window = win32gui.FindWindow(None, "Fortnite  ")
if window == 0:
    print("Could not find Fortnite window. Fortnite must be open before you can use this tool!")
    sleep(2)
    exit()

# Second, get the width and height of the monitor. Use CTYPES

monitor_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
monitor_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# Third, let's set up a tkinter window for the fov that has a slider and a number.

root = tk.Tk()
root.title("FOV Changer")
root.resizable(False, False)

frame = ttk.Frame(root, padding = "10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

fov_slider_label = ttk.Label(frame, text="FOV: 80")
fov_slider_label.grid(row=0, column=1, padx=10, pady=10)

def update_label(value):
    vF = float(value)
    fov_slider_label.config(text=f"FOV: {round(vF)}")

fov_slider = ttk.Scale(frame, from_ = 80, to=135, orient = tk.HORIZONTAL, command = update_label)
fov_slider.grid(row = 0, column = 0, padx = 10, pady = 10)

fov_slider.set(80)

def change_fov():
    valueFlt = round(float(fov_slider.get()))
    
    h = int(utils.calculate_fov(valueFlt))
    win32gui.MoveWindow(window, 0, int((monitor_height - h) / 2), monitor_width, h, True)

fov_apply_button = ttk.Button(master = frame, text = "Apply", command = change_fov)
fov_apply_button.grid(row = 1, column = 0, padx = 10, pady = 10)

root.mainloop()