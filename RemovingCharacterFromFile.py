# RemovingCharacterFromFile.py
# Making this program to cut down excess text present in pre-named files from the Internet.

import os

path = r"G:\My Drive\AS & A Past Papers\Topical Questions\Pure Maths 3 - Topical Questions"
for filename in os.listdir(path):
    new_filename = filename.replace('Worksheet - P3 - ', '')
    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))