from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys


try:
    
    link = input("Insert your YouTube link: ")
    yt = YouTube(link, on_progress_callback=on_progress)

    only_audio = input("Download only audio? y/n: ")

    stream = yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True).order_by("resolution").desc().first()
    audiostream = yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True).order_by("abr").desc().first()

    if only_audio == "y":
         audiostream.download(r"C:\Users\flawent\Downloads")
         print("Here your audio twin!! :P ")
         sys.exit()
    elif only_audio == "n":
         print("k bro :)")
         
    print("Video title: " + yt.title)
    print("Downloading right now...")

    
    stream.download(r"C:\Users\flawent\Downloads")

    print("Downloaded this shit! >o< ")
    audio_request = input("Download audio too? y/n: ")
    if audio_request == "y":
         audiostream.download(r"C:\Users\flawent\Downloads")
         print("Here you go twin!! >~< ")
    elif audio_request == "n":
         print("k twin")
    else:
         print("y or n, pls")

except Exception as e:
      print(f"An error occurred. :( {e}")