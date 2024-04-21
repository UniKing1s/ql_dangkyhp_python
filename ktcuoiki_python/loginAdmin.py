import tkinter as tk
from ktcuoiki_python.models.cruds import loginService
from tkinter import  messagebox
from ktcuoiki_python.views import ql_hocphan
from setuptools.msvc import winreg


# global masv_input
# global pas_input
class login_view():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Đăng nhập quản lý đăng ký học phần")
        self.window.minsize(400,150)
        self.window.maxsize(400,150)
        self.frame= tk.Frame(self.window, width=400, height=150)
        self.login_label_frame = tk.LabelFrame(self.frame, text="Thông tin đăng nhập")
        self.masv = tk.Label(self.login_label_frame, text="Tài khoản")
        self.matkhau = tk.Label(self.login_label_frame, text="Mật khẩu")
        self.masv_input = tk.Entry(self.login_label_frame)
        self.type_show = "*"
        self.pas_input = tk.Entry(self.login_label_frame,show=self.type_show)
        self.load()

    def load(self):
        self.login_label_frame.grid(row=0,column=0)
        self.show_pass_var = tk.BooleanVar(value=False)
        self.show_pass = tk.Checkbutton(self.login_label_frame,variable=self.show_pass_var,text="Hiển thị mật khẩu",command= self.show_pas_click)
        self.show_pass.grid(row=2,column=1)
        self.masv.grid(row=0,column=0)
        self.masv_input.grid(row=0,column=1)
        self.matkhau.grid(row=1,column=0)
        self.pas_input.grid(row=1,column=1)
        self.frame.pack()
        button = tk.Button(self.frame, text="Đăng nhập", command=lambda : self.button_click())
        button.grid(row=1,column=0)
        self.window.mainloop()
    def show_pas_click(self):
        if self.show_pass_var.get():
            self.type_show = "text"
        else:
            self.type_show = "*"
        self.pas_input.config(show=self.type_show)

    def button_click(self):
        print("Button clicked!")
        if len(loginService.checkLogin(self.masv_input.get(),self.pas_input.get())) == 0:
            print("Thông tin sai")
        else:
            self.window.destroy()
            print("Đăng nhập thành công")
            # mainView.createMainView()
login_view()