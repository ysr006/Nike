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
girdi7 = input("Hangi işlemciyi/işlemcileri kullanıyorsunuz? [İ]ntel [A]md [N]vdia  Birden fazla seçim yapılabilir.Örnek IAN AN gibi :")
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
        os.system('pacman -S intel-ucode')

    if process == "A":
        os.system('pacman -S amd-ucode')

    if process == "N":
        os.system('pacman -S nvidia')

for graphic in girdi8:
    if graphic == "I":
        os.system('pacman -S xf86-video-intel')

    if graphic == "A":
        os.system('pacman -S xf86-video-amdgpu xf86-video-ati')

    if graphic == "N":
        os.system('pacman -S xf86-video-nouveau')

# En son olarak grub ayarlayıp kurulumu bitiriyoruz
if girdi2 == "U":
    os.system('grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB')

elif girdi2 == "L":
    os.system('grub-install --recheck /dev/{}'.format(girdi1))

os.system('grub-mkconfig -o /boot/grub/grub.cfg')
os.system('mkinitcpio -P')
os.system('pacman -S lightdm xorg')
os.system('systemctl enable lightdm')

for gui in girdi9:
    if gui == "P":
        os.system('pacman -S plasma kde-applications')

    if gui == "M":
        os.system('pacman -S mate mate-extra')

    if gui == "I":
        os.system('pacman -S i3')

    if gui == "X":
        os.system('pacman -S xfce4 xfce4-goodies')

girdi11 = str(girdi11)
os.system('useradd -m -G wheel -s /bin/bash {}'.format(girdi10))
os.system('passwd'.format(girdi11))
os.system('echo "{}" | passwd {}'.format(girdi11,girdi10))
os.system('echo "{} ALL=(ALL:ALL) ALL" >> /etc/sudoers'.format(girdi10))
os.system('exit')
os.system('umount -R /mnt')
os.system('shutdown now')

