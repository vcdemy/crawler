# 網路爬蟲簡介

## 關於唯客學院

* [唯客學院網址](http://www.vcdemy.com)
* [唯客學院粉絲專頁](https://www.facebook.com/vcdemy/)
* [唯客學院線上課程](https://khpy.teachable.com)

## 課程內容

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vcdemy/crawler/)

簡單介紹 requests, beautifulsoup跟selenium的使用。

### 投影片及相關連結

* [Web簡介 - 投影片](https://docs.google.com/presentation/d/1UEPMx0G-MYWW2gHZs0Y93L6XwVVg5S5I0QLVsv4A0y4/edit?usp=sharing)
* [爬蟲簡介 - 投影片](https://docs.google.com/presentation/d/1-ydjrfvmsSnn2COglvybabIp5edGubZ8g8Ahh2xDv9k/edit?usp=sharing)
* [爬蟲練習網站](https://victorgau.github.io/khpy_web_intro/)

### 1. 文件導覽

* [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/)
* [Beautiful Soup 4.2.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)
* [Selenium with Python](https://selenium-python.readthedocs.io/)
* [Web Drivers](https://selenium-python.readthedocs.io/installation.html#drivers)
* [Selenium IDE](https://www.selenium.dev/selenium-ide/)
* [Katalon](https://www.katalon.com/)

#### 套件及模組說明

|模組, 套件|說明|
|:--|:--|
|requests|很多人用來做HTTP request的套件。|
|BeautifulSoup|很多人用來做HTML原始碼剖析的套件。|
|Selenium|很多人用來做自動化網頁測試的套件。|
|json|用來做json文件剖析的內建模組。|
|csv|用來讀寫csv文件的內建模組。|

|工具|說明|
|:--|:--|
|Selenium IDE|可以錄製使用者的操作，再轉換成Python程式的工具。|
|Katalon|Katalon也可以錄製使用者的操作，再轉換成Python程式。之前，Selenium IDE曾經移除export to python code的功能，如果再發生，可以再改用Katalon來錄製使用者的操作。|
|Chrome DevTools|可以用來檢視本地端跟伺服器端的資料傳輸的開發者工具。|

### 2. 實作引導

* requests 使用簡介
  * 使用 requests 抓取網頁原始檔。
  * 使用 requests 抓取圖片。
  * 使用 requests 抓取pdf檔。
  * 使用 requests 抓取json檔，並剖析json檔。
  * 使用 reqeusts 抓取csv檔，並剖析csv檔。
* BeautifulSoup 使用簡介
  * 使用 BeautifulSoup 剖析HTML檔 (網頁原始檔)。
  * 使用 BeautifulSoup 剖析XML檔。
  * 說明在 BeautifulSoup 裡面如何使用 CSS Selector 來選取標籤。
* Chrome DevTools 的使用簡介。
* Selenium 使用簡介。

### 3. 自我挑戰

* 讀取政府資料開放平台資料
* 讀取Ubike腳踏車資訊
* 讀取高雄市政府公車資訊
* 讀取高雄市政府停車場資訊
* 讀取新聞本文
* 讀取新聞標題
* 讀取圖片
* 讀取pdf檔

#### 套件安裝：

* 安裝 requests

```
pip install requests
```

* 安裝 beautifulsoup4

```
pip install beautifulsoup4
```
