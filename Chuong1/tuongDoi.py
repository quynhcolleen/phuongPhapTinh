class saiSoTuongDoi:
    def __init__(self, ganDung, tuyetDoi):
        self.ganDung = ganDung
        self.tuyetDoi = tuyetDoi
        
    def TuongDoi(self):
        print(f"a* = {self.ganDung} ± {self.tuyetDoi}")
        print()
        tuongDoi = self.ganDung / self.tuyetDoi
        print(f"=> δa = ∆a / |a|")
        print(f"=> δa = {self.ganDung} / {self.tuyetDoi}")
        print(f"=> δa = {tuongDoi}")