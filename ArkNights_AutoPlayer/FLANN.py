# 基于FLANN的匹配器(FLANN based Matcher)定位图片
import numpy as np
from PIL import Image,ImageGrab
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 12  # 设置最低特征点匹配数量为12

# Initiate SIFT detector创建sift检测器
sift = cv2.xfeatures2d.SIFT_create()

def FLANN_match(template_path):

    # 生成对象
    # template_path = 'end_part3.jpg'  # queryImage(小图)
    # target_path = 'end.png'  # trainImage(大图)
    template = cv2.imread(template_path, 0)
    #ImageGrab截图，并且转换为cv2
    img = ImageGrab.grab()
    target = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)


    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(template, None)
    kp2, des2 = sift.detectAndCompute(target, None)

    # 创建设置FLANN匹配
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []

    # 舍弃大于0.7的匹配
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)
    if len(good) > MIN_MATCH_COUNT:

        # 获取关键点的坐标
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        # 获取目标图的中心点
        dst_xy = dst_pts.tolist()
        dst_x = []
        dst_y = []
        for i in dst_xy:
            dst_x.append(i[0][0])
            dst_y.append(i[0][1])

        dst_x_mean = np.median(dst_x)
        dst_y_mean = np.median(dst_y)
        print("( %d , %d )" % (dst_x_mean, dst_y_mean))

        # # 计算变换矩阵和MASK
        # M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        # matchesMask = mask.ravel().tolist()
        # h, w = template.shape
        #
        # # 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标
        # pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        # dst = cv2.perspectiveTransform(pts, M)
        # cv2.polylines(target, [np.int32(dst)], True, 0, 2, cv2.LINE_AA)
        return dst_x_mean, dst_y_mean

    else:
        print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
        matchesMask = None
        return 0,0
    # draw_params = dict(matchColor=(0, 255, 0),
    #                    singlePointColor=None,
    #                    matchesMask=matchesMask,
    #                    flags=2)
    # result = cv2.drawMatches(template, kp1, target, kp2, good, None, **draw_params)
    # plt.imshow(result, 'gray')
    # plt.show()
