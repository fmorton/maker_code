import cv2 as cv

video = cv.VideoCapture(1)

while True:
    status, frame = video.read()

    cv.imshow("Video Display", frame)

    cv.namedWindow(
        "Video Display", cv.WINDOW_NORMAL
    )  # size must be specified or thonny hangs
    cv.resizeWindow("Video Display", 640, 360)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

print("Release...")
video.release()
print("Release...Done")

cv.destroyAllWindows()
print("Destroy Windows...Done")
cv.waitKey(1)
print("All Done")
