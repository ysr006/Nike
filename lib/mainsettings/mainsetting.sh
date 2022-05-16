arch-chroot /mnt
ln -sf /usr/share/zoneinfo/Europe/Istanbul /etc/localtime
hwclock --systohc
echo "tr_TR.UTF-8 UTF-8" >> /etc/locale.gen
echo "tr_TR ISO-8859-9" >> /etc/locale.gen
locale-gen
echo "LANG=tr_TR.UTF-8" >> /etc/locale.conf
echo "KEYMAP=trq" >> /etc/vconsole.conf
echo "archlinux" >> /etc/hostname
echo "127.0.0.1   localhost" >> /etc/hosts
echo "::1         localhost" >> /etc/hosts
echo "127.0.1.1   archlinux.localdomain  archlinux" >> /etc/hosts
pacman -S grub grub-btrfs os-prober efibootmgr dosfstools mtools dialog wpa_supplicant network-manager-applet bluez-utils cups xdg-utils xdg-user-dirs pulseaudio alsa-utils gvfs
systemctl enable NetworkManager
systemctl enable bluetooth.service
systemctl enable cups