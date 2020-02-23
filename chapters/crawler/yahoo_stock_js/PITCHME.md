@snap[midpoint slide1]
<h1>爬蟲<br>yahoo!股市<br>每日技術分析</h1>
@snapend

+++
### 找出拿到資料的網址
會發覺技術分析的每日資料，並不存在原始碼中，  
因此我們使用 Chrome 開發人員工具的「Network」，  
來找出是哪個網址才有我們想要的資訊：  
- 開啟「Network」後先按"清除圖示"=>重整網頁=>按下"搜尋圖示"  
- Headers > General > Request URL 就是我們需要的網址
- Preview 可以了解資料內容
![yahoo_2330_js_url](assets/img/yahoo_2330_js_url.png)

+++
### 獲取網頁
``` python 
import requests
url = "https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=d&mkt=10&sym=2330&v=1"
response = requests.get(url)
html = response.text
print(html)
```
可以試著換換看網址參數(type, perd, mkt, sym, v)後面的參數值：
![yahoo_2330_js_url_parm](assets/img/yahoo_2330_js_url_parm.png)

+++
### 解析網頁
會發覺資料很像 Python 的字典、串列，  
代表可以用 json 模組解析。  
但只是很像，不完全就是，因此還是需要做一些前處理：
```python
import json
data = html.split("null(")[-1].split(");")[0]
json_data = json.loads(data)
print(json_data["mkt"],json_data["id"])
```
@[1](宣告使用 json 模組)
@[2](取出 null（...）; 中的資料，並用 data 物件指向解析結果)
@[3](將 data 以 json 方式解析)
@[4](就可以用字典、串列的方式取值)

+++
#### 練習
用 迴圈 針對剛才拿到的資料，  
取得每日日期、開盤價、最高價、最低價、收盤價、成交量

``` python
for row in json_data["___"]:
    print(row)
```

Note:

``` python
for row in json_data["ta"]:
    print(row)
```


