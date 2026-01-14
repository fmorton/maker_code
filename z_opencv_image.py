import cv2 as cv

image = cv.imread("python.png", -1)  # -1=unchanged 0=grayscale 1=color

if image is not None:
    print("Image loaded...")
    cv.imshow("Window Name Here", image)

    key = cv.waitKey(5000)

    if key != -1:
        key = chr(key)
    else:
        key = None

    print("Key...", key, key.__class__.__name__)

    print("Copy image...")
    cv.imwrite("python_2.jpeg", image)

    print("Clear image...")

    cv.waitKey(1)
    cv.destroyAllWindows()
    cv.waitKey(1)
