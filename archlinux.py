import os

print("Merhaba ben Nike. Adımı yunan mitolojisinden alan 3. programım.")
print("Rahatala ve arkana yaslan.Arch Linux kurulumununda tüm zor işlemleri ben halledeceğim.")
print("\nAma önce size bazı sorular sormam gerekiyor. Sizin memnuniyetiniz benim için en önemli şey")

girdi1 = input("Sanal makineye mi kurulum yoksa gerçek makineye mi? [S]anal / [G]erçek")
if girdi1 == "G":
    girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz?")
    print("\nEğer legacy kurulum yapacaksanız programdan çıkıp fdisk ile bölümlendirin")
    if girdi2 == "U":
        os.system('sh ~/Nike/lib/partition/Uefigercek.sh')
    girdi3 = input("8 GB swap alanı olsun mu? [E]vet / [H]ayır :")
    if girdi3 == "E":
        os.system('sh ~/Nike/lib/partition/Swapgercek.sh')
    os.system('sh ~/Nike/lib/partition/Partitiongercek.sh')

else:
    girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz?")
    print("\nEğer legacy kurulum yapacaksanız programdan çıkıp fdisk ile bölümlendirin")
    if girdi2 == "U":
        os.system('sh ~/Nike/lib/partition/Uefisanal.sh')
    girdi3 = input("8 GB swap alanı olsun mu? [E]vet / [H]ayır :")
    if girdi3 == "E":
        os.system('sh ~/Nike/lib/partition/Swapsanal.sh')
    os.system('sh ~/Nike/lib/partition/Partitionsanal.sh')


# girdi4 = input("hangi biçimde kurulum yapmak istersin.Örnek:ext4,btrfs")
# girdi5 = input("Ne tür harddisk kullanıyorsunuz.Örnek:hdd,sdd")