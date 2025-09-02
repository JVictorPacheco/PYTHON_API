import qrcode

data = "Opá, isso é um teste"

img = qrcode.make(data)

img.save("qrcode_linkedin.png")