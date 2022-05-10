import os

class Partition():
    gridi1 = ""
    kod1 = 'echo "n\n\n\n\n\nw\n" | gdisk /dev{}'.format(girdi1)
    os.system(kod1)

class Uefi():
    girdi = ""
    kod2 = 'echo "n\n\n\n+512M\nef00\nw\n" | gdisk /dev{}'.format(girdi1)
    os.system(kod2)

class Swap():
    girdi1 = ""
    girdi3 = ""
    kod3 = 'echo "n\n\n\n+{}\n8200\nw\n" | gdisk /dev{}'.format(girdi1,girdi3)
    os.system(kod3)
