class dkhp:
    def __init__(self,masv , mahp, ngaydangky, ngaydongphi, dadongphi):
        self.tongtienhp = None
        self.masv = masv
        self.mahp = mahp
        self.ngaydangky = ngaydangky
        self.ngaydongphi = ngaydongphi
        self.dadongphi = dadongphi
    def showInfo(self):
        return (self.masv, self.mahp, self.ngaydangky, self.ngaydongphi, self.dadongphi)
    def setTongTien(self,tong):
        self.tongtienhp = tong
    def showInfoWithTong(self):
        return (self.masv, self.mahp, self.ngaydangky, self.ngaydongphi, self.dadongphi, self.tongtienhp)