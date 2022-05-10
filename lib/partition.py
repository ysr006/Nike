import os

class Partition():
    def __init__(self,girdi1):
        self.girdi1 = girdi1
    def Partition(self):
        kod1 = 'echo "n\n\n\n\n\nw\n" | gdisk /dev{}'.format(self.girdi1)
        os.system(kod1)

class Uefi():
    def __init__(self,girdi1):
        self.girdi1 = girdi1
    def Uefi(self):
        kod2 = 'echo "n\n\n\n+512M\nef00\nw\n" | gdisk /dev{}'.format(self.girdi1)
        os.system(kod2)

class Swap():
    def __init__(self,girdi1,girdi3):
        self.girdi1 = girdi1
        self.girdi3 = girdi3
    def Uefi(self):
        kod3 = 'echo "n\n\n\n+{}\n8200\nw\n" | gdisk /dev{}'.format(self.girdi1,self.girdi3)
        os.system(kod3)