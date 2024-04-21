from ktcuoiki_python.models.cruds import dangkyService
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ktcuoiki_python.models.objects.dkhp import dkhp
class lb_frame():
    def __init__(self, frame, btn_them, btn_sua,btn_xoa):
        self.table = None
        self.txt_masv = tk.StringVar()
        self.txt_mahp = tk.StringVar()
        self.txt_ngaydangky = tk.StringVar()
        self.txt_ngaydongphi = tk.StringVar()
        self.dathanhtoan_boolean = tk.IntVar()
        self.btn_them = btn_them
        self.btn_sua = btn_sua
        self.btn_xoa = btn_xoa
        self.load(frame)
    def load(self,frame):
        infohp_lbframe = tk.LabelFrame(frame, text="Thông tin đăng ký học phần")
        # infohp_lbframe.grid(row=0, column=0,padx=10, pady=10)
        infohp_lbframe.pack(fill='both',expand=True)
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
        dathanhtoan_lb_show = tk.Checkbutton(infohp_lbframe, text = 'Đã thanh toán', variable = self.dathanhtoan_boolean)
        if self.dathanhtoan_boolean == 1:
            dathanhtoan_lb_show.select()
        else:
            dathanhtoan_lb_show.deselect()
        # dathanhtoan_lb_show = tk.Entry(infohp_lbframe, textvariable=self.txt_dathanhtoan)
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
        ###setting for button them sua xoa command
        self.btn_them.config(command=lambda: self.insert_dkhp())
        self.btn_sua.config(command=lambda: self.update_dkhp())
        self.btn_xoa.config(command=lambda: self.delete_dkhp())
    def subscribe_table(self, table):
        self.table = table;
    def insert_dkhp(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có chắc đăng ký học phần cho sinh viên này?")
        if check == "yes":
            try:
                hpdk = dkhp(self.txt_masv.get(),self.txt_mahp.get(),self.txt_ngaydangky.get(),self.txt_ngaydongphi.get(),self.dathanhtoan_boolean.get())
                dangkyService.insert(hpdk.masv,hpdk.mahp)
                box = messagebox.showinfo("Thông báo", "Đăng ký học phần thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Đăng ký học phần thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")
        self.table.load_data_table()
    def update_dkhp(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có chắc sửa thông tin đăng ký học phần cho sinh viên này?")
        if check == "yes":
            try:
                hpdk = dkhp(self.txt_masv.get(),self.txt_mahp.get(),self.txt_ngaydangky.get(),self.txt_ngaydongphi.get(),self.dathanhtoan_boolean.get())
                dangkyService.update(hpdk)
                box = messagebox.showinfo("Thông báo", "Sửa thông tin đăng ký học phần thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Sửa thông tin đăng ký học phần thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")

    def delete_dkhp(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có chắc xóa thông tin đăng ký học phần cho sinh viên này?")
        if check == "yes":
            try:
                hpdk = dkhp(self.txt_masv.get(),self.txt_mahp.get(),self.txt_ngaydangky.get(),self.txt_ngaydongphi.get(),self.dathanhtoan_boolean.get())
                dangkyService.delete(hpdk.masv,hpdk.mahp)
                box = messagebox.showinfo("Thông báo", "Xóa thông tin đăng ký học phần thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Xóa thông tin đăng ký học phần thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")

    def setInfo(self, masv, mahp, ngaydangky, ngaydongphi, dathanhtoan):
        self.txt_masv.set(masv)
        self.txt_mahp.set(mahp)
        self.txt_ngaydangky.set(ngaydangky)
        self.txt_ngaydongphi.set(ngaydongphi)
        self.dathanhtoan_boolean.set(dathanhtoan)

    # return infohp_lbframe
class table():
    def __init__(self, frame, label_frame):
        self.lb_frame = label_frame
        self.table = ttk.Treeview(frame, columns=("1", "2", "3", "4", "5"), show="headings", selectmode="browse")
        self.load_table(frame)
    def load_table(self,frame):
        self.table.heading("1", text="MSSV")
        self.table.heading("2", text="Mã học phần")
        self.table.heading("3", text="Ngày đăng ký")
        self.table.heading("4", text="Ngày đóng phí")
        self.table.heading("5", text="Thanh toán")
        self.table.column('1',width=50, minwidth=60)
        self.table.column('2',width=100, minwidth=110)
        self.table.column('3',width=100, minwidth=110)
        self.table.column('4',width=100, minwidth=110)
        self.table.column('5',width=80, minwidth=85)

        # self.table.grid(row=0, column=0)
        self.table.pack(fill='both',expand=True)
        style = ttk.Style(self.table)
        style.configure('Treeview', rowheight=40)

        #scroll xbar
        scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command= self.table.xview)
        self.table.configure(xscrollcommand=scroll.set)
        scroll.pack(side=tk.BOTTOM, fill='x')
        self.load_data_table();
        self.lb_frame.subscribe_table(self)

    def load_data_table(self):
        self.table.delete(*self.table.get_children())
        for i in dangkyService.getAll():
            self.table.insert(parent='', index=tk.END, values=i.showInfo())
        self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)

    def handle_selectItem(self, event):
        selection = self.table.selection()
        for i in selection:
            store = self.table.item(i, "values")
            self.lb_frame.setInfo(store[0],store[1],store[2],store[3],store[4])