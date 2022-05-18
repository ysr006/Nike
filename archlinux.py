# Kütüphaneler

import os
import time


# Giriş

print("Merhaba ben Nike. Arch Linux kurulum asistanıyım.")
print("Rahatala ve arkana yaslan.Arch Linux kurulumununda tüm zor işlemleri ben halledeceğim.")
print("\nAma önce size bazı sorular sormam gerekiyor. Sizin memnuniyetiniz benim için en önemli şey")


# Kullanıcıdan istenen girdiler

girdi1 = input("Hangi bölüme kuracaksınız? Örnek:sda,sdb,vda,... vs :")
girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz? :")
girdi3 = input("Swap alanı olsun mu? [E]vet / [H]ayır :")
girdi4 = input("[E]xt4 mü kuracaksınız yoksa [B]trfs mi? :")
girdi5 = input("Harddiskiniz [H]DD mi yoksa [S]SD mi? :")
girdi6 = input("1.) Linux\n2.) Linux lts\n3.) Linux Zen\nHangi kerneli indireceksiniz? Örnek:1 :")
girdi7 = input("Hangi işlemciyi/işlemcileri kullanıyorsunuz? [İ]ntel [A]md Birden fazla seçim yapılabilir.Örnek IA gibi :")
girdi8 = input("Hangi ekran kartı/ekran kartlarını kullanıyorsunuz? [İ]ntel [A]md [N]vdia  Birden fazla seçim yapılabilir.Örnek IAN AN gibi :")
girdi9 = input("Hangi masaüstü ortamını/oertamlarını yüklemek istersin? [P]lasma [M]ate [I]3 [X]fce4. Birden fazla seçim yapılabilir.Örnek PMI MX gibi :")
girdi10 = input("Kullanıcı adı giriniz.Örnek:arch :")
print("Hatırlatma şifrenizi kaydetmeniz önerilir.")
girdi11 = input("Şifrenizi giriniz :")
print("Artık gerisi bende. 30 sn içinde başlayacak Kurulumu yapıp bilgisayarı kapatacağım. Açıldığında herşey hazır olacak.")
time.sleep(30)

# Bölümleme

if girdi2 == "U":
    os.system('sh ~/Nike/lib/partition/Uefi.sh | gdisk /dev/{}'.format(girdi1))
if girdi3 == "E":
    os.system('sh ~/Nike/lib/partition/Swap.sh | gdisk /dev/{}'.format(girdi1))

os.system('sh ~/Nike/lib/partition/Partition.sh |gdisk /dev/{}'.format(girdi1))

# Bölüm oluşturma efi bölümü swap bölümü ve btrfs bölümü ext4 ya da btrfs formatında

if girdi4 == "E" and girdi3 == "E" and girdi2 == "U":
    os.system('mkfs.fat -F 32 /dev/{}1'.format(girdi1))
    os.system('mkswap /dev/{}2'.format(girdi1))
    os.system('mkfs.ext4 /dev/{}3'.format(girdi1))

elif girdi4 == "E" and girdi3 == "H" and girdi2 == "U":
    os.system('mkfs.fat -F 32 /dev/{}1'.format(girdi1))
    os.system('mkfs.ext4 /dev/{}2'.format(girdi1))

elif girdi4 == "E" and girdi3 == "E" and girdi2 == "L":
    os.system('mkswap /dev/{}1'.format(girdi1))
    os.system('mkfs.ext4 /dev/{}2'.format(girdi1))

elif girdi4 == "E" and girdi3 == "H" and girdi2 == "L":
    os.system('mkfs.ext4 /dev/{}1'.format(girdi1))

elif girdi4 == "B" and girdi3 == "E" and girdi2 == "U":
    os.system('mkfs.fat -F 32 /dev/{}1'.format(girdi1))
    os.system('mkswap /dev/{}2'.format(girdi1))
    os.system('mkfs.btrfs -f /dev/{}3'.format(girdi1))

elif girdi4 == "B" and girdi3 == "H" and girdi2 == "U":
    os.system('mkfs.fat -F 32 /dev/{}1'.format(girdi1))
    os.system('mkfs.btrfs -f /dev/{}2'.format(girdi1))

elif girdi4 == "B" and girdi3 == "E" and girdi2 == "L":
    os.system('mkswap /dev/{}1'.format(girdi1))
    os.system('mkfs.btrfs -f /dev/{}2'.format(girdi1))

