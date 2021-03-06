import cv2
import sys


def load_image(image_path):
    return cv2.imread(image_path)


def gray_image(image):
    gray = image
    if image.ndim == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def get_detector(cascade_path):
    return cv2.CascadeClassifier(cascade_path)


def detect_faces(detector, gray_scale_image):
    return detector.detectMultiScale(
        gray_scale_image,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )


def draw_rectangles(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)


def show_wait_destroy(image):
    cv2.imshow("Faces found!", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image_path = sys.argv[1]
    cascade_path = '../resources/haarcascade_frontalface_default.xml'

    image = load_image(image_path)
    gray_scale_image = gray_image(image)
    detector = get_detector(cascade_path)
    faces = detect_faces(detector, gray_scale_image)
    if len(faces) == 0:
        print "Faces have been not found!"
        return
    draw_rectangles(image, faces)
    show_wait_destroy(image)


if __name__ == '__main__':
    main()
