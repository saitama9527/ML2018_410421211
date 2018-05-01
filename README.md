##### 機器學習導論 HW1 #

利用梯度下降法解密圖片

--------------------------

1. 使用PIL讀取圖片
2. 將圖片轉成2維陣列
3. 設定初始weight 1維陣列
4. 在限制的epoch內，使用梯度下降法利用已解密的圖片進行training
-----Training的參數: Learn rate = 0.00001 , Max epoch = 10-----
5. 計算出weight後，反推出解密後圖片的陣列
6. 用np.uint8轉為整數後，輸出成圖片(png)


### weight #
Weight vector w = [0.24914331 , 0.6613819 , 0.08923953]

#### 以下為解密前與解密後 

##### 解密前 #
![Alt text](https://imgur.com/1nEVhKv.png)

##### 解密後 #
![Alt text](https://imgur.com/PxkqGcv.png)

#### 遇到的問題 #
公式內矩陣轉置又轉置，寫的時候很容易搞混，爾且numpy轉置一維矩陣又有些麻煩，花了很多時間才弄懂。再來就是在反推圖片陣列的時候都是浮點數，而在轉整數時因為uint8的設定只能0~255，所以有些四捨五入後變成256的就被轉成0，導致圖片出現很多黑點，最後用一個判斷式調整數值避免爆表。

#### 學到了 #
Github基本功能，python對圖片簡單的處理，梯度下降法實作時用的演算法，一些numpy的功能

--------------------------