elif girdi4 == "B" and girdi3 == "H" and girdi2 == "L":
    os.system('mkfs.btrfs /dev/{}1'.format(girdi1))

# Bağlama işlemi yapıyoruz.

if girdi2 == "U" and girdi3 == "E" and girdi4 == "E":
    os.system('mount /dev/{}3 /mnt'.format(girdi1))
    os.system('swapon /dev/{}2'.format(girdi1))
    os.system('mkdir -p /mnt/boot')
    os.system('mkdir -p /mnt/boot/efi')
    os.system('mount /dev/{}1 /mnt/boot/efi'.format(girdi1))

elif girdi2 == "U" and girdi3 == "H" and girdi4 == "E":
    os.system('mount /dev/{}2 /mnt'.format(girdi1))
    os.system('mkdir -p /mnt/boot')
    os.system('mkdir -p /mnt/boot/efi')
    os.system('mount /dev/{}1 /mnt/boot/efi'.format(girdi1))

elif girdi2 == "L" and girdi3 == "E" and girdi4 == "E":
    os.system('mount /dev/{}2 /mnt'.format(girdi1))
    os.system('swapon /dev/{}1'.format(girdi1))

elif girdi2 == "L" and girdi3 == "H" and girdi4 == "E":
    os.system('mount /dev/{}1 /mnt'.format(girdi1))

elif girdi2 == "U" and girdi3 == "E" and girdi4 == "B":
    os.system('mount /dev/{}3 /mnt'.format(girdi1))
    os.system('btrfs subvolume create /mnt/@')
    os.system('btrfs subvolume create /mnt/@home')
    os.system('btrfs subvolume create /mnt/@var')

    if girdi5 == "H":
        os.system('mount -o noatime,compress=zstd,subvol=@ /dev/{}3 /mnt'.format(girdi1))
        os.system('mkdir -p /mnt/home')
        os.system('mkdir -p /mnt/var')
        os.system('mount -o noatime,compress=zstd,subvol=@home /dev/{}3 /mnt/home'.format(girdi1))
        os.system('mount -o noatime,compress=zstd,subvol=@var /dev/{}3 /mnt/var'.format(girdi1))
        os.system('swapon /dev/{}2'.format(girdi1))
        os.system('mkdir -p /mnt/boot')
        os.system('mkdir -p /mnt/boot/efi')
        os.system('mount /dev/{}1 /mnt/boot/efi'.format(girdi1))

    elif girdi5 == "S":
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@ /dev/{}3 /mnt'.format(girdi1))
        os.system('mkdir -p /mnt/home')
        os.system('mkdir -p /mnt/var')
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@home /dev/{}3 /mnt/home'.format(girdi1))
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@var /dev/{}3 /mnt/var'.format(girdi1))
        os.system('swapon /dev/{}2'.format(girdi1))
        os.system('mkdir -p /mnt/boot')
        os.system('mkdir -p /mnt/boot/efi')
        os.system('mount /dev/{}1 /mnt/boot/efi'.format(girdi1))

if girdi2 == "U" and girdi3 == "H" and girdi4 == "B":
    if girdi5 == "H":
        os.system('mount -o noatime,compress=zstd,subvol=@ /dev/{}2 /mnt'.format(girdi1))
        os.system('mkdir -p /mnt/home')
        os.system('mkdir -p /mnt/var')
        os.system('mount -o noatime,compress=zstd,subvol=@home /dev/{}2 /mnt/home'.format(girdi1))
        os.system('mount -o noatime,compress=zstd,subvol=@var /dev/{}2 /mnt/var'.format(girdi1))
        os.system('mkdir -p /mnt/boot')
        os.system('mkdir -p /mnt/boot/efi')
        os.system('mount /dev/{}1 /mnt/boot/efi'.format(girdi1))

    elif girdi5 == "S":
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@ /dev/{}2 /mnt'.format(girdi1))
        os.system('mkdir -p /mnt/home')
        os.system('mkdir -p /mnt/var')
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@home /dev/{}2 /mnt/home'.format(girdi1))
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@var /dev/{}2 /mnt/var'.format(girdi1))
        os.system('mkdir -p /mnt/boot')
        os.system('mkdir -p /mnt/boot/efi')
        os.system('mount /dev/{}1 /mnt/boot/efi'.format(girdi1))

