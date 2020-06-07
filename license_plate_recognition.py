from PIL import Image, ImageTk  # 导入图像处理函数库
import tkinter as tk  # 导入GUI界面函数库
from tkinter import messagebox, filedialog
import cv2
import numpy as np

root = tk.Tk()
root.title("主窗口")
root.geometry("1000x600+250+50")
global img_png  # 定义全局变量 图像的
global Img


def import_img():
    global img_png
    global Img
    OpenFile = tk.Tk()  # 创建新窗口
    OpenFile.withdraw()
    file_path = filedialog.askopenfilename()
    Img = Image.open(file_path)
    Img = Img.resize((680, 500))
    img_png = ImageTk.PhotoImage(Img)
    label_Img = tk.Label(root, image=img_png)
    label_Img.place(x=10, y=50)
    # messagebox.showinfo("窗口", "导入图片成功！")


def license_plate_recognition():
    global img_png
    global Img
    gray = cv2.cvtColor(np.asarray(Img),cv2.COLOR_BGR2GRAY)
    


# 区域提示框
E1 = tk.Label(root, text="——————————————————————— 图片显示区域")
E1.place(x=10, y=15)
E2 = tk.Label(root, text='———————————————————————')
E2.place(x=387, y=15)
E3 = tk.Label(root, text="——————车牌显示区域——————")
E3.place(x=700, y=15)

# 导入图片按钮
button_import_img = tk.Button(root, text="导入图片", width=30, height=2, command=import_img)
button_import_img.place(x=700, y=430)

# 车牌识别按钮
button_import_img = tk.Button(root, text="车牌识别", width=30, height=2, command=license_plate_recognition)
button_import_img.place(x=700, y=505)

# 车牌识别按钮
root.mainloop()
