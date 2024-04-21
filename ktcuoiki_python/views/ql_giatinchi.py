from ktcuoiki_python.models.cruds import dangkyService,giatinchiService
from ktcuoiki_python.models.objects.giatinchi import giatinchi
import tkinter as tk
from tkinter import ttk, messagebox


class lb_frame():
    def __init__(self, frame ,btn_them, btn_sua,btn_xoa):
        self.table = None
        self.txt_gia = tk.StringVar()
        self.txt_namhoc = tk.StringVar()
        self.btn_them = btn_them
        self.btn_sua = btn_sua
        self.btn_xoa = btn_xoa
        self.load(frame)
    def load(self,frame):
        infohp_lbframe = tk.LabelFrame(frame, text="Thông tin giá tín chỉ")
        # infohp_lbframe.grid(row=1, column=0)
        infohp_lbframe.pack(fill='both',expand=True)
        # Tạo label
        gia_lb = tk.Label(infohp_lbframe, text="Giá tiền:")
        namhoc_lb = tk.Label(infohp_lbframe, text="Năm học:")


        # Tạo ô nhập
        gia_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_gia)
        namhoc_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_namhoc)


        # set vị trí cho khung thông tin

        # các label mỗi dòng cột 0
        gia_lb.grid(row=0, column=0)
        namhoc_lb.grid(row=1, column=0)


        # các entry ô nhập liệu mỗi dòng cột 1
        gia_entry.grid(row=0, column=1)
        namhoc_entry.grid(row=1, column=1)
        self.btn_them.config(command=lambda: self.insert())
        self.btn_sua.config(command=lambda: self.udate())
        self.btn_xoa.config(command=lambda: self.delete())
    def subscribe_table(self, table):
        self.table = table;

    def setInfo(self, gia, namhoc):
        self.txt_gia.set(gia)
        self.txt_namhoc.set(namhoc)
    def insert(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có chắc muốn thêm giá tín chỉ cho năm học này không?")
        if check == "yes":
            try:
                gtc = giatinchi(self.txt_gia.get(), self.txt_namhoc.get())
                giatinchiService.insert(gtc.gia,gtc.namhoc)
                box = messagebox.showinfo("Thông báo", "Thêm giá tín chỉ thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Thêm giá tín chỉ thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")

    def udate(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có chắc muốn sửa giá tín chỉ cho năm học này không?")
        if check == "yes":
            try:
                # gtc = giatinchi(self.txt_gia.get(), self.txt_namhoc.get())
                giatinchiService.update(int(self.txt_gia.get()), int(self.txt_namhoc.get()))
                box = messagebox.showinfo("Thông báo", "Sửa giá tín chỉ thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Sửa giá tín chỉ thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")
    def delete(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có chắc muốn xóa giá tín chỉ cho năm học này không?")
        if check == "yes":
            try:
                # gtc = giatinchi(self.txt_gia.get(), self.txt_namhoc.get())
                giatinchiService.delete(int(self.txt_namhoc.get()))
                box = messagebox.showinfo("Thông báo", "Xóa giá tín chỉ thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Xóa giá tín chỉ thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")

    # return infohp_lbframe
class table():
    def __init__(self, frame, label_frame):
        self.lb_frame = label_frame
        self.table = ttk.Treeview(frame, columns=("1", "2"), show="headings", selectmode="browse")
        self.load_table(frame)
    def load_table(self, frame):
        self.table.heading("1", text="Giá tiền")
        self.table.heading("2", text="Năm học")
        style = ttk.Style(self.table)
        style.configure('Treeview', rowheight=40)
        self.table.column('2', width=70, minwidth=80)
        # self.table.grid(row=0, column=0)
        
        self.table.pack(fill='both',expand=True)
        # scoll xbar
        scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command= self.table.xview)
        self.table.configure(xscrollcommand=scroll.set)
        scroll.pack(side=tk.BOTTOM, fill='x')
        # load dữ liệu tree view
        self.load_data_table()
        # đăng ký table của label frame = bảng này
        self.lb_frame.subscribe_table(self)
        # for i in giatinchiService.getAll():
        #     self.table.insert(parent='', index=tk.END, values=i.showInfo())
        # self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
    def load_data_table(self):
        self.table.delete(*self.table.get_children())
        for i in giatinchiService.getAll():
            self.table.insert(parent='', index=tk.END, values=i.showInfo())
        self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
    def handle_selectItem(self, event):
        selection = self.table.selection()
        for i in selection:
            store = self.table.item(i, "values")
            self.lb_frame.setInfo(store[0],store[1])