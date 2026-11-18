"""Make a QR code (PNG + SVG) for your permanent certificate URL.

Usage:
    pip install qrcode[pil]
    python make_qr.py https://your-project.vercel.app

Run this ONCE, after the site is deployed. The QR never needs to change.
"""
import sys
import qrcode
import qrcode.image.svg

if len(sys.argv) != 2 or not sys.argv[1].startswith("http"):
    sys.exit("Usage: python make_qr.py https://your-project.vercel.app")

url = sys.argv[1]
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=4)
qr.add_data(url)
qr.make(fit=True)

qr.make_image(fill_color="black", back_color="white").save("certificate-qr.png")
qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save("certificate-qr.svg")
print(f"Saved certificate-qr.png and certificate-qr.svg for {url}")
