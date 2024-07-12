import math
import win32api, win32con

CONST_V_FOV: float = 50.5340158467

def calculate_fov(fov: float) -> int:
    r = (math.tan(math.radians(fov / 2)) / math.tan(math.radians(CONST_V_FOV / 2)))
    print(r)
    monitor_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)

    h = round(monitor_width / r)
    return h