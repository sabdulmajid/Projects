# RemovingCharacterFromFile.py
# Making this program to cut down excess text present in pre-named files from the Internet.

import os

path = r"C:\Users\shaik\Videos\Intuitive - S1"
for filename in os.listdir(path):
    new_filename = filename.replace('Exam Hack_ CIE AS Maths _ S1 _ ', '')
    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))