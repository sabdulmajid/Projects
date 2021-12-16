# DownloadingYouTubeVideos.py
# Very simple way to download YouTube videos using Python Web-Scraping.

from __future__ import unicode_literals
import youtube_dl


input_link = input('Please enter your link and press space after it, then press enter: ')
ydl_opts = {'outtmpl': 'c:\\Users\\Programming\\Desktop\\Videos\\%(title)s.%(ext)s'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([input_link])
