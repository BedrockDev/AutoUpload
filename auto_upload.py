import glob
import eyed3
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
temp_path = "C:/Temp/auto_upload_audio.mp3"

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

def tag_ID3(title):
    # load tags
    audiofile = eyed3.load(temp_path)
    # audiofile.initTag()
    if debug: print("tag_ID3: loaded file from " + temp_path)
    if debug and audiofile is None: print("audiofile is None")
    # read image into memory
    imagedata = open("cover.jpg", "rb").read()
    # append image to tags
    audiofile.tag.images.set(3, imagedata, "image/jpeg", u"Cover image")
    audiofile.tag.artist = u"유해신 목사님"
    audiofile.tag.album = u"관악교회"
    audiofile.tag.title = title
    audiofile.tag.release_date = today.year

    # write it back
    audiofile.tag.save()

if len(sys.argv) > 1:
    if debug: print("Argument: " + sys.argv[1])
    if sys.argv[1] == "morning":
        # Video file renaming
        os.rename(video_target, video_path + "/" + title_1 + ".mp4")
        video_target = video_path + "/" + title_1 + ".mp4"

        # ffmpeg script
        script = "ffmpeg -i \"" + video_target + "\" -b:a 96K -vn \"" + temp_path
        if debug: print("Executing morning script: " + script)
        os.system(script)
        
        # ID3 Tagging
        tag_ID3(title_1)
        os.rename(temp_path, audio_path + "/" + title_1 + ".mp3")
    if sys.argv[1] == 'main':
        # Video file renaming
        os.rename(video_target, video_path + "/" + title_2 + ".mp4")
        video_target = video_path + "/" + title_2 + ".mp4"

        # ffmpeg script
        script = "ffmpeg -i \"" + video_target + "\" -b:a 96K -vn \"" + temp_path
        if debug: print("Executing main script: " + script)
        os.system(script)
        
        # ID3 Tagging
        tag_ID3(title_2)
        os.rename(temp_path, audio_path + "/" + title_2 + ".mp3")
else:
    if debug: print("Argument not available, define video type to process")
    # os.system("ffmpeg -i " + video_path + "/" + video_target + " -b:a 96K -vn audio.mp3")
