from tkinter import ttk, messagebox
import tkinter
import json
import hashlib
from loguru import logger
import os

def login_progress():
    def verify_progress():
        if len(verify_name.get())==0 or len(verify_code.get()) == 0 :
            logger.info(verify_name.get(), verify_code.get())
            messagebox.showwarning('error','invalid input!')
        elif len(verify_name.get()) !=0 or len(verify_code.get()) != 0 :
            if messagebox.askyesno('tips',f'be sure about it?\n your input is: \n {verify_name.get()} \n {verify_code.get()}'):
                try:
                    with open(r'E:\python_projects\craw_movie_trail\default_param\verify_messages.json', 'r',) as f:
                        data = json.load(f)
                        logger.debug(data)
                        if data['account']==verify_name.get() and data['code']==verify_code.get():
                            logger.debug('login_success')
                            root.destroy()
                            return True
                        else:
                            messagebox.showwarning('error','account and code do not match! \n retry again!')

                except Exception as a:
                    logger.info(a)

        else:
            logger.debug('something arise....')

    def quit_verify_progress():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()


    root = tkinter.Tk()
    root.title("登录界面")

    ttk.Label(root,text='account:').grid(row=0, column=0,columnspan=2,sticky=tkinter.NSEW)
    verify_name = ttk.Entry(root, width=40)
    verify_name.grid(row=0, column=3,columnspan=4,sticky=tkinter.NSEW)

    ttk.Label(root,text="code:").grid(row=1, column=0,columnspan=2,sticky=tkinter.NSEW)
    verify_code = ttk.Entry(root, width=40)
    verify_code.grid(row=1, column=3,columnspan=4,sticky=tkinter.NSEW)

    ttk.Button(root,text='登录',command=verify_progress).grid(row=3, column=0,columnspan=2,sticky=tkinter.NSEW)
    ttk.Button(root,text='退出',command=quit_verify_progress).grid(row=3, column=3,columnspan=2,sticky=tkinter.NSEW)

    root.mainloop()

if __name__ == '__main__':
    login_progress()