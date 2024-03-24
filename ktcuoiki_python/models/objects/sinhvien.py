class Sinhvien:
    def __init__(self, masv, hodem, ten, ngaysinh, gioitinh, noisinh, malop ):
        self.masv = masv
        self.hodem = hodem
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.gioitinh = gioitinh
        self.noisinh = noisinh
        self.malop = malop
    def showInfo(self):
        return (self.masv, self.hodem, self.ten, self.ngaysinh, self.gioitinh, self.noisinh, self.malop)