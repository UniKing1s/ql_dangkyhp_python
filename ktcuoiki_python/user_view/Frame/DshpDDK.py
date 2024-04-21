import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from ktcuoiki_python.models.cruds import dangkyService

class DshpDDK():
    def __init__(self,frame):
        self.frame = frame
    
    def setDSHPDDK(self, masv):

        LbTieude = Label(self.frame, text="Danh Sách Học Phần Đã Đăng Ký",bg='#b0c4de', fg='blue', font=('cambria', 20, 'bold'), width=40,)
        LbTieude.pack(fill='x')

        LbfrdshpTong = LabelFrame(self.frame, text="Danh Sách Học Phần Đã Đăng Ký",bg='#b0c4de')
        LbfrdshpTong.pack(expand=True,fill='both')
        ## danh sách
        Framedshp = Frame(LbfrdshpTong)
        Framedshp.pack(expand=True,fill='both', side=LEFT, anchor=W, ipadx=150)
        ##chuc năng
        FramedshpChucNang = Frame(LbfrdshpTong)
        FramedshpChucNang.pack(expand=True,fill='both', side=RIGHT, anchor=W, ipadx=50)
        #
        # Load thông tin vô bảng và ô
        label_frame = lb_frame(FramedshpChucNang)
        table_frame = table(Framedshp, label_frame, masv)



class lb_frame():
    def __init__(self, frame):
        self.table = None
        self.txt_masv = tk.StringVar()
        self.txt_mahp = tk.StringVar()
        self.txt_ngaydangky = tk.StringVar()
        self.txt_ngaydongphi = tk.StringVar()
        self.dathanhtoan_boolean = tk.IntVar()
        self.dathanhtoan_label = tk.StringVar()
        self.tongtien = tk.IntVar()
        self.load(frame)
    def load(self,frame):
        infohp_lbframe = tk.LabelFrame(frame, text="Thông tin đăng ký học phần")
        # infohp_lbframe.grid(row=0, column=0,padx=10, pady=10)
        infohp_lbframe.pack(fill='both',expand=True)
        # Tạo label
        masv_lb = tk.Label(infohp_lbframe, text="Mã sinh viên:",font = ("Arial", 11, "bold"))
        mahp_lb = tk.Label(infohp_lbframe, text="Mã học phần:",font = ("Arial", 11, "bold"))
        ngaydangky_lb = tk.Label(infohp_lbframe, text="Ngày đăng ký:",font = ("Arial", 11, "bold"))
        ngaydongphi_lb = tk.Label(infohp_lbframe, text="Ngày đóng phí:",font = ("Arial", 11, "bold"))
        dathanhtoan_lb = tk.Label(infohp_lbframe, text="Thanh toán: ",font = ("Arial", 11, "bold"))
        tongtien_lb = tk.Label(infohp_lbframe, text="Tổng tiền học phần: ", font=("Arial", 11, "bold"))
        # Tạo ô nhập
        masv_entry = tk.Label(infohp_lbframe, textvariable=self.txt_masv)
        mahp_entry = tk.Label(infohp_lbframe, textvariable=self.txt_mahp)
        # self.txt_ngaydangky.set('alvsdvsdv')
        ngaydangky_lb_show = tk.Label(infohp_lbframe, textvariable=self.txt_ngaydangky)
        ngaydongphi_lb_show = tk.Label(infohp_lbframe, textvariable=self.txt_ngaydongphi)
        tongtien_lb_show = tk.Label(infohp_lbframe, textvariable=self.tongtien)

        # tk.StringVar()
        dathanhtoan_lb_show = tk.Label(infohp_lbframe, textvariable = self.dathanhtoan_label)

        # dathanhtoan_lb_show = tk.Entry(infohp_lbframe, textvariable=self.txt_dathanhtoan)
        # set vị trí cho khung thông tin

        # các label mỗi dòng cột 0
        masv_lb.grid(row=0, column=0)
        mahp_lb.grid(row=1, column=0)
        ngaydangky_lb.grid(row=2, column=0)
        ngaydongphi_lb.grid(row=3, column=0)
        dathanhtoan_lb.grid(row=4, column=0)
        tongtien_lb.grid(row=5, column=0)

        # các entry ô nhập liệu mỗi dòng cột 1
        masv_entry.grid(row=0, column=1)
        mahp_entry.grid(row=1, column=1)
        ngaydangky_lb_show.grid(row=2, column=1)
        ngaydongphi_lb_show.grid(row=3, column=1)
        dathanhtoan_lb_show.grid(row=4, column=1)
        tongtien_lb_show.grid(row=5,column=1)
        ###setting for button them sua xoa command
    def subscribe_table(self, table):
        self.table = table
    def setInfo(self, masv, mahp, ngaydangky, ngaydongphi, dathanhtoan, tongtien):
        self.txt_masv.set(masv)
        self.txt_mahp.set(mahp)
        self.txt_ngaydangky.set(ngaydangky)
        self.txt_ngaydongphi.set(ngaydongphi)
        self.dathanhtoan_boolean.set(dathanhtoan)
        self.tongtien.set(tongtien)
        if dathanhtoan == 1:
            self.dathanhtoan_label.set("Đã thanh toán")
        else:
            self.dathanhtoan_label.set("Chưa thanh toán")
class table():
    def __init__(self, frame, label_frame, masv):
        self.lb_frame = label_frame
        self.table = ttk.Treeview(frame, columns=("1", "2", "3", "4", "5","6"), show="headings", selectmode="browse")
        self.load_table(frame,masv)
    def load_table(self,frame,masv):
        self.table.heading("1", text="MSSV")
        self.table.heading("2", text="Mã học phần")
        self.table.heading("3", text="Ngày đăng ký")
        self.table.heading("4", text="Ngày đóng phí")
        self.table.heading("5", text="Thanh toán")
        self.table.heading("6", text="Tổng tiền hp")
        self.table.column('1',width=40, minwidth=40)
        self.table.column('2',width=40, minwidth=40)
        self.table.column('3',width=70, minwidth=70)
        self.table.column('4',width=70, minwidth=70)
        self.table.column('5',width=30, minwidth=20)
        self.table.column('5', width=50, minwidth=50)

        # self.table.grid(row=0, column=0)
        self.table.pack(fill='both',expand=True)
        style = ttk.Style(self.table)
        style.configure('Treeview', rowheight=40)

        #scroll xbar
        scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command= self.table.xview)
        self.table.configure(xscrollcommand=scroll.set)
        scroll.pack(side=tk.BOTTOM, fill='x')
        self.load_data_table(masv)
        self.lb_frame.subscribe_table(self)

    def load_data_table(self, masv):
        self.table.delete(*self.table.get_children())
        for i in dangkyService.getAllByMasvHaveMoney(masv):
            self.table.insert(parent='', index=tk.END, values=i.showInfoWithTong())
        self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)

    def handle_selectItem(self, event):
        selection = self.table.selection()
        for i in selection:
            store = self.table.item(i, "values")
            self.lb_frame.setInfo(store[0],store[1],store[2],store[3],store[4],store[5])