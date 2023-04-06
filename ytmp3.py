from pytube import YouTube
import os

url = 'https://www.youtube.com/watch?v=FSVHx23ByhM'
video = YouTube(url)
print('Title : ', video.title)
print('Downloading...') 
out_path = video.streams.filter(only_audio=True).first().download()
new_name = os.path.splitext(out_path)[0] + '.mp3'
os.rename(out_path, new_name)
