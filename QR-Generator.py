# steps for execution :-
# - give any link in "dataUrl" variable where you want to redirect your QR-Code.
# - execute the program, then you will get a message that QR is generated.
# - make sure to check the path of terminal, your QR will be generated in that path.
# - scan that QR and you will be redirected to that link


import pyqrcode  # make sure to install "pyqrcode" -- "pip install pyqrcode"

dataUrl = "https://www.linkedin.com/in/amitcoder/"       # This "dataUrl" hold the link where you will be redirected when you scan Qr-code
qr = pyqrcode.create(dataUrl)            # This line will create QR using "dataUrl"
qr.png("QR-Code.png", scale=5)           # QR will be generated in the form of image ,# scale is used for the size of the QR-code
print("QR Generated Successfully")
