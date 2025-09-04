import qrcode
from PIL import Image, ImageDraw, ImageFont

data = "QFDEM"
#data = "https://www.obramax.com.br/piso%20porcelanato?_q=piso%20porcelanato&map=ft"
titulo = "QFDEM"

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="orange", back_color="blue")
qr_img = qr_img.convert('RGB')

img_width, img_height = qr_img.size
nova_altura = img_height + 80
nova_img = Image.new('RGB', (img_width, nova_altura), 'white')

nova_img.paste(qr_img, (0, 60))

draw = ImageDraw.Draw(nova_img)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
except:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), titulo, font=font)
text_width = bbox[2] - bbox[0]
x = (img_width - text_width) // 2

draw.text((x, 20), titulo, fill='black', font=font)

nova_img.save("qrcode_linkedin.png")