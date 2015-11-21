import numpy as np
import matplotlib.pyplot as plt
import cv2



def main():

    image_type = cv2.IMREAD_COLOR

    ref_im = cv2.imread(r'..\test.images\pcb.1\CircuitBoard.jpg', image_type)
    tst_im = cv2.imread(r'..\test.images\pcb.1\CircuitBoard-diff.png', image_type)
    tst_im = cv2.imread(r'..\test.images\pcb.1\CircuitBoard-diff-light.png', image_type)

    h, w = ref_im.shape[:2]

    diff = np.zeros((h,w), dtype=np.float32)

    b = 12

    for i in range(0, h-b, b):
        for j in range(0, w-b, b):

            ref_roi = ref_im[i:i+b, j:j+b]
            tst_roi = tst_im[i:i+b, j:j+b]
            diff_roi = diff[i:i+b, j:j+b]

            score = cv2.matchTemplate(tst_roi, ref_roi, cv2.TM_CCOEFF_NORMED)

            score = 1.0 - float(score)

            diff_roi.fill(score)



    plt.imshow(diff)


    # apply max filter (dilate)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (b,b))
    diff2 = cv2.morphologyEx(diff, cv2.MORPH_DILATE, k)
    diff2 = np.uint8(diff2 * 255.0)
    plt.figure()
    plt.subplot(121)
    plt.imshow(diff)
    plt.subplot(122)
    plt.imshow(diff2)




    # treshold the diff image
    treshval, bin = cv2.threshold(diff2, 0.0, 255.0,  cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #treshval, bin = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)
    #bin = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 30)
    # morpological dilate/close the tresh image

    bin = np.uint8(bin)

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

    plt.figure()
    plt.imshow(diff)
    plt.figure()
    plt.imshow(bin)
    plt.figure()
    plt.imshow(bin2)
    plt.figure()
    plt.imshow(lbl)
    plt.show()
    plt.close('all')



    return


if __name__ == '__main__':
    main()