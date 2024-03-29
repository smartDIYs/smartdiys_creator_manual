ここでは、ユーザ設定の「補正」項目について説明します。
この補正項目は下記の現象を改善するために有効な調整値です。

- 加工物の寸法がデータと異なる
- X軸とY軸が直角ではない

## 加工物の寸法がデータと異なる

### 主な原因
1. 光軸調整が適切ではない
2. プーリーやタイミングベルトなどの調整が適切ではない

上記の調整を行なっても改善しきれない場合は、大きさ補正の項目を設定して頂くことで改善が期待できます。

### 補正値の算出方法

1. 任意の幅・高さの矩形の加工データを用意します。
2. シワや歪みが生じにくい素材に刻印加工を行います。
3. データのサイズと刻印加工のサイズから比率を算出します。

#### [算出例]
データのサイズ: H:200.00mm x W:200.00mm<br/>
実際の加工サイズ: H:199.10mm x W:199.50mm

[Hの補正値]

```
求め方: （データ）200.00 / （実際）199.10 = 1.00452034...
設定値: 100.45203(%)
```

[Wの補正値]

```
求め方: （データ）200.00 / （実際）199.50 = 1.00250626...
設定値: 100.25063(%)
```

## ハッチングやラスタ加工時に左右の輪郭がブレる
### 主な原因

1. X軸のプーリーやタイミングベルトなどの調整が適切ではない。
2. 素材に対するレーザーのパワーが低い。

上記の調整を行なっても改善しきれない場合は、スキャン補正の項目を設定して頂くことで改善が期待できます。

### 補正値の算出方法

1. 任意の幅・高さの矩形のベクタ塗り加工データを用意します。
2. シワや歪みが生じにくい素材に刻印加工を行います。任意のスピードで、ハッチングは0.5〜1mm程度に設定します。
3. 段差の距離(D)を計測し、その値の半分の値を設定します。スピードは加工時のスピードを入力します。

<p align="center">
<img alt="SmartScreen" src="./images/correction/scan_correction.png" style="width:70%">
</p>

#### [算出例]
```
加工時のスピード: 6000mm/min
ズレ幅: 0.3mm
求め方: 0.3 / 2 = 0.15
設定値値: 6000 | 0.15
```
※任意のスピードに対し任意の補正値を設定できます。設定値間の数値は補完されます。<br/>
※X方向の補正のみサポートしています。

## 直角のデータが正確ではない

### 主な原因

原因:
1. 光軸調整が適切ではない
2. フレームやX軸の組み立て時に傾きが生じている

上記の調整を行なっても改善しきれない場合は、傾き補正の項目を調整して頂くことで改善が期待できます。

### 補正値の算出方法

まず、上記の「大きさ補正」を済ませておくと、より正確に補正値が算出できます。

1. 任意の幅・高さの矩形の加工データを用意します。
2. シワのない紙などの素材を切断加工します。
3. 左下角と左上角が重なるように折り重ねます。
4. 右下角と右上角の重なりにズレがある場合、このズレの距離（L）を測ります。
5. 下記の公式に当てはめて、角度を算出します。<br/>
`θ (deg) = arcsin ( (L/2) / W ) * 180 / π`

<p align="center">
<img alt="SmartScreen" src="./images/correction/x-axis-angle.png" style="width:70%">
</p>

#### [算出例]

データのサイズ: H:280.00mm x W:400.00mm<br/>
折り重ねた際の右下角と右上角のズレ: L: 1.50mm

[角度の補正値]

```
求め方: arcsin( 0.75 / 400.00 ) * 180 / π
設定値:
右上がりを補正する場合: -0.10743°
右下がりを補正する場合: +0.10743°
```
