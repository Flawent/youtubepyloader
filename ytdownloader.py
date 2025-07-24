from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys
import os
import ffmpeg

#finding the download folder
output_folder = os.path.join(os.path.expanduser("~"), "Downloads")

try:
     #making paths of temps for the ffmpeg
     video_path = os.path.join(output_folder, "temp_video.mp4")
     audio_path = os.path.join(output_folder, "temp_audio.mp4")

     #asking user youtube link to be inserted
     link = input("Insert your YouTube link: ")
     yt = YouTube(link, on_progress_callback=on_progress)
     print("")

     #making finalpaths of files for the ffmpeg
     finalvideo_path = os.path.join(output_folder, yt.title + ".mp4")
     finalaudio_path = os.path.join(output_folder, yt.title + ".mp3")

     #streams options
     videostream = yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True).order_by("resolution").desc().first()
     audiostream = yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True).order_by("abr").desc().first() 
     
     #asking user about only audio
     only_audio = input("Download only audio? y/n: ")
     print("")
     if only_audio == "y":
         audiostream.download(output_folder)
         print("Here your audio twin!! :P ")
         input("Press Enter to exit...")
         sys.exit()
     elif only_audio == "n":
          print("Proceeding then...")
         
     print("Video title: " + yt.title)
     print("")
     #downloading video and audio stream to merge later

     #video
     print("Downloading video stream now...")
     videostream.download(output_folder, filename = "temp_video.mp4")
     print("Downloaded this video stream! >o< ")
     print("")

     #audio
     print("Downloading audio stream now...")
     audiostream.download(output_folder, filename = "temp_audio.mp4")
     print("Downloaded this audio stream too! >o< ")
     print("")

     print("Merging now...")
     print("")
     #actually don't really even sure how this shit works ▼▼▼?? chatgpt ahh programming 
     
     ffmpeg.output(ffmpeg.input(video_path),
     ffmpeg.input(audio_path),
     finalvideo_path,
     vcodec='copy',
     acodec='aac',
     strict='experimental'
     ).run(overwrite_output=True, quiet=True)
     
     print(f"Done! ♡⸜(˶˃ ᵕ ˂˶)⸝♡. Saved as: {yt.title}.mp4")
     print("")
     #asking user if he wants to keep the audio

     audio_request = input("Want to have audio separately too? y/n: ")
     if audio_request == "y":
          print(f"Here you go twin!! >~<. Saved as: {yt.title}.mp3")
          os.remove(video_path)
          os.rename(src = audio_path, dst = finalaudio_path)
          input("Press Enter to exit...")
          sys.exit()
     elif audio_request == "n":
          print("Gotcha!")
          print("Now removing temp files...")
          os.remove(video_path)
          os.remove(audio_path)
          input("Press Enter to exit...")
          sys.exit()
     else:
          print("I didn't quite understood you... Type 'y' or 'n' next time, pls!")
          input("Press Enter to exit...")
          os.remove(video_path)
          os.remove(audio_path)
          sys.exit()     

except Exception as e:
     print(f"An error occurred. :( {e}")
     os.remove(video_path)
     os.remove(audio_path)
     input("Press Enter to exit...")