import cv2
import matplotlib.pyplot as plt
import numpy as np

imagePath = r"C:\Users\Michal jr. K\OneDrive\Dokumenty\aaaaProgramming\ETS2-Autopilot\images\highway_straight+shadow.jpg"
baseImage = cv2.imread(imagePath)

## Returns only the region of interest
def regionOfInterest(image):
    height, width = image.shape
    rectangle = np.array([
        [(700, height-550), (950, 325), (1000, 325), (width-450, height-550)]
    ])
    ## Black image of baseImage dimensions
    mask = np.zeros_like(image)
    ## Fills mask with image, leaving only the region of interest
    mask = cv2.fillPoly(mask, rectangle, 255)
    mask = cv2.bitwise_and(image, mask)
    return mask

def makePoints(image, average):
    # print(average)
    slope, y_int = average
    y1 = image.shape[0]
    ## How long we want our lines to be --> 3/5 the size of the image
    y2 = int(y1 * (3/5))
    ## Determine algebraically
    x1 = int((y1 - y_int) // slope)
    x2 = int((y2 - y_int) // slope)
    return np.array([x1, y1, x2, y2])

def averageLines(image, lines):
    left = []
    right = []

    if lines is not None:
      for line in lines:
        print(line)
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        print(parameters)
        slope = parameters[0]
        y_int = parameters[1]
        if slope < 0:
            left.append((slope, y_int))
        else:
            right.append((slope, y_int))

    ## Takes the average between all the columns (column0: slope, column1: y_int)
    right_avg = np.average(right, axis=0)
    left_avg = np.average(left, axis=0)
    ## Creates lines based on average calculates done above
    left_line = makePoints(image, left_avg)
    right_line = makePoints(image, right_avg)
    return np.array([left_line, right_line])

def drawLines(image, lines):
    lines_image = np.zeros_like(image)
    #make sure array isn't empty
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line
            #draw lines on a black image
            cv2.line(lines_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return lines_image

def findLanes(image):
    ## Creates a greyscale image
    #image = np.asarray(image)
    #greyImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    ## Creates a copy of the image
    copy1 = np.copy(image)

    ## Reduces noise
    blurredImage = cv2.GaussianBlur(copy1, (5, 5), 0)
    # cv2.imshow("blurred", blurredImage)
    # cv2.waitKey(0)

    ## Shows the outlines in the image
    edgesImage = cv2.Canny(blurredImage, 255/3, 255)
    # cv2.imshow("edges", edgesImage)
    # cv2.waitKey(0)

    ## Isolates the region of interest
    isolated = regionOfInterest(edgesImage)
    cv2.imshow("isolated", isolated)
    cv2.waitKey(0)

    lines = cv2.HoughLinesP(isolated, 2, np.pi/180, 60, np.array([]), minLineLength=2, maxLineGap=10)
    #cv2.imshow("houghed", lines)
    #cv2.waitKey(0)
    try:
        averaged_lines = averageLines(copy1, lines)
    except: pass
    black_lines = drawLines(copy1, averaged_lines)
    ## Taking weighted sum of original image and lane lines image
    lanes = cv2.addWeighted(copy1, 0.8, black_lines, 1, 1)
    cv2.imshow("lanes", lanes)

    ## Doesn't close until user presses a key
    cv2.waitKey(0)

findLanes(baseImage)