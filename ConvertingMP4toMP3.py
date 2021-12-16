# ConvertingMP4toMP3.py
from moviepy.editor import *

mp4_file = r'c:\\Users\\Programming\\Desktop\\Videos\\26th Ramadan 1441 Makkah Taraweeh Sheikh Dosary.mp4\\'
mp3_file = r'c:\\Users\\Programming\\Desktop\\Videos\\26th Ramadan 1441 Makkah Taraweeh Sheikh Dosary.mp3\\'

videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)

audioclip.close()
videoclip.close()
