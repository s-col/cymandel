cimport cython
from tqdm import tqdm
import numpy as np


DTYPE = np.uint8


cdef void csquare(double s[], double x, double y):
    s[0] = x*x - y*y
    s[1] = 2.0 * x * y


cdef int calc(double cx, double cy, int inf, double lim):
    # 計算の心臓部
    cdef double x = 0.0
    cdef double y = 0.0
    cdef int n = 0
    cdef double s[2]
    while n < inf and x*x + y*y < lim:
        csquare(s, x, y)
        x = s[0] + cx
        y = s[1] + cy
        n = n + 1
    return n


cdef void hsv2bgr(unsigned char clr_lst[], double h, double s, double v):
    cdef double b, g, r
    cdef int hi = <int>(h / 60) % 6
    cdef double f = h / 60 - hi
    cdef double p = v * (1.0 - s)
    cdef double q = v * (1.0 - f * s)
    cdef double t = v * (1.0 - (1.0 - f) * s)
    if hi == 0:
        b = p
        g = t
        r = v
    elif hi == 1:
        b = p
        g = v
        r = q
    elif hi == 2:
        b = t
        g = v
        r = p
    elif hi == 3:
        b = v
        g = q
        r = p
    elif hi == 4:
        b = v
        g = p
        r = t
    elif hi == 5:
        b = q
        g = p
        r = v

    clr_lst[0] = <unsigned char>(b * 255.0)
    clr_lst[1] = <unsigned char>(g * 255.0)
    clr_lst[2] = <unsigned char>(r * 255.0)


@cython.boundscheck(False)
@cython.wraparound(False)
def get_mandel_array(
        double x0, double x1, double y0, double y1,
        int w, int inf, double lim):

    cdef double dx = (x1 - x0) / w
    cdef double dy = (y1 - y0) / w
    cdef double cx = x0
    cdef double cy = y1
    cdef int x_fig, y_fig
    cdef int h
    cdef unsigned char clr_lst[3]

    img_np = np.zeros((w, w, 3), dtype=DTYPE)
    cdef unsigned char[:, :, ::1] img = img_np

    pbar = tqdm(total=w)

    for x_fig in range(w):
        for y_fig in range(w):
            h = calc(cx, cy, inf, lim)
            if h == inf:
                clr_lst[0] = clr_lst[1] = clr_lst[2] = 0
            else:
                hsv2bgr(clr_lst, <double>h*3, 1.0, 1.0)

            img[x_fig, y_fig, 0] = clr_lst[2]
            img[x_fig, y_fig, 1] = clr_lst[1]
            img[x_fig, y_fig, 2] = clr_lst[0]
            # 見た目の都合上, 赤と青を入れ替えている

            cx += dx

        cx = x0
        cy -= dy
        pbar.update(1)
    pbar.close()
    return img_np
