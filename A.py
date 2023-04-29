import cv2
import numpy as np

# 读取图像
img = cv2.imread('./line2.png')

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 进行高斯模糊以去除噪声
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 进行 Canny 边缘检测
edges = cv2.Canny(blur, 50, 150, apertureSize=3)

# 进行霍夫直线变换
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# 遍历所有检测到的直线
for line in lines:
    rho, theta = line[0]
    
    # 计算直线的 x 和 y 坐标
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    
    # 计算直线的端点坐标
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    
    # 绘制直线
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    # 计算黑线与垂直线的偏移角度
    if np.pi/4 < theta < np.pi*3/4:
        offset_angle = theta - np.pi/2
    else:
        offset_angle = theta
    
    print("偏移角度：", offset_angle)

# 显示结果
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
