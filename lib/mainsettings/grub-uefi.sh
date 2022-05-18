echo 'grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
mkinitcpio -P
pacman -S xorg
systemctl enable lightdm
exit
' | arch-chroot /mnt
