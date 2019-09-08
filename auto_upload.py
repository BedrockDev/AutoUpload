# import moviepy.editor as mp
# import imageio
# imageio.plugins.ffmpeg.download()
import glob
import os
from pathlib import Path
from datetime import date
import sys
import os

debug = True

home = str(Path.home())
today = date.today()
video_path = home + "/Videos/Logitech Webcam"
audio_path = home + "/OneDrive/오디오파일"
title_path = home + "/Desktop/업로드"

# read title.txt (contains 2 title texts divided with a line break)
f = open(title_path + "/title.txt", "rt", encoding='UTF8')

title_1 = f.readline()[:-1]
if "관악" not in title_1:
    title_1 += " 관악고신 유해신 목사 " + today.strftime("%Y-%m-%d") + " 오전성경공부"
if debug: print("Title 1: " + title_1)

title_2 = f.readline()
if "관악" not in title_2:
    title_2 += " 관악고신 유해신 목사 " + today.strftime("%Y-%m-%d") + " 주일예배"
if debug: print("Title 2: " + title_2)

list_of_files = glob.glob(video_path + "/*.mp4")
video_target = max(list_of_files, key=os.path.getctime)
if debug: print("Video target: " + video_target)

list_of_files = glob.glob(audio_path + "/*.mp3")
audio_target = max(list_of_files, key=os.path.getctime)
if debug: print("Audio target: " + audio_target)

#clip = mp.VideoFileClip(target)
#clip.audio.write_audiofile("theaudio.mp3")

if len(sys.argv) > 1:
    if sys.argv[1] is 'morning':
        if debug: print("Executing morning script: " + "ffmpeg -i " + video_path + "/" + video_target + " -b:a 96K -vn " + title_1 + ".mp3")
        # os.system("ffmpeg -i " + video_path + "/" + video_target + " -b:a 96K -vn " + title_1 + ".mp3")
    if sys.argv[1] is 'main':
        if debug: print("Executing main script: " + "ffmpeg -i " + video_path + "/" + video_target + " -b:a 96K -vn " + title_2 + ".mp3")
        # os.system("ffmpeg -i " + video_path + "/" + video_target + " -b:a 96K -vn " + title_2 + ".mp3")
else:
    if debug: print("Argument not available, define video type to process")
    # os.system("ffmpeg -i " + video_path + "/" + video_target + " -b:a 96K -vn audio.mp3")
