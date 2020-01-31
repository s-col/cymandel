import cv2
import sys
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

try:
    # 拡張モジュールのインポート
    from c_mandel import get_mandel_array
except ModuleNotFoundError as e:
    print(e)
    s = (
        'Run the following command:\n'
        '   \"python setup.py build_ext -i\"'
    )
    print(s)
    sys.exit(1)


DUMP_FILE_NAME = 'param_dict.pickle'    # パラメータを保存するファイル


if __name__ == '__main__':
    W = int(sys.argv[2])    # 分割数
    LIMIT = 4.0             # 計算停止閾値
    INF = 300               # 繰り返し上限

    try:
        f = open(DUMP_FILE_NAME, 'rb')
        param_dict = pickle.load(f)
        X0 = param_dict['X0']   # xの最小値
        X1 = param_dict['X1']   # xの最大値
        Y0 = param_dict['Y0']   # yの最小値
        Y1 = param_dict['Y1']   # yの最大値
        f.close()
    except FileNotFoundError:
        param_dict = {}
        X0 = param_dict['X0'] = -2.25
        X1 = param_dict['X1'] = 0.75
        Y0 = param_dict['Y0'] = -1.50
        Y1 = param_dict['Y1'] = 1.50

    with open(DUMP_FILE_NAME, 'wb') as f:
        param_dict['W'] = W
        pickle.dump(param_dict, f)
        f.close()

    # パラメータの表示
    s = (
        'X0 = {:12.9f}  Y0 = {:12.9f}\n'
        'X1 = {:12.9f}  Y1 = {:12.9f}'
    ).format(X0, Y0, X1, Y1)
    print(s)

    # get_mandel_array -> np.ndarray
    img = get_mandel_array(X0, X1, Y0, Y1, W, INF, LIMIT)

    if sys.argv[1] == 'png':
        dt = datetime.now().strftime('%y%m%d%H%M%S')
        file_dir = './mandel_img'
        filename = file_dir + '/mandelbrot_{}.png'.format(dt)
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        cv2.imwrite(filename, img)
        print(filename)
    elif sys.argv[1] == 'show':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.show()
