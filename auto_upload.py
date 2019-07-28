# import moviepy.editor as mp
# import imageio
# imageio.plugins.ffmpeg.download()
import glob
import os
from pathlib import Path

home = str(Path.home())
video_path = home + "/Videos/Logitech Webcam"
audio_path = home + "/OneDrive/오디오파일"

list_of_files = glob.glob(video_path + "/*.mp4")
target = max(list_of_files, key=os.path.getctime)

print(target[:-4])

list_of_files = glob.glob(audio_path + "/*.mp3")
target = max(list_of_files, key=os.path.getctime)

print(target)

#clip = mp.VideoFileClip(target)
#clip.audio.write_audiofile("theaudio.mp3")
