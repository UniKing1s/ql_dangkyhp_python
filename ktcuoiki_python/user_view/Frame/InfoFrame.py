from tkinter import *
from ktcuoiki_python.models.cruds import sinhvienService
from PIL import Image, ImageTk

class InfoFrame():
    def __init__(self,frame):
    # win = Tk()
    # win.title('Ứng Dụng Quản Lý Đăng Ký Học Phần')
    # win.geometry
    # heightGlobal = 500
    # WidthGlobal = 800

    # win.geometry(str(WidthGlobal) + "x" + str(heightGlobal))
# frame tổng
        self.frame = frame

    def setFrame(self, mssv):
        sinhvien = sinhvienService.getAllSVByMasv(mssv)[0]
# label chứa thanh tiêu đề
        LbTieude = Label(self.frame, text="Thông Tin Sinh Viên",bg='#b0c4de', fg='blue', font=('cambria', 20, 'bold'), width=40,)
        LbTieude.pack(fill='x')


        # frame chứa thông tin
        LbFrInfo = LabelFrame(self.frame, text="Thông Tin Sinh Viên", bg='#b0c4de')
        LbFrInfo.pack(expand=True,fill='both')


        # label frame chứa các label xuất thông tin
        LbFrInfoElement =Frame(LbFrInfo, bg='#b0c4de')
        LbFrInfoElement.pack(expand=True, fill='both', side=LEFT, anchor=W)


        # các label xuất thông tin
        LbMasv = Label(LbFrInfoElement, text="MSSV : ", bg='#b0c4de', fg='blue', font=('cambria', 15))
        LbMasv.place(x=10, y=10)
        OutMssv = Label(LbFrInfoElement, text= sinhvien.masv, bg='#b0c4de', font=('cambria', 15))
        OutMssv.place(x=170, y=10)

        # masv, hodem, ten, ngaysinh, gioitinh, noisinh, malop

        LbHoTenSV = Label(LbFrInfoElement, text="Họ Tên : " , bg='#b0c4de', fg='blue', font=('cambria', 15))
        LbHoTenSV.place(x=10, y=50)
        OutHoTenSV = Label(LbFrInfoElement, text= sinhvien.hodem + ' ' + sinhvien.ten, bg='#b0c4de', font=('cambria', 15))
        OutHoTenSV.place(x=170, y=50)

        LbGioiTinh = Label(LbFrInfoElement, text="Giới tính : ",bg='#b0c4de', fg='blue', font=('cambria', 15))
        LbGioiTinh.place(x=10, y=90)
        if sinhvien.gioitinh == 1:
                gioitinh = 'nam'
        else:
                gioitinh ='nu'
        OutGioiTinh = Label(LbFrInfoElement, text= gioitinh, bg='#b0c4de', font=('cambria', 15))
        OutGioiTinh.place(x=170, y=90)

        LbLop = Label(LbFrInfoElement, text="Lớp : ",bg='#b0c4de', fg='blue', font=('cambria', 15))
        LbLop.place(x=10, y=130)
        OutLop = Label(LbFrInfoElement, text=sinhvien.malop, bg='#b0c4de', font=('cambria', 15))
        OutLop.place(x=170, y=130)

        LbNgaySinh = Label(LbFrInfoElement, text="Ngày sinh : ",bg='#b0c4de', fg='blue', font=('cambria', 15))
        LbNgaySinh.place(x=10, y=170)
        OutNgaySinh = Label(LbFrInfoElement, text= sinhvien.ngaysinh, bg='#b0c4de', font=('cambria', 15))
        OutNgaySinh.place(x=170, y=170)

        LbNoiSinh = Label(LbFrInfoElement, text="Nơi sinh : ",bg='#b0c4de', fg='blue', font=('cambria', 15))
        LbNoiSinh.place(x=10, y=210)
        OutNoiSinh = Label(LbFrInfoElement, text= sinhvien.noisinh, bg='#b0c4de', font=('cambria', 15))
        OutNoiSinh. place(x=170, y=210)




# win.mainloop()

