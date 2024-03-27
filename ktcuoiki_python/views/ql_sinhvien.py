from ktcuoiki_python.models.cruds import dangkyService,sinhvienService
import tkinter as tk
from tkinter import ttk
class lb_frame():
    def __init__(self, frame):
        self.txt_massv = tk.StringVar()
        self.txt_hosv = tk.StringVar()
        self.txt_tensv= tk.StringVar()
        self.txt_ngaysinh = tk.StringVar()
        self.txt_gioitinh = tk.StringVar()
        self.txt_noisinh = tk.StringVar()
        self.txt_malop = tk.StringVar()
        self.load(frame)
    def load(self,frame):
        infohp_lbframe = tk.LabelFrame(frame, text="Thông tin sinh viên")
        infohp_lbframe.grid(row=0, column=0,padx=10, pady=10)
        # Tạo label
        massv_lb = tk.Label(infohp_lbframe, text="Mã Số Sinh Viên:")
        hosv_lb = tk.Label(infohp_lbframe, text="Họ Đệm:")
        tensv_lb = tk.Label(infohp_lbframe, text="Tên Sinh Viên:")
        ngaysinh_lb = tk.Label(infohp_lbframe, text="Ngày Sinh:")
        gioitinh_lb = tk.Label(infohp_lbframe, text="Giới Tính:")
        noisinh_lb = tk.Label(infohp_lbframe, text="Nơi Sinh:")
        malop_lb = tk.Label(infohp_lbframe, text="Mã Lớp:")

        # Tạo ô nhập
        massv_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_massv)
        hosv_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_hosv)
        tensv_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_tensv)
        ngaysinh_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_ngaysinh)
        gioitinh_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_gioitinh)
        noisinh_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_noisinh)
        malop_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_malop)

        # set vị trí cho khung thông tin
        # các label mỗi dòng cột 0
        massv_lb.grid(row=0, column=0)
        hosv_lb.grid(row=1, column=0)
        tensv_lb.grid(row=2, column=0)
        ngaysinh_lb.grid(row=3, column=0)
        gioitinh_lb.grid(row=4, column=0)
        noisinh_lb.grid(row=5, column=0)
        malop_lb.grid(row=6, column=0)

        # các entry ô nhập liệu mỗi dòng cột 1
        massv_entry.grid(row=0, column=1)
        hosv_entry.grid(row=1, column=1)
        tensv_entry.grid(row=2, column=1)
        ngaysinh_entry.grid(row=3, column=1)
        gioitinh_entry.grid(row=4, column=1)
        noisinh_entry.grid(row=5, column=1)
        malop_entry.grid(row=6, column=1)
    def setInfo(self, massv,hosv, tensv,ngaysinh,gioitinh,noisinh,malop):
        self.txt_massv.set(massv)
        self.txt_hosv.set(hosv)
        self.txt_tensv.set(tensv)
        self.txt_ngaysinh.set(ngaysinh)
        self.txt_gioitinh.set(gioitinh)
        self.txt_noisinh.set(noisinh)
        self.txt_malop.set(malop)
    # return infohp_lbframe
class table():
    def __init__(self, frame, label_frame):
        self.lb_frame = label_frame
        self.table = ttk.Treeview(frame, columns=("1", "2", "3", "4","5","6","7"), show="headings",selectmode="browse")
        self.load_table()
    def load_table(self):
        self.table.heading("1", text="Mã Số Sinh Viên")
        self.table.heading("2", text="Họ Sinh Viên")
        self.table.heading("3", text="Tên Sinh Viên")
        self.table.heading("4", text="Ngày Sinh")
        self.table.heading("5", text="Giới Tính")
        self.table.heading("6", text="Nơi Sinh")
        self.table.heading("7", text="Mã Lớp ")
        self.table.grid(row=0, column=0)
        for i in sinhvienService.getAll():
            self.table.insert(parent='', index=tk.END, values=i.showInfo())
        self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
    def handle_selectItem(self, event):
        selection = self.table.selection()
        for i in selection:
            store = self.table.item(i, "values")
            self.lb_frame.setInfo(store[0],store[1],store[2],store[3],store[4],store[5],store[6])