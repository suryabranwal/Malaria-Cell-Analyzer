import cv2
import glob
import os


class Malaria_Cell_Analyzer:
    dirList = glob.glob("media/*.png")
    for img_path in dirList:
        im = cv2.imread(img_path)
        im = cv2.GaussianBlur(im, (5, 5), 2)
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(im_gray, 127, 255, 0)
        _, contours, _ = cv2.findContours(thresh, 1, 2)

        for contour in contours:
            cv2.drawContours(im_gray, contours, -1, (0, 255, 0), 3)
            cv2.imwrite("media/processed.png", im_gray)
            cv2.imshow("window2", im_gray)
            cv2.waitKey(500)
        list = []
        k = 0
        for i in range(5):
            try:
                area = cv2.contourArea(contours[i])
                list.append([area])
            except:
                list.append([0])
        print(list)
        cv2.waitKey(20000)
        os.remove(img_path)

        break








