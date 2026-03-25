import tkinter
from tkinter import ttk,messagebox
import time
import sys

def progress_show(progress_time):


    def stop():
        progress.stop()
        if messagebox.askyesno("tips", "确认终止?"):
            root.destroy()

    root = tkinter.Tk()
    root.title("请等待。。。")

    progress = ttk.Progressbar(root, orient=tkinter.HORIZONTAL,mode="indeterminate",length=400)
    progress.pack()

    ttk.Button(root,text='终止',command=stop).pack()

    progress.start()

    # root.destroy()
    root.mainloop()



if __name__ == '__main__':
    progress_show(20)