if girdi2 == "L" and girdi3 == "E" and girdi4 == "B":
    if girdi5 == "H":
        os.system('mount -o noatime,compress=zstd,subvol=@ /dev/{}2 /mnt'.format(girdi1))
        os.system('mkdir -p /mnt/home')
        os.system('mkdir -p /mnt/var')
        os.system('mount -o noatime,compress=zstd,subvol=@home /dev/{}2 /mnt/home'.format(girdi1))
        os.system('mount -o noatime,compress=zstd,subvol=@var /dev/{}2 /mnt/var'.format(girdi1))
        os.system('swapon /dev/{}1'.format(girdi1))

    elif girdi5 == "S":
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@ /dev/{}2 /mnt'.format(girdi1))
        os.system('mkdir -p /mnt/home')
        os.system('mkdir -p /mnt/var')
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@home /dev/{}2 /mnt/home'.format(girdi1))
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@var /dev/{}2 /mnt/var'.format(girdi1))
        os.system('swapon /dev/{}1'.format(girdi1))

if girdi2 == "L" and girdi3 == "H" and girdi4 == "B":
    if girdi5 == "H":
        os.system('mount -o noatime,compress=zstd,subvol=@ /dev/{}1 /mnt'.format(girdi1))
        os.system('mkdir -p /mnt/home')
        os.system('mkdir -p /mnt/var')
        os.system('mount -o noatime,compress=zstd,subvol=@home /dev/{}1 /mnt/home'.format(girdi1))
        os.system('mount -o noatime,compress=zstd,subvol=@var /dev/{}1 /mnt/var'.format(girdi1))

    elif girdi5 == "S":
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@ /dev/{}1 /mnt'.format(girdi1))
        os.system('mkdir -p /mnt/home')
        os.system('mkdir -p /mnt/var')
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@home /dev/{}1 /mnt/home'.format(girdi1))
        os.system('mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@var /dev/{}1 /mnt/var'.format(girdi1))

# Bölümleri yazdırma ve gerekli paketlerin kurulumunun yapıldığı yer

os.system('sh ~/Nike/lib/baseinstall/install.sh')
girdi6 = str(girdi6)
if girdi6 == "1":
    os.system('pacstrap /mnt linux linux-headers')
elif girdi6 == "2":
    os.system('pacstrap /mnt linux-lts linux-lts-headers')
elif girdi6 == "3":
    os.system('pacstrap /mnt linux-zen linux-zen-headers')

# Genel ayarlamaların yapıldığı yer (zaman host vs...)

os.system('sh ~/Nike/lib/mainsettings/mainsetting.sh')

for process in girdi7:
    if process == "I":
        os.system('sh ~/Nike/lib/mainsettings/process-intel.sh')

    if process == "A":
        os.system('sh ~/Nike/lib/mainsettings/process-amd.sh')


for graphic in girdi8:
    if graphic == "I":
        os.system('sh ~/Nike/lib/mainsettings/graphic-intel.sh')

    if graphic == "A":
        os.system('sh ~/Nike/lib/mainsettings/graphic-amd.sh')

    if graphic == "N":
        os.system('sh ~/Nike/lib/mainsettings/graphic-nvidia.sh')

# En son olarak grub ayarlayıp kurulumu bitiriyoruz
if girdi2 == "U":
    os.system('sh ~/Nike/lib/mainsettings/grub-uefi.sh')

elif girdi2 == "L":
    legacy = open("lib/final/","w")
    legacy.write(f'echo "grubinstall --recheck /dev/{girdi1}\ngrubmkconfig -o /boot/grub/grub.cfg\nmkinitcpio -P\npacman -S xorg\nsystemctl enable lightdm\nexit\n"| arch-chroot /mnt')
    legacy.close()
    os.system('sh ~/Nike/lib/mainsettings/grub-legacy.sh')

for gui in girdi9:
    if gui == "P":
        os.system('sh ~/Nike/lib/final/plasma.sh')

    if gui == "M":
        os.system('sh ~/Nike/lib/final/mate.sh')

    if gui == "I":
        os.system('sh ~/Nike/lib/final/i3.sh')

    if gui == "X":
        os.system('sh ~/Nike/lib/final/xfce.sh')

final = open("lib/final/final.sh")
final.write('echo "useradd -m -G wheel -s /bin/bash {girdi10}\npasswd\n{girdi11}\npasswd {girdi10}\n{girdi11}\necho "{} ALL=(ALL:ALL) ALL" >> /etc/sudoers\nexit\n" | arch-chroot /mnt')
os.system('sh ~/Nike/lib/final/finalsh')
os.system('umount -R /mnt')
os.system('shutdown now')

