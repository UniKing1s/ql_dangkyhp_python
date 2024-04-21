from tkinter import *

from PIL import Image, ImageTk
from Frame.InfoFrame import InfoFrame
from Frame.Dshp import Dshp
from Frame.DshpDDK import DshpDDK
from ktcuoiki_python.models.cruds import sinhvienService


class main_view_user ():
    def __init__(self, masv):

        self.mssv = masv

        win = Toplevel()
        win.title('Ứng Dụng Quản Lý Đăng Ký Học Phần')
        win.geometry
        heightGlobal = 500
        WidthGlobal = 1070

        win.geometry(str(WidthGlobal) + "x" + str(heightGlobal))




        # frame tổng
        self.frame = Frame(win,bg='#b0c4de')
        self.frame.pack(fill='both', expand=True)




        # label tiêu đề
        title = Label(self.frame, text="QUẢN LÝ HỌC PHẦN CÁ NHÂN",bg='#b0c4de', fg='blue', font=('cambria', 20, 'bold'), width=40)
        title.pack(fill='x')




        # frame chứa các tính năng chính
        self.lbfrTong = LabelFrame(self.frame, bg='#b0c4de')
        self.lbfrTong.pack(fill='both', expand=True)




        # chứa thông tin, ảnh và chức năng
        self.lbfrLeft = LabelFrame(self.lbfrTong, bg='#b0c4de')
        self.lbfrLeft.pack(expand=True, fill='both', side=LEFT, anchor=W)




        # add hình ảnh
        self.img = Image.open("anhdaidien.jpg")
        self.img = self.img.resize((100, 100))
        self.img = ImageTk.PhotoImage(self.img)




        # frame chứa ảnh và thông tin
        self.lbfrInfo = LabelFrame(self.lbfrLeft, text="Thông tin sinh viên", bg='#b0c4de')
        self.lbfrInfo.pack(expand=True,fill='x', side=TOP,anchor=N)




        # add hình ảnh vào label chung với thông tin
        Lbimage = Label(self.lbfrInfo, image=self.img, compound=LEFT)
        # Lbimage = Label(self.lbfrInfo, text="hình", compound=LEFT)
        Lbimage.pack(side=LEFT,anchor='nw')
        Lbimage.config(borderwidth=1, relief="solid")




        # label chứa 3 label con hiển thị thông tin của sinh viên
        lbThongTin = Label(self.lbfrInfo, bg='#b0c4de')
        lbThongTin.pack(side=LEFT,anchor=E)

        self.lbTen = Label(lbThongTin,text='Nguyễn Đặng Huỳnh',anchor=W, bg='#b0c4de')
        self.lbTen.pack(fill="x")

        self.lbMssv = Label(lbThongTin,text='2108110327',anchor=W, bg='#b0c4de')
        self.lbMssv.pack(fill="x")

        self.lbLop = Label(lbThongTin,text='K15DCPM06',anchor=W, bg='#b0c4de')
        self.lbLop.pack(fill="x")


        self.lbfrRight = LabelFrame(self.lbfrTong)
        self.lbfrRight.pack(fill='both',expand=True, side=LEFT,anchor=W,ipadx=600)
        self.load_info_main()

        lbfrChucNang = LabelFrame(self.lbfrLeft, text="Chức Năng", bg='#b0c4de')
        lbfrChucNang.pack(side=BOTTOM, fill='both', expand=True, anchor=S, ipady=600)

        btInfo = Button(lbfrChucNang, text="Thông Tin Cá Nhân", command=self.getClickInfoSV)
        btInfo.pack(fill='x', side=TOP)

        btDKHP = Button(lbfrChucNang, text="Đăng Ký Học Phần", command=self.getClickDSHP)
        btDKHP.pack(fill='x', side=TOP)

        btDKHPed = Button(lbfrChucNang, text="Học Phần Đã Đăng Ký", command=self.getClickDSHPDDK)
        btDKHPed.pack(fill='x', side=TOP)

        btLogout = Button(lbfrChucNang, text="Đăng Xuất", bg='#fa8072', fg='#000000', command= lambda : win.destroy())
        btLogout.pack(fill='x', side=BOTTOM)
        win.mainloop()

    def getClickInfoSV(self):
        self.clearFrame()
        infoF = InfoFrame(self.lbfrRight)
        infoF.setFrame(self.mssv)

    def getClickDSHP(self):
        self.clearFrame()
        infoF = Dshp(self.lbfrRight, self.mssv)
        infoF.setDSHP()

    def getClickDSHPDDK(self):
        self.clearFrame()
        infoF = DshpDDK(self.lbfrRight)
        infoF.setDSHPDDK(self.mssv)

    def clearFrame(self):
        for i in self.lbfrRight.winfo_children():
            i.destroy()
    def load_info_main(self):
        sv = sinhvienService.getAllSVByMasv(self.mssv)[0]
        self.lbTen.config(text= sv.hodem + ' ' + sv.ten)
        self.lbMssv.config(text= sv.masv)
        self.lbLop.config(text= sv.malop)

        infoF = InfoFrame(self.lbfrRight)
        infoF.setFrame(self.mssv)



