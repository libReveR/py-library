from pytube import YouTube
from pydub import AudioSegment
import os

# Kullanıcıdan YouTube video URL'sini al
video_url = input("YouTube video URL'sini giriniz: ")

# YouTube videosunu indir
yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()
out_file = video.download(output_path=".")

# Dosya adını değiştir ve MP3 formatına dönüştür
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
audio = AudioSegment.from_file(out_file)
audio.export(new_file, format="mp3")

# Geçici dosyayı sil
os.remove(out_file)

print(f"{yt.title} başarıyla MP3 formatına dönüştürüldü ve {new_file} olarak kaydedildi.")
