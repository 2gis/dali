import numpy
import cv


def diff(img1, img2, result):
    im1 = cv.LoadImage(img1, 1)
    im2 = cv.LoadImage(img2, 1)

    mat1 = cv.GetMat(im1)
    mat2 = cv.GetMat(im2)

    a = numpy.asarray(mat1)

    diff = cv.CloneMat(mat1)
    cv.AbsDiff(mat1, mat2, diff)

    c = numpy.asarray(diff)

    difference = c.sum(axis=2)
    differenceNonZeroes = difference.nonzero()
    res = float(differenceNonZeroes[0].size) / difference.size * 100

    diffNonZeroes = c.nonzero()
    positions = []
    for pos in range(len(diffNonZeroes[0])):
        for dim in range(len(diffNonZeroes)):
            positions.append(diffNonZeroes[dim][pos])
        a[positions[0]][positions[1]] = [0, 0, 255]
        positions = []

    cv.SaveImage(result, cv.fromarray(a))

    return res
