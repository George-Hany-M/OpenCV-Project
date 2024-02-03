import cv2


# This function will be called whenever a mouse event occurs.
# 'event' The type of mouse event (left button down, right button down, etc.).
# 'x' The x-coordinate of the mouse click
# 'y' The y-coordinate of the mouse click
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('[x, y] = ', '[', x, ', ', y, ']')
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' + str(y), (x, y), font, 1, (255, 0, 0), 2)  # BGR
        cv2.imshow('Colors', img)
        # If the left mouse button is clicked, it prints the x and y coordinates to the console
        # and overlays these coordinates on the image

    if event == cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x, y), font, 1, (255, 255, 0), 2)
        print('[Three Colors] = ', '[', b, ', ', g, ', ', r, ']')
        cv2.imshow('Colors', img)
        # If the right mouse button is clicked, it prints the x and y coordinates along
        # with the BGR values of the pixel at that location


while True:
    img = cv2.imread('D:\\LEVEL - 3\\Semester - 1\\Computer Vision\\Project\\Image (1).jpeg', 1)

    img = cv2.resize(img, (600, 650))  # width of 500 pixels and height of 550 pixels.

    cv2.imshow('Colors', img)
    cv2.setMouseCallback('Colors', click_event)

    if cv2.waitKey(0) == ord('s'):
        cv2.imwrite('saved_image.jpg', img)
        print('Image saved as "saved_image.jpg" in files of this program.')
        cv2.destroyAllWindows()
        break

    elif cv2.waitKey(0) == 27:  # Check if the 'ESC' key is pressed to exit
        cv2.destroyAllWindows()
        break
