import os

print("Merhaba ben Nike. Adımı yunan mitolojisinden alan 3. programım.")
print("Rahatala ve arkana yaslan.Arch Linux kurulumununda tüm zor işlemleri ben halledeceğim.")
print("\nAma önce size bazı sorular sormam gerekiyor. Sizin memnuniyetiniz benim için en önemli şey")

girdi1 = input("Sanal makineye mi kurulum yoksa gerçek makineye mi? [S]anal / [G]erçek")
if girdi1 == "G":
    girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz?")
    if girdi2 == "U":
        os.system('sh ~/Nike/lib/partition/Uefigercek.sh')
    girdi3 = input("8 GB swap alanı olsun mu? [E]vet / [H]ayır :")
    if girdi3 == "E":
        os.system('sh ~/Nike/lib/partition/Swapgercek.sh')

else:
    girdi2 = input("\n\nSoru 1: [U]efi mi yoksa [L]egacy mu kurululm yapıyorsunuz?")
    if girdi2 == "U":
        os.system('sh ~/Nike/lib/partition/Uefisanal.sh')
    girdi3 = input("8 GB swap alanı olsun mu? [E]vet / [H]ayır :")
    if girdi3 == "E":
        os.system('sh ~/Nike/lib/partition/Swapsanal.sh')

os.system('sh ~/Nike/lib/partition/Partitionsanal.sh')
#
# print("Bölüm oluşturma bitti şimdi biçimlendirme zamanı...")
#
# girdi4 = input("[E]xt4 mü kuracaksınız yoksa [B]trfs mi?:")