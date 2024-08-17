from flask import Flask, request, send_file
from pytube import YouTube
from pydub import AudioSegment
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_video():
    video_url = request.form['url']
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=".")
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    audio = AudioSegment.from_file(out_file)
    audio.export(new_file, format="mp3")
    
    os.remove(out_file)
    
    return send_file(new_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
