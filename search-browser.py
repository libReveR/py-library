import webbrowser

# Kullanıcıdan arama terimini al
arama_terimi = input("Aramak istediğiniz nedir? ")

# Arama URL'sini oluştur
url = f"https://www.google.com/search?q={arama_terimi}"

# Tarayıcıda arama yap
webbrowser.open(url)

print("Arama sonuçları tarayıcıda açıldı.")
