import os
import sys
from urllib.request import urlopen
from urllib.request import build_opener
import subprocess
import glob
##prefix="La-Salle-College-3 320--000"
##tsfile = open("final.ts", 'ab')
##for root, dirs, files in os.walk(".", topdown=False):
##    for name in files:
##        a = os.path.join(root, name)
##        infile = a
##        outfile = a.replace(".ts",".mp4")
##        subprocess.run(['ffmpeg', '-i', infile, outfile])

from moviepy.editor import *
import os
from natsort import natsorted

L =[]

for root, dirs, files in os.walk("./"):

    #files.sort()
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile("output.mp4", fps=24, remove_temp=False)
