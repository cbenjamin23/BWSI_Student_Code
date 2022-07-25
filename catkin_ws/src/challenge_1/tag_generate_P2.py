#this file was unecessary
import numpy as np
import cv2

# LOAD CORRECT TAG DICTIONARY
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
SIZE = 500 # pixels

# CREATE ARRAY FOR MARKER
marker = np.zeros((SIZE, SIZE, 1), dtype=np.uint8)

# DRAW AND SAVE MARKER
ID1 = 5
cv2.aruco.drawMarker(arucoDict, ID1, SIZE, marker, 1)
cv2.imwrite('DICT_ARUCO_ORIGINAL_id_{}_{}.png'.format(ID1, SIZE), marker)
ID2 = 10
cv2.aruco.drawMarker(arucoDict, ID2, SIZE, marker, 1)
cv2.imwrite('DICT_ARUCO_ORIGINAL_id_{}_{}.png'.format(ID2, SIZE), marker)