import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk

from tkinter import Label
import detect as dt
from tkinter import messagebox
import argparse
import os
import shutil
import cv2
import sys

# 解析当前文件执行路径
local_directory = os.path.dirname(os.path.dirname(os.path.realpath(sys.executable)))


# 目标输入文件路径
target_directory = '\\gui\\_internal\\data\\images\\'  # 将此路径替换为目标目录的实际路径
target_filename = 'input_image.png'  # 保存的文件名

# 选择并显示图片
def choosepic():
    path_ = tkinter.filedialog.askopenfilename()
    path.set(path_)
    print(path)
    img_open = Image.open(entry.get())
    img = ImageTk.PhotoImage(img_open.resize((300, 300)))
    lableShowImage.config(image=img)
    lableShowImage.image = img

    # 选择并显示图片
def classfypic(path):
    path_ = path.get()
    # 使用 shutil 模块的 copy2 函数将图片文件从源目录复制到目标目录
    shutil.copy2(path_, local_directory + target_directory + target_filename)

    # define the results folder
    PT_IMAGE_DIR = "\\gui\\_internal\\runs\\results\\"
    RT_IMAGE_DIR = local_directory + PT_IMAGE_DIR

    # Save the image to a file in the images directory
    image_filename = os.path.join(RT_IMAGE_DIR, 'output_image.png')

    # Check if the image file exists and delete if it does
    if os.path.exists(image_filename):
        os.remove(image_filename)

    opt = dt.parse_opt()
    im0,num = dt.perform_inference(**vars(opt))

    im0 = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
    # Create an Image object from the pixel data
    image = Image.fromarray(im0)
    # Save the image to a file in PNG format
    image.save(image_filename)


    image = Image.open(image_filename) # 图片输出结果
    photo = ImageTk.PhotoImage(image.resize((300, 300)))
    showClaImage.config(image=photo)
    showClaImage.image = photo  # 保持对图像的引用以防止垃圾回收


if __name__ == '__main__':
    # 生成tk界面 app即主窗口
    app = tk.Tk()
    # 修改窗口titile
    app.title("显示图片")
    # 设置主窗口的大小和位置
    app.geometry("800x900")

    path = tk.StringVar()
    entry = tk.Entry(app, state='readonly', text=path, width=50)
    entry.pack()
    # 选择图片的按钮
    buttonSelImage = tk.Button(app, text='选择图片', command=choosepic)
    buttonSelImage.pack()

    # 创建"原始图片"和"处理后图片"的标签
    name1 = Label(app, text="原始图片")
    name1.place(relx=0.3, rely=0.2)

    name2 = Label(app, text="处理后图片")
    name2.place(relx=0.3, rely=0.6)

    # 使用Label显示图片
    lableShowImage = tk.Label(app)
    lableShowImage.place(relx=0.4, rely=0.1)

    # 处理图片的按钮
    btnClaImage = tk.Button(app, text='识别图片', command=lambda: classfypic(path))
    btnClaImage.place(relx=0.3, rely=0.4)

    # 使用Label显示识别后的图片
    showClaImage = tk.Label(app)
    showClaImage.place(relx=0.4, rely=0.5)

    app.mainloop()

