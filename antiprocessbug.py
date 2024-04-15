import psutil
import pystray
import keyboard
import subprocess  # Додати цей рядок
import os
from PIL import Image


def kill_unresponsive_processes():
    try:
        if subprocess.call(["taskkill", "/F", "/FI", "STATUS eq NOT RESPONDING"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
            print("Успішно закрито не відповідаючі процеси.")
        else:
            print("Помилка під час спроби закрити не відповідаючі процеси.")
    except Exception as e:
        print("Помилка:", e)

def on_activate():
    kill_unresponsive_processes()

# Встановлення гарячої клавіші
keyboard.add_hotkey("ctrl+alt+f1", on_activate)
def on_exit():
    subprocess.call(["taskkill", "/F", "/PID", str(os.getpid())])
# Створення іконки в треї
def create_tray_icon():
    icon_path = os.path.join(os.path.dirname(__file__), "icon.png")  # Вказуємо шлях до файлу з іконкою
    icon = Image.open(icon_path)

    # icon = Image.open("icon.png")  # Замініть "icon.png" на шлях до вашого зображення іконки
    menu = (pystray.MenuItem("Закрити не відповідаючі процеси", kill_unresponsive_processes),pystray.MenuItem("Закрити",on_exit ))
    tray_icon = pystray.Icon("name", icon, "AntiProcessBug", menu)
    tray_icon.run()

# Запуск програми
create_tray_icon()
