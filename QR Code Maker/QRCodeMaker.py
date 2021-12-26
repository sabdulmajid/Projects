# QRCodeMaker.py
import qrcode

img = qrcode.make("https://iamayman.tech/")
img.save("qr.png", "PNG")