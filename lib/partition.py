import os

girdi1 = ""
girdi3 = ""

class Partition():
    kod1 = 'echo "n\n\n\n\n\nw\n" | gdisk /dev{}'.format(girdi1)
    os.system(kod1)

class Uefi():
    kod2 = 'echo "n\n\n\n+512M\nef00\nw\n" | gdisk /dev{}'.format(girdi1)
    os.system(kod2)

class Swap():
    kod3 = 'echo "n\n\n\n+{}\n8200\nw\n" | gdisk /dev{}'.format(girdi1,girdi3)
    os.system(kod3)