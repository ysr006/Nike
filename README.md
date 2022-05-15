# Nike

Arch Linux indirme uygulamasıdır. Türkçe dilindedir ve Türkiye'ye göre indirme yapar.

Klavye türkçe yapmak için

#loadkeys trq

İnternete bağlanmak için

#iwctl

iwd# wsc wlan0 push-button 1

iwd# station scan

iwd# station wlan0 SDDI_ISMI (Kendi ağ isminizi giriniz.)

pashhrase:******** (Kendi şifrenizi giriniz.)

iwd#exit #networkctl reconfigure wlan0

Script ve gerekli dosyaları indirmek için
#pacman -Sy

#pacman -S pacman-contrib sh nano git python

Yazınız.

myarchscript doyasını indirmek için

#git clone https://github.com/ysr006/myarchscript

yazınız.

Hata Öneri Destek İçin: https://www.youtube.com/channel/UCTlm2_b42fcfuQph76AChTQ
