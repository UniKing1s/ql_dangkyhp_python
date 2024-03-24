from ktcuoiki_python.models.cruds import hocphanService

class hpcontroller:
    def __init__(self):
        pass
    def getAll(self):
        return hocphanService.getAll()
    def insert(self, hocphan):
        hocphanService.insert(hocphan)
    def delete(self, mamh):
        hocphanService.delete(mamh)
    def update(self, hocphan):
        hocphanService.update(hocphan)