import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time
import keyboard

print('hello')

config = ('-l eng --oem 1 --psm 3')

while True:

    time.sleep(1)
    im = ImageGrab.grab(bbox=(75,500,300,600))
    #im.save('scr1.png', 'png')
    img_np = np.array(im)

    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    cv2.imshow("Screen",frame)

    text = pytesseract.image_to_string(im, config=config)
    print(text)
    #keyboard.write(text)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
