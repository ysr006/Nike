from lib.partition import partition

print("Merhaba ben Nike. Adımı yunan mitolojisinden alan 3. programım.")
print("Rahatala ve arkana yaslan.Arch Linux kurulumununda tüm zor işlemleri ben halledeceğim.")
print("\nAma önce size bazı sorular sormam gerekiyor. Sizin memnuniyetiniz benim için en önemli şey")

girdi1 = input("Sanal makineye mi kurulum yoksa gerçek makineye mi? [S]anal / [G]erçek")
if girdi1 == "G":
    girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz?")
    print("\nEğer legacy kurulum yapacaksanız programdan çıkıp fdisk ile bölümlendirin")
    if girdi2 == "U":
        partition.Uefigercek()
    girdi3 = input("8 GB swap alanı olsun mu? [E]vet / [H]ayır :")
    if girdi3 == "E":
        partition.Swapgercek()
    partition.Partitiongercek()

else:
    girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz?")
    print("\nEğer legacy kurulum yapacaksanız programdan çıkıp fdisk ile bölümlendirin")
    if girdi2 == "U":
        partition.Uefisanal()
    girdi3 = input("8 GB swap alanı olsun mu? [E]vet / [H]ayır :")
    if girdi3 == "E":
        partition.Swapsanal()
    partition.Partitionsanal()


# girdi4 = input("hangi biçimde kurulum yapmak istersin.Örnek:ext4,btrfs")
# girdi5 = input("Ne tür harddisk kullanıyorsunuz.Örnek:hdd,sdd")