import sys
import pickle
from mandel import DUMP_FILE_NAME


try:
    f = open(DUMP_FILE_NAME, 'rb')
    param_dict = pickle.load(f)
    f.close()
except FileNotFoundError:
    s = (
        '{} is not found.\n'
        'Run mandel.py once.'
    ).format(DUMP_FILE_NAME)
    print(s)
    sys.exit(1)


X0 = param_dict['X0']
X1 = param_dict['X1']
Y0 = param_dict['Y0']
Y1 = param_dict['Y1']
W = param_dict['W']

dx = (X1 - X0) / W
dy = (Y1 - Y0) / W

if len(sys.argv) == 1:
    # 引数無しならリセット
    x0 = -2.25
    x1 = 0.75
    y0 = -1.50
    y1 = 1.50
else:
    x0 = X0 + float(sys.argv[1]) * dx
    x1 = X0 + float(sys.argv[2]) * dx
    y0 = Y1 - float(sys.argv[3]) * dy
    y1 = y0 + x1 - x0


# パラメータの表示
s = '''X0 = {:12.9f}  Y0 = {:12.9f}
X1 = {:12.9f}  Y1 = {:12.9f}'''.format(x0, y0, x1, y1)
print(s)


param_dict['X0'] = x0
param_dict['X1'] = x1
param_dict['Y0'] = y0
param_dict['Y1'] = y1

with open(DUMP_FILE_NAME, 'wb') as f:
    pickle.dump(param_dict, f)
    f.close()
