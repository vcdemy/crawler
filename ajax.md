# 傳統網頁 vs ajax

傳統的網頁的做法，大致上是把資料都彙整到.html檔案上面，所以只要將網頁原始碼抓回來，在進一步剖析網頁原始碼，就會得到資料。

Ajax是Asynchronous Javascript and XML的縮寫。 他會使用非同步傳輸的方式，將資料填到網頁上面去。意思是說，網頁伺服器會先傳個網頁的框架給使用者，在利用非同步傳輸的方式將資料填到網頁上面去。Ajax的做法會稍微提升爬取網頁資料的難度。

可以比較一下下面兩個網址的內容，思考一下傳統網頁跟Ajax的差異：

* [傳統網頁](https://vcdemy.github.io/web/spy.html)
* [Ajax網頁](https://vcdemy.github.io/web/spy_ajax.html)

在上面的Ajax網頁中，可以嘗試Disable Javascript看看網頁有什麼差別！

## Disabling Javascript

方法一：

* 在 Chrome Browser 的網址列輸入：`chrome://settings/content/javascript`
* 再選擇關掉Javascript

方法二：

* 點擊右上角的三個點圖標，選擇「設定」。
* 向下滾動並點擊「隱私權與安全性」。
* 選擇「網站設定」。
* 在「內容」部分中，點擊「JavaScript」。
* 切換JavaScript的開關至「關閉」狀態。

方法三：

* 打開 Chrome DevTools
* 點擊右上角的設定按鈕
* 從Debugger那個Section中，選擇Disable Javascript