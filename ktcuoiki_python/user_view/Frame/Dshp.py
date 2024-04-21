from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from ktcuoiki_python.models.cruds import hocphanService,dangkyService
from ktcuoiki_python.models.objects.hocphan import hocphan
from ktcuoiki_python.models.objects.dkhp import dkhp
class Dshp():
    def __init__(self,frame, mssv):
        self.frame = frame
        self.mssv = mssv
    
    def setDSHP(self):

        LbTieude = Label(self.frame, text="Danh Sách Học Phần",bg='#b0c4de', fg='blue', font=('cambria', 20, 'bold'), width=40,)
        LbTieude.pack(fill='x')

        LbfrdshpTong = LabelFrame(self.frame, text="Danh Sách Học Phần",bg='#b0c4de')
        LbfrdshpTong.pack(expand=True,fill='both')
        #frame chứa ds hp
        Framedshp = Frame(LbfrdshpTong)
        Framedshp.pack(expand=True,fill='both', side=LEFT, anchor=W, ipadx=150)

        #frame chứa chức năng
        FramedshpChucNang = Frame(LbfrdshpTong)
        FramedshpChucNang.pack(expand=True,fill='both', side=RIGHT, anchor=W, ipadx=50)

        # FrameInfoHp = Frame(FramedshpChucNang)
        # FrameInfoHp.pack(expand=True,fill='x', side=TOP, anchor=N)
        BtDKHP = Button(FramedshpChucNang, text="Đăng ký học phần", foreground="white", background="blue",
                        font=("Arial", 12, "bold"))
        lb_frame_chuc_nang = lb_frame(FramedshpChucNang, BtDKHP,self.mssv)
        table_hp = table(Framedshp,lb_frame_chuc_nang,self.mssv)
        BtDKHP.pack(side=TOP, fill='x', expand=True, anchor=S)



class lb_frame():
    def __init__(self, frame, btndkhp, mssv):
        self.mssv = mssv
        self.table = None
        self.txt_mhp = tk.StringVar()
        self.txt_tenhp = tk.StringVar()
        self.txt_stc = tk.StringVar()
        self.txt_hk = tk.StringVar()
        self.btndkhp = btndkhp
        # self.btn_them = btn_them
        self.load(frame)

    def load(self,frame):
        infohp_lbframe = tk.LabelFrame(frame, text="Thông tin học phần")
        # infohp_lbframe.grid(row=0, column=0,padx=10, pady=10)
        infohp_lbframe.pack(fill='both',expand=True)
        # Tạo label
        mahp_lb = tk.Label(infohp_lbframe, text="Mã học phần:",font = ("Arial", 11, "bold"))
        tenhp_lb = tk.Label(infohp_lbframe, text="Tên học phần:",font = ("Arial", 11, "bold"))
        stc_lb = tk.Label(infohp_lbframe, text="Số tín chỉ:",font = ("Arial", 11, "bold"))
        hocki_lb = tk.Label(infohp_lbframe, text="Học kỳ: ",font = ("Arial", 11, "bold"))
        # Tạo ô nhập
        mahp_entry = tk.Label(infohp_lbframe, textvariable=self.txt_mhp)
        tenhp_entry = tk.Label(infohp_lbframe, textvariable=self.txt_tenhp)
        stc_entry = tk.Label(infohp_lbframe, textvariable=self.txt_stc)
        hocki_entry = tk.Label(infohp_lbframe, textvariable=self.txt_hk)
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
        # BtDKHP = Button(infohp_lbframe, text="Đăng ký học phần",foreground="white", background="blue")
        # # BtDKHP.pack(side=TOP, fill='x', expand=True, anchor=S)
        # BtDKHP.grid(row = 4, column = 0, columnspan=2)
        self.btndkhp.config(command=lambda: self.dk_hp())

        ###setting for button them sua xoa command
        # self.btn_them.config(command=lambda: self.insert_hp())
    def subscribe_table(self, table):
        self.table = table
    def setInfo(self, mahp,tenhp, stc,hocki):
        self.txt_mhp.set(mahp)
        self.txt_tenhp.set(tenhp)
        self.txt_stc.set(stc)
        self.txt_hk.set(hocki)
    def dk_hp(self):
        check = messagebox.askquestion("Thông báo",
                                       "Bạn có muốn đăng ký học phần này không?")
        if check == "yes":
            try:
                # hpdk = dkhp(self.txt_mhp.get(),self.txt_tenhp.get(),self.txt_stc.get(),self.txt_hk.get())
                dangkyService.insert(self.mssv,self.txt_mhp.get())
                box = messagebox.showinfo("Thông báo", "Đăng ký học phần thành công")
                self.table.load_data_table(self.mssv)
            except:
                box = messagebox.showerror("Thông báo",
                                           "Đăng ký học phần thất bại!!\nVui lòng kiểm tra lại thông tin đã chọn")

    # return infohp_lbframe
class table():
    def __init__(self, frame, label_frame ,mssv):
        self.lb_frame = label_frame
        self.table = ttk.Treeview(frame, columns=("1", "2", "3", "4"), show="headings",selectmode="browse")
        self.load_table(frame,mssv)
    def load_table(self,frame,mssv):
        self.table.heading("1", text="Mã HP")
        self.table.heading("2", text="Tên học phần")
        self.table.heading("3", text="STC")
        self.table.heading("4", text="Học kỳ")
        style = ttk.Style(self.table)
        style.configure('Treeview', rowheight=40)
        self.table.column('1',width=50, minwidth=60)
        self.table.column('2',width=175, minwidth=200)
        self.table.column('3',width=20, minwidth=20)
        self.table.column('4',width=20, minwidth=20)




        # self.table.grid(row=0, column=0)
        self.table.pack(fill='both',expand=True)
        scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command= self.table.xview)
        self.table.configure(xscrollcommand=scroll.set)
        scroll.pack(side=tk.BOTTOM, fill='x')


        # for i in hocphanService.getAll():
        #     self.table.insert(parent='', index=tk.END, values=i.showInfo())
        # self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
        self.load_data_table(mssv)
        self.lb_frame.subscribe_table(self)
    def load_data_table(self, masv):
        self.table.delete(*self.table.get_children())
        for i in hocphanService.getAllHpBySV(masv):
            self.table.insert(parent='', index=tk.END, values=i.showInfo())
        self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
    def handle_selectItem(self, event):
        selection = self.table.selection()
        for i in selection:
            store = self.table.item(i, "values")
            self.lb_frame.setInfo(store[0],store[1],store[2],store[3])