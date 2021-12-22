ここではSmartDIYs Creatorにおけるレーザ加工の種類と、対応する画像フォーマットについて説明します。

## ベクタ（線）加工

<p align="center">
<img alt="SmartScreen" src="./images/processtype/vector_stroke_photo.jpg" style="width:60%">
</p>

この加工方法では、ベクタ画像のパスに沿ってレーザヘッドが移動し、加工を行うことができます。

### 特徴
- 切断加工や直線・曲線の刻印に適している加工方法です。
- この加工を行うためには、ベクタ画像（SVGやDXF）が必要です。

### データ作成方法
お持ちのドローイングソフトウェアにて任意の図形（パス）を描き、線の色を設定することでベクタ（線）加工を行うためのデータが作成できます。
また、SVGデータをソフトウェアにインポートする際、色ごと別々のアイテムに分割されます。そのため、あらかじめ線の色分けを行なっておくことで、加工順序の変更を調整できるようになります。
```
※白色の線は無視されるため、白色以外で指定してください。
```
<p align="center">
<img alt="SmartScreen" src="./images/processtype/vector_stroke.png" style="width:70%">
</p>


----------------------------------

## ベクタ（塗り）加工

<p align="center">
<img alt="SmartScreen" src="./images/processtype/vector_fill_photo.jpg" style="width:60%">
</p>

この加工方法では、パスの「塗り」を細かい平行線を引き重ねて表現します（ハッチング）。本ソフトウェアでは平行線同士の間隔やパターンを設定することができます。

### 特徴
- ロゴや文字の刻印に適している加工方法です。
- この加工を行うためには、ベクタ画像（SVG）が必要です。

### データ作成方法
お持ちのドローイングソフトウェアにて任意の図形（パス）を描き、塗りの色を設定することでベクタ（塗り）加工を行うためのデータが作成できます。<br>
また、SVGデータをソフトウェアにインポートする際、色ごと別々のアイテムに分割されます。そのため、あらかじめ線塗りの色分けを行なっておくことで、加工順序を調整できるようになります。
```
※白色の塗りは無視されるため、白色以外で指定してください。
```
<p align="center">
<img alt="SmartScreen" src="./images/processtype/vector_fill.png" style="width:70%">
</p>

```
[ご注意]
JPGやPNGなどをSVGとして保存してもベクタ画像には変換されません。
ベクタデータに変換するためには、お持ちのドローイングソフトウェアにて画像トレース等の作業が必要です。
```
----------------------------------

## ラスタ加工

<p align="center">
<img alt="SmartScreen" src="./images/processtype/raster_photo.jpg" style="width:60%">
</p>

この加工方法では、ラスタ画像にディザリング処理を行って画像の濃淡を表現します。

### 特徴
- 濃淡のあるイラストや写真の刻印に適している加工方法です。
- この加工を行うためには、ラスタ画像（JPGやPNG等）が必要です。
- レーザの強度（刻印の濃さ）ではなく、ドットの密度で濃淡を表現します。

### データ作成方法
お持ちのペイントソフトウェア等にてトリミングやコントラストの調整を行ってください。

```
※インポート時にグレースケールへ自動変換変換されます。
※インポート時に横1023ピクセルにリサイズされます。
```

<p align="center">
<img alt="SmartScreen" src="./images/processtype/raster.png" style="width:70%">
</p>


----------------------------------
## DXFデータについて

### 書き出し形式について
本ソフトウェアでは、**DXF R12・テキスト** 形式の書き出しを推奨しております。

### 寸法について
本ソフトウェアでは 1単位=1mm として読み込まれます。

### 色分けについて
DXFフォーマットはソフトウェア毎の方言が多く、お使いのソフトウェアによっては上記の形式で書き出した場合でも色を認識できない場合がございます。
その場合は、SVGとして書き出して頂くか、SVG変換を行うためのソフトウェアやオンラインサービスをご利用ください。

- [https://www.dxfconverter.org/](https://www.dxfconverter.org/)
- [https://convertio.co/ja/dxf-svg/](https://convertio.co/ja/dxf-svg/)
- [https://onlineconvertfree.com/ja/convert-format/dxf-to-svg/](https://onlineconvertfree.com/ja/convert-format/dxf-to-svg/)
