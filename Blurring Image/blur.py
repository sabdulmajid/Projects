# blur.py
# Importing blur tools from the PIL (Python Imaging Library) and blurring an image.
from PIL import Image, ImageFilter

original = Image.open('G:\My Drive\Python Programmes\Projects\Blurring Image\\bridge.bmp')
processed = original.filter(ImageFilter.BoxBlur(10)) 
processed.save("G:\My Drive\Python Programmes\Projects\Blurring Image\\blurred_bridge.bmp")