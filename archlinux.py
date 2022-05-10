from lib import partition


print("Merhaba ben Nike. Adımı yunan mitolojisinden alan 3. programım.")
print("Rahatala ve arkana yaslan.Arch Linux kurulumununda tüm zor işlemleri ben halledeceğim.")
print("\nAma önce size bazı sorular sormam gerekiyor. Sizin memnuniyetiniz benim için en önemli şey")

girdi1 = input("hangi bölüme kurulum yapacaksınız?Örnek:sda,sdb... vs")
girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz?")
if girdi2 == "U":
    partition.Uefi()
    girdi3 = input("Swap alanı ne kadar olsun?Örnek:off,+8,+16...vs")
    if girdi3 != "off":
        partition.Swap()
    partition.Partition()

    # girdi4 = input("hangi biçimde kurulum yapmak istersin.Örnek:ext4,btrfs")
    # girdi5 = input("Ne tür harddisk kullanıyorsunuz.Örnek:hdd,sdd")
    #
    #
