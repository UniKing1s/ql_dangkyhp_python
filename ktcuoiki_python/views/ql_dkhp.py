from ktcuoiki_python.models.cruds import dangkyService
import tkinter as tk
from tkinter import ttk
class lb_frame():
    def __init__(self, frame):
        self.txt_masv = tk.StringVar()
        self.txt_mahp = tk.StringVar()
        self.txt_ngaydangky = tk.StringVar()
        self.txt_ngaydongphi = tk.StringVar()
        self.txt_dathanhtoan = tk.StringVar()
        self.load(frame)
    def load(self,frame):
        infohp_lbframe = tk.LabelFrame(frame, text="Thông tin đăng ký học phần")
        infohp_lbframe.grid(row=0, column=0,padx=10, pady=10)
        # Tạo label
        masv_lb = tk.Label(infohp_lbframe, text="Mã sinh viên:")
        mahp_lb = tk.Label(infohp_lbframe, text="Mã học phần:")
        ngaydangky_lb = tk.Label(infohp_lbframe, text="Ngày đăng ký:")
        ngaydongphi_lb = tk.Label(infohp_lbframe, text="Ngày đóng phí: ")
        dathanhtoan_lb = tk.Label(infohp_lbframe, text="Thanh toán: ")

        # Tạo ô nhập
        masv_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_masv)
        mahp_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_mahp)
        # self.txt_ngaydangky.set('alvsdvsdv')
        ngaydangky_lb_show = tk.Label(infohp_lbframe, textvariable=self.txt_ngaydangky)
        ngaydongphi_lb_show = tk.Label(infohp_lbframe, textvariable=self.txt_ngaydongphi)
        dathanhtoan_lb_show = tk.Entry(infohp_lbframe, textvariable=self.txt_dathanhtoan)

        # set vị trí cho khung thông tin

        # các label mỗi dòng cột 0
        masv_lb.grid(row=0, column=0)
        mahp_lb.grid(row=1, column=0)
        ngaydangky_lb.grid(row=2, column=0)
        ngaydongphi_lb.grid(row=3, column=0)
        dathanhtoan_lb.grid(row=4, column=0)


        # các entry ô nhập liệu mỗi dòng cột 1
        masv_entry.grid(row=0, column=1)
        mahp_entry.grid(row=1, column=1)
        ngaydangky_lb_show.grid(row=2, column=1)
        ngaydongphi_lb_show.grid(row=3, column=1)
        dathanhtoan_lb_show.grid(row=4, column=1)

    def setInfo(self, masv, mahp, ngaydangky, ngaydongphi, dathanhtoan):
        self.txt_masv.set(masv)
        self.txt_mahp.set(mahp)
        self.txt_ngaydangky.set(ngaydangky)
        self.txt_ngaydongphi.set(ngaydongphi)
        self.txt_dathanhtoan.set(dathanhtoan)
    # return infohp_lbframe
class table():
    def __init__(self, frame, label_frame):
        self.lb_frame = label_frame
        self.table = ttk.Treeview(frame, columns=("1", "2", "3", "4", "5"), show="headings", selectmode="browse")
        self.load_table()
    def load_table(self):
        self.table.heading("1", text="Mã sinh viên")
        self.table.heading("2", text="Mã học phần")
        self.table.heading("3", text="Ngày đăng ký")
        self.table.heading("4", text="Ngày đóng phí")
        self.table.heading("5", text="Thanh toán")
        self.table.grid(row=0, column=0)
        for i in dangkyService.getAll():
            self.table.insert(parent='', index=tk.END, values=i.showInfo())
        self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
    def handle_selectItem(self, event):
        selection = self.table.selection()
        for i in selection:
            store = self.table.item(i, "values")
            self.lb_frame.setInfo(store[0],store[1],store[2],store[3],store[4])