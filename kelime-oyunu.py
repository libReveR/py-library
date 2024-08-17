import random

# Kelime listesi
kelimeler = ["elma", "armut", "muz", "çilek", "kiraz", "karpuz", "kavun", "portakal", "mandalina", "üzüm"]

# Rastgele bir kelime seç
kelime = random.choice(kelimeler)

# Oyuncuya kelimenin uzunluğunu ve ilk harfini göster
print(f"Kelimenin uzunluğu: {len(kelime)}")
print(f"İlk harf: {kelime[0]}")

# Oyuncunun tahminlerini al
tahminler = []
hak = 5

while hak > 0:
    tahmin = input("Bir kelime tahmin edin: ")
    if tahmin == kelime:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    else:
        hak -= 1
        tahminler.append(tahmin)
        print(f"Yanlış tahmin. Kalan hak: {hak}")

if hak == 0:
    print(f"Maalesef, doğru kelime '{kelime}' idi.")

print("Tahminleriniz:", tahminler)
