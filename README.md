# pythonCalculatorBot

## Python 作業

###### Author : 00957125 簡蔚驊 [jimmyhealer](github.com/jimmyhealer) 00957009 鄧暐宣 [jteng2127](github.com/jteng2127)

## 功能

使用者可以用語音輸入多個矩形的座標資訊及顏色，並計算所有矩形的覆蓋面積，最後會顯示矩形覆蓋的情況。

## 使用方式

電腦會依序詢問每個矩形左下角跟右上角的座標和顏色，使用者說沒有矩形後，算出總覆蓋面積及各顏色覆蓋面積比例。

## 技術

- speechRecognition
- 圖像顯示
- 對話管理

### speechRecognition

我們是使用 Google 的服務作為語音辨識

### 圖像顯示

我們利用Python的Matplotlib、shapely、geopandas套件，來顯示矩形覆蓋的圖像。

### 對話管理

我們使用物件導向實作，並將對話內容實體化，增加後續開發效率及易讀性。

![](https://i.imgur.com/YpeylQo.png)

## DEMO

![](https://i.imgur.com/vEhZ3ck.png)

## dependency

[安裝geopandas](https://stackoverflow.com/questions/56958421/pip-install-geopandas-on-windows/60936148)
