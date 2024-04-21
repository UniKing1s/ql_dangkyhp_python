from ktcuoiki_python.models.cruds import hocphanService
from ktcuoiki_python.models.objects.hocphan import hocphan
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class lb_frame():
    def __init__(self, frame, btn_them, btn_sua, btn_xoa):
        self.table = None
        self.txt_mhp = tk.StringVar()
        self.txt_tenhp = tk.StringVar()
        self.txt_stc = tk.StringVar()
        self.txt_hk = tk.StringVar()
        self.btn_them = btn_them
        self.btn_sua = btn_sua
        self.btn_xoa = btn_xoa
        self.load(frame)

    def load(self,frame):
        infohp_lbframe = tk.LabelFrame(frame, text="Thông tin học phần")
        # infohp_lbframe.grid(row=0, column=0,padx=10, pady=10)
        infohp_lbframe.pack(fill='both',expand=True)
        # Tạo label
        mahp_lb = tk.Label(infohp_lbframe, text="Mã học phần:")
        tenhp_lb = tk.Label(infohp_lbframe, text="Tên học phần:")
        stc_lb = tk.Label(infohp_lbframe, text="Số tín chỉ:")
        hocki_lb = tk.Label(infohp_lbframe, text="Học kì: ")
        # Tạo ô nhập
        mahp_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_mhp)
        tenhp_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_tenhp)
        stc_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_stc)
        hocki_entry = tk.Entry(infohp_lbframe, textvariable=self.txt_hk)
        # set vị trí cho khung thông tin
        # các label mỗi dòng cột 0
        mahp_lb.grid(row=0, column=0)
        tenhp_lb.grid(row=1, column=0)
        stc_lb.grid(row=2, column=0)
        hocki_lb.grid(row=3, column=0)
        # các entry ô nhập liệu mỗi dòng cột 1
        mahp_entry.grid(row=0, column=1)
        tenhp_entry.grid(row=1, column=1)
        stc_entry.grid(row=2, column=1)
        hocki_entry.grid(row=3, column=1)
        ###setting for button them sua xoa command
        self.btn_them.config(command=lambda: self.insert_hp())
        self.btn_xoa.config(command=lambda: self.delete_hp())
        self.btn_sua.config(command = lambda: self.update_hp())
    def subscribe_table(self, table):
        self.table = table;
    def setInfo(self, mahp,tenhp, stc,hocki):
        self.txt_mhp.set(mahp)
        self.txt_tenhp.set(tenhp)
        self.txt_stc.set(stc)
        self.txt_hk.set(hocki)
    def insert_hp(self):
        check = messagebox.askquestion("Thông báo",
                                       "Mã học phần sẽ tự động tạo mới!\nBạn có muốn thêm học phần này không?")
        if check == "yes":
            try:
                hp = hocphan(self.txt_mhp.get(),self.txt_tenhp.get(),self.txt_stc.get(),self.txt_hk.get())
                hocphanService.insert(hp)
                box = messagebox.showinfo("Thông báo", "Thêm học phần thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Thêm học phần thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")
    def delete_hp(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có chắc là xóa học phần này không?")
        if check == "yes":
            try:
                hp = hocphan(self.txt_mhp.get(),self.txt_tenhp.get(),self.txt_stc.get(),self.txt_hk.get())
                hocphanService.delete(hp.mahp)
                box = messagebox.showinfo("Thông báo", "Xóa học phần thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Xóa học phần thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")
    def update_hp(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có muốn sửa học phần này không?")
        if check == "yes":
            try:
                hp = hocphan(self.txt_mhp.get(),self.txt_tenhp.get(),self.txt_stc.get(),self.txt_hk.get())
                hocphanService.update(hp)
                box = messagebox.showinfo("Thông báo", "Sửa học phần thành công")
                self.table.load_data_table()
            except:
                box = messagebox.showerror("Thông báo",
                                           "Sửa học phần thất bại!!\nVui lòng kiểm tra lại thông tin đã nhập")

    # return infohp_lbframe
class table():
    def __init__(self, frame, label_frame):
        self.lb_frame = label_frame
        self.table = ttk.Treeview(frame, columns=("1", "2", "3", "4"), show="headings",selectmode="browse")
        self.load_table(frame)
    def load_table(self,frame):
        self.table.heading("1", text="Mã HP")
        self.table.heading("2", text="Tên học phần")
        self.table.heading("3", text="STC")
        self.table.heading("4", text="Học kỳ")
        style = ttk.Style(self.table)
        style.configure('Treeview', rowheight=40)
        self.table.column('1',width=50, minwidth=60)
        # self.table.column('2',width=175, minwidth=200)
        # self.table.column('3',width=30, minwidth=40)
        # self.table.column('4',width=30, minwidth=40)




        # self.table.grid(row=0, column=0)
        self.table.pack(fill='both',expand=True)
        scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command= self.table.xview)
        self.table.configure(xscrollcommand=scroll.set)
        scroll.pack(side=tk.BOTTOM, fill='x')


        # for i in hocphanService.getAll():
        #     self.table.insert(parent='', index=tk.END, values=i.showInfo())
        # self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
        self.load_data_table()
        self.lb_frame.subscribe_table(self)
    def load_data_table(self):
        self.table.delete(*self.table.get_children())
        for i in hocphanService.getAll():
            self.table.insert(parent='', index=tk.END, values=i.showInfo())
        self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
    def handle_selectItem(self, event):
        selection = self.table.selection()
        for i in selection:
            store = self.table.item(i, "values")
            self.lb_frame.setInfo(store[0],store[1],store[2],store[3])



