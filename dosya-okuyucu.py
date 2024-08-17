import os

# Kullanıcıdan dosya konumunu al
dosya_konumu = input("Dosya konumunu giriniz: ")

# Dosya konumundaki dosya ve klasörleri listele
try:
    dosyalar = os.listdir(dosya_konumu)
    print(f"{dosya_konumu} konumundaki dosya ve klasörler:")
    for dosya in dosyalar:
        print(dosya)
except FileNotFoundError:
    print("Belirtilen dosya konumu bulunamadı.")
except NotADirectoryError:
    print("Belirtilen konum bir dosya değil, lütfen bir klasör konumu girin.")
except PermissionError:
    print("Bu konuma erişim izniniz yok.")

print("İşlem tamamlandı.")
