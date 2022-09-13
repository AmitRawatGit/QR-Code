# Steps for execution :-
# - install two modules "pip install pyzbar" and "pip install pillow".
# - give a link or path of QR-Code that you want to read in "qrCodeImg" variable.
# - execute the code then you will get the link that the QR-Code holds.

from pyzbar.pyzbar import decode
from PIL import Image

qrCodeImg = Image.open("QR-code.png")  # this variable holds the link/path of an QR image

linkFromQR = decode(qrCodeImg) # this line reads the QR image and stores the data found from QR into "linkFromQR"

# checking if some data is found from the image or not
if linkFromQR[0].data.decode():
    print("---------- Successfully Decodes QR-Code ----------")
    print("QR-Code holds this link :- ", linkFromQR[0].data.decode())

else:
    print("**************************")
    print("Error : unable to read QR-Code")
    print("QR may holds no link or ,QR may be unreadable or ,path of the QR image may be wrong !!")
    print("**************************")
