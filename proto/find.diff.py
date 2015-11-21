import numpy as np
import matplotlib.pyplot as plt
import cv2



def main():

    ref_im = cv2.imread(r'..\test.images\pcb.1\CircuitBoard.jpg', cv2.IMREAD_GRAYSCALE)
    tst_im = cv2.imread(r'..\test.images\pcb.1\CircuitBoard-diff.png', cv2.IMREAD_GRAYSCALE)

    # diff the images
    diff = cv2.absdiff(ref_im, tst_im)

    # treshold the diff image
    treshval, bin = cv2.threshold(diff, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    #treshval, bin = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)
    #bin = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 30)
    # morpological dilate/close the tresh image
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    bin2 = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, k)

    # extract connected components
    cc, lbl, stats, centroids = cv2.connectedComponentsWithStats(bin2)

    print stats
    # draw 

    plt.figure()
    plt.subplot(121)
    plt.title('reference')
    plt.imshow(ref_im, cmap='gray')
    ax = plt.gca()
    for i, (left, top, width, height, area) in enumerate(stats):
        if i != 0:
            bottom = top + height

            left = left - 10
            bottom = bottom + 10
            width = width + 20
            height = height + 20
            top = top - 10


            r = plt.Rectangle((left,top), width, height, fill=False, edgecolor='red')
            ax.add_patch(r)
        pass

    plt.subplot(122)
    plt.title('test')
    plt.imshow(tst_im, cmap='gray')
    ax = plt.gca()
    for i, (left, top, width, height, area) in enumerate(stats):
        if i != 0:
            bottom = top + height

            left = left - 10
            bottom = bottom + 10
            width = width + 20
            height = height + 20
            top = top - 10

            r = plt.Rectangle((left,top), width, height, fill=False, edgecolor='red')
            ax.add_patch(r)
        pass

    #plt.figure()
    #plt.imshow(diff)
    #plt.figure()
    #plt.imshow(bin)
    #plt.figure()
    #plt.imshow(bin2)
    #plt.figure()
    #plt.imshow(lbl)
    plt.show()
    plt.close('all')

    return


if __name__ == '__main__':
    main()