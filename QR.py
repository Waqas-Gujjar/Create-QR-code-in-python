import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://github.com/Waqas-Gujjar/Create-QR-code-in-python");
img = qr.make_image(fill_color="black" , back_color="lightgray")
qr.make(fit=True)
img.save("GitHub.png")

