# DownloadingFiles.py
import requests
import wget
# Downloading an image from a certain URL.
image_url = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'

r = requests.get(image_url)

with open("python_logo.png", 'wb') as f:
    f.write(r.content)

# The file is stored in the current directory - i.e. New Python Programs folder.

url = 'https://www.python.org/static/img/python-logo@2x.png'

aymansfile = requests.get(url)

open('c:/Users/Programming/Desktop/Test/aymansfile.png', 'wb').write(aymansfile.content)

url2 = 'https://www.python.org/static/community_logos/python-powered-w-100x40.png'

wget.download(url2, 'c:/Users/Programming/Desktop/Test/python_logo.jpg')

