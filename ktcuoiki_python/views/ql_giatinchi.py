from ktcuoiki_python.models.cruds import dangkyService,giatinchiService

import tkinter as tk
from tkinter import ttk
class lb_frame():
    def __init__(self, frame):
        self.txt_gia = tk.StringVar()
        self.txt_namhoc = tk.StringVar()
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



    def setInfo(self, gia, namhoc):
        self.txt_gia.set(gia)
        self.txt_namhoc.set(namhoc)

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

        for i in giatinchiService.getAll():
            self.table.insert(parent='', index=tk.END, values=i.showInfo())
        self.table.bind('<<TreeviewSelect>>', self.handle_selectItem)
    def handle_selectItem(self, event):
        selection = self.table.selection()
        for i in selection:
            store = self.table.item(i, "values")
            self.lb_frame.setInfo(store[0],store[1])