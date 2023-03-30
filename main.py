import segno
from PIL import Image

# create qr code object
url = "https://github.com/"
qr = segno.make(url, error='h')

# save qr code as png file
qr.save("qrcode.png", dark="#0A6A56", scale=20)

# open qr code image
img = Image.open("qrcode.png")
img = img.convert("RGBA")

# open logo image
logo = Image.open("logo.png")
logo = logo.convert("RGBA")

# resize logo according to img size
img_w, img_h = img.size
logo_w, logo_h = logo.size
ratio = min(img_w / (4 * logo_w), img_h / (4 * logo_h))
new_logo_w = int(logo_w * ratio)
new_logo_h = int(logo_h * ratio)
logo = logo.resize((new_logo_w, new_logo_h))

# paste logo on top of img
img.paste(logo, ((img_w - new_logo_w) // 2, (img_h - new_logo_h) // 2), mask=logo)

# save img
img.save("qrcode.png")