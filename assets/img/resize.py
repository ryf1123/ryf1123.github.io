import cv2
import sys

a = cv2.imread("%s"%sys.argv[1])
a = cv2.resize(a, (150,150))
cv2.imwrite("%s"%sys.argv[1], a)