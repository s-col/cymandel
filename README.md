# cymandel
Python+Cythonでマンデルブロ集合を描く．

## 準備
setup.pyを実行してCythonモジュールをビルドする．

    $ python setup.py build_ext -i
    
## 使い方
#### マンデルブロ集合の表示と保存方法
マンデルブロ集合の表示と保存は`mandel.py`で行う．

`show`コマンドでマンデルブロ集合を表示する．`W`は一行当たりの分割数．

    $ python mandel.py show W

`png`コマンドでマンデルブロ集合のpngを保存する．保存先は`./mandel_png`.

    $ python mandel.py png W

`mandel.py`実行時に表示されるX0, X1, Y0, Y1の値はマンデルブロ集合を求めた座標の範囲を表しており，(X0, Y0)が左下の点の座標，(X1, Y1)が右上の点の座標である．
    
#### 範囲の変更
マンデルブロ集合を求める範囲の変更は`set_params_pixel.py`や`set_params_direct.py`で行う.

* `set_params_pixel.py`は直近に生成したマンデルブロ集合のピクセルの座標を使って範囲を指定する．

      $ python set_params_pixel.py [LEFT RIGHT BOTTOM]

  `LEFT`は左端のピクセルの列番号，`RIGHT`は右端のピクセルの列番号，`BOTTOM`は下端のピクセルの行番号を指定する．上端のピクセルの行番号(TOP)は縦横の比が1:1になるように自動的に決められる．

  引数を与えなければ初期化される．

      $ python set_params_pixel.py

`set_params_pixel.py`の具体的な使い方の例は次の通りである：  
1. `mandel.py`を実行し，マンデルブロ集合を表示させる．
2. matplotlibのGUIのズーム機能を利用して画像を拡大する．
3. matplotlibのプロットに表示される座標を見て`RIGHT`, `LEFT`, `BOTTOM`を調べる.
4. `set_params_pixel.py`を実行し範囲を変更する．

* `set_params_direct.py`は直接座標を指定して範囲を変更する．

      $ python set_params_direct.py [X0 X1 Y0]

  Y1は縦横比が1:1になるように自動的に決められる．

  引数を与えなければ初期化される．

      $ python set_params_direct.py

## 予定
範囲指定まわりがちょっと不便なので変更するかもしれない．
