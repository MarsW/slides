@snap[midpoint slide1]
<h1>爬蟲<br>yahoo!股市<br>即時成交明細</h1>
@snapend

+++
### 獲取網頁
``` python 
import requests
url = "https://tw.stock.yahoo.com/q/ts?s=2330"
response = requests.get(url)
html = response.text
print(html)
```

@[1](宣告使用 requests 模組)
@[2](url 物件指向我們想要爬的網址)
@[3](使用 requests 模組的 get 工具)
@[3](將爬取的結果以物件 reposnse 指向)
@[4](將爬取的結果內文文字的部分，以物件 html 指向)
@[5](印出 html 物件)

+++
@title[檢查獲取結果]
先找一下有沒有 [yahoo!股市-台積電](https://tw.stock.yahoo.com/q/ts?s=2330)「成交明細」的數字
![yahoo_2330](assets/img/yahoo_2330.png)

+++
### 使用 Chrome 開發人員工具
右鍵點選網頁我們想取的資料位置，選擇「檢查」，  
就可以利用 Chrome 的 「開發人員工具」- Elements，  
找出我們想抓的資料在網頁結構中的哪個位置
![yahoo_2330_xpath1](assets/img/yahoo_2330_xpath1.png)
+++
### Copy XPath
利用 Chrome 的 「開發人員工具」，  
可利用 Copy XPath，把對應反白區塊資料的 XPath 路徑複製下來
![yahoo_2330_xpath1_copy](assets/img/yahoo_2330_xpath1_copy.png)
+++

### 檢查 XPath 
利用 Chrome 的 套件 - [XPath Helper](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl?hl=zh-TW)，  
檢查 XPath 是否真的能抓到資料
![yahoo_2330_xpath1_xpaht_helper](assets/img/yahoo_2330_xpath1_xpaht_helper.png)

+++ 
### 使用 Chrome 觀察注意事項
Elements 是「輔助」我們觀察經 Chrome 排版過的原始碼架構，  
但 Chrome 因為有多加工，我們真實抓到的資料不一定是長這樣！  
XPath Helper 也是檢查 Chrome 加工後的資訊，所以僅能當輔助，  
要看原始碼才是最準的！(右鍵>檢視原始碼)  

+++
### Python 解析 XPath

```python
from lxml import etree
page = etree.HTML(html)
xpath_1 = "//html/body/center/table[1]/tbody/tr/td[1]/table[2]//text()"
xpath_2 = "//table[@border=0 and @width=700][1]//td//text()"
result = page.xpath(xpath_1)
for row in result:
    print(row)
```
@[1](宣告僅使用 lxml 模組的 etree 工具)
@[2](用 etree 將我們爬到的網頁 html 以 HTML 方式解析成「XPath的節點 node 型態」)
@[2](並用 page 物件指向解析結果)
@[3](使用  Chrome 的 「開發人員工具」建議的 XPath)
@[4](以觀察特性歸納的 XPath)
@[5](符合規則的所有資料以物件 result 指向)
@[6,7](在這 XPath 中，符合規則的所有資料以迴圈印出)

+++
#### 練習
用 迴圈 配合 `enumerate` 或是 `range`，加上判斷式：
- 過濾掉標題
- 僅拿取時間
- 拿取時間以及該時間對應的各種數字以串列方式存起來

``` python
from lxml import etree
page = etree.HTML(html)
xpath_1 = "//html/body/center/table[1]/tbody/tr/td[1]/table[2]//text()"
xpath_2 = "//table[@border=0 and @width=700][1]//td//text()"
result = page.xpath(xpath_2)
## result_list = []
for index,row in enumerate(result)):
    if index>=___: # and index%___==___:
        print(index,row)
        ## row_list = result[index:index+___]
        ## print(index,row_list)
        ## result_list.append(row_list)
## print(result_list)
```


Note:

``` python
from lxml import etree
page = etree.HTML(html)
xpath_1 = "//html/body/center/table[1]/tbody/tr/td[1]/table[2]//text()"
xpath_2 = "//table[@border=0 and @width=700][1]//td//text()"
result = page.xpath(xpath_2)
result_list = []
for index,row in enumerate(result)):
    if index>=9 and index%6==3:
        print(index,row)
        row_list = result[index:index+6]
        print(index,row_list)
        result_list.append(row_list)
print(result_list)
```


