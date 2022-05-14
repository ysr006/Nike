import os

print("Merhaba ben Nike. Adımı yunan mitolojisinden alan 3. programım.")
print("Rahatala ve arkana yaslan.Arch Linux kurulumununda tüm zor işlemleri ben halledeceğim.")
print("\nAma önce size bazı sorular sormam gerekiyor. Sizin memnuniyetiniz benim için en önemli şey")

girdi1 = input("Hangi bölüme kuracaksınız? Örnek:sda,sdb,vda,... vs")
girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz?")
if girdi2 == "U":
    os.system('sh ~/Nike/lib/partition/Uefi.sh | gdisk /dev/{}'.format(girdi1))
girdi3 = input("Swap alanı olsun mu? [E]vet / [H]ayır :")
if girdi3 == "E":
    os.system('sh ~/Nike/lib/partition/Swap.sh | gdisk /dev/{}'.format(girdi1))

os.system('sh ~/Nike/lib/partition/Partition.sh |gdisk /dev/{}'.format(girdi1))
#
# print("Bölüm oluşturma bitti şimdi biçimlendirme zamanı...")
#
# girdi4 = input("[E]xt4 mü kuracaksınız yoksa [B]trfs mi?:")