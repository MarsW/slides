@snap[midpoint slide1]
<h1>金融爬蟲</h1>
@ul[](false)
- @size[80%]yahoo!股市-即時成交明細(HTML)
- @size[80%]爬蟲與網頁相關背景知識介紹
- @size[80%]yahoo!股市-每日技術分析(JS)
- @size[80%]資料的正確性
- @size[80%]台灣銀行、台灣證交所
- @size[80%]函式
- @size[80%]總結
@ulend
@snapend

---?include=chapters/crawler/yahoo_stock_html/PITCHME.md

---?include=chapters/crawler/knowledge/req_resp/PITCHME.md

---?include=chapters/crawler/yahoo_stock_js/PITCHME.md
---
@title[資料正確性]
但怎麼確定 yahoo!股市 的資料是對的呢？  
找了[台灣銀行的股市資訊網](https://fund.bot.com.tw/z/index.htm)，比對了一下：  
發覺交易量不一致！
![yahoo_fundbot](assets/img/yahoo_fundbot.png)
+++
@title[中央資料比對]
就直接找最中央的[台灣證券交易所(台灣證交所)](https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html)：
![yahoo_fundbot_twse](assets/img/yahoo_fundbot_twse.png)
+++
@title[小結]
看起來是台灣銀行的資料跟中央是一致的，  
為了確保資料的正確性，台灣銀行是可用名單，  
那大家應該會問說，那為什麼不直接爬 台灣證交所呢？  

因為根據以前的經驗，台灣證交所超過一定數量的爬取  
eg. 當日收盤後直接爬所有股票，就會阻擋該程式爬取一段時間。  
個人習慣會選擇比較穩定的網頁爬取，所以會選擇台灣銀行，  
但因為台灣銀行是給最近一定天數的數量，  
而台灣證交所有該公司上櫃以來的資料，  
所以如果還是會用台灣證交所來補齊過往資料。  
  
透過前面「yahoo!股市-每日技術分析」的技巧，  
可以找到 台灣銀行資料、台灣證交所的 HTML 或 CSV 的網址，  
而不同網站回傳的資料，都有不同的格式，這也就是需要更近一步開發程式的地方。  


---?include=chapters/crawler/fund_bot/PITCHME.md

---?include=chapters/crawler/twse/PITCHME.md

---
@title[寫得更彈性優雅]
雖然前面我們已經會基本的爬蟲：
1. 找出拿到資料的網址
2. 獲取該網址中的資料
3. 解析出想要的資訊：Python 內建模組語法、配合 XPath 
4. 決定儲存方式  

都是直接以一支程式運行到底，  
但若遇到網路不穩定或像台灣證交所這種可能不定時會阻擋爬蟲，  
更好的做法是將以上這些步驟拆成各自獨立的運作模式，    
這樣可以針對沒有成功執行完畢的地方重新執行，  
而不需要所有部分都重新執行。

---?include=chapters/basic/statement/function/PITCHME.md
---
@snap[midpoint slide1]
<h1>一步步把程式以函式改寫</h1>
@snapend
+++
@title[改寫]
以 台灣銀行的爬蟲為例，現在有兩隻股票 2330, 2317 要解析：

```python
import requests 
for stock_id in [2330,2317]:
    url = "https://fund.bot.com.tw/Z/ZC/ZCW/CZKC1.djbcd?a={}&b=D&c=1440".format(stock_id)
    resp_html = requests.get(url)
    html = resp_html.text
    group = html.split(" ")
    g_date,g_open,g_high,g_low,g_close,g_volume = group[0:5+1]
    g_date = g_date.split(",")
    g_open = g_open.split(",")
    g_high = g_high.split(",")
    g_low = g_low.split(",")
    g_close = g_close.split(",")
    g_volume = g_volume.split(",")
    datas = []
    for i in range(0,len(g_date)):
        datas.append([g_date[i],g_open[i],g_high[i],g_low[i],g_close[i],g_volume[i]])
        print(stock_id,datas[i])
```
+++
@title[改寫-獲取該網址中的資料]

```python
import requests 
for stock_id in [2330,2317]:
    url = "https://fund.bot.com.tw/Z/ZC/ZCW/CZKC1.djbcd?a={}&b=D&c=1440".format(stock_id)
    resp_html = requests.get(url)
    html = resp_html.text
    group = html.split(" ")
    ......
```
<center>⇩</center>
```python
import requests 
def get_html(stock_id):
    url = "https://fund.bot.com.tw/Z/ZC/ZCW/CZKC1.djbcd?a={}&b=D&c=1440".format(stock_id)
    resp_html = requests.get(url)
    return resp_html.text

for stock_id in [2330,2317]:
    html = get_html(stock_id)
    group = html.split(" ")
    ......
```

+++
### 練習：改寫-解析出想要的資訊 

```python 
def parse_html(____):
    ____
    return ____
for stock_id in [2330,2317]:
    html = get_html(stock_id)
    datas = parse_html(____)
    for i in range(0,len(datas)):
        print(stock_id,datas[i])
```

Note:
[解答](codes/function_fund_bot.py)
+++
@title[爬蟲合併]
如果把台灣銀行、台灣證交所的爬蟲合併，就會如同 codes/function_finance.py  
函式的好處：除了更容易閱讀，要除錯(debug)、優化也容易針對部分程式碼，不怕改錯地方，例如如果我擔心網路不穩定，想先把爬蟲獲取各網址中的資料留存下來，之後再進行解析就可以做以下的改寫。

```python 
def get_html(stock_id,sdate="20200201",source=""):
    ...
    改存成檔案，不return

def parse_fundbot(stock_id):
    改從讀檔處理
    ...
    return datas
for stock_id in [2330,2317]:
    if stock_id.txt 存在此資料夾中:
        parse_XXX(stock_id)
    else:
        get_html(stock_id,source="XXX")
        parse_XXX(stock_id)
    for i in range(0,len(datas)):
        print(stock_id,datas[i])
```
+++
@title[爬蟲合併-語法傳送門]
#### 傳送門
- [檔案讀寫](https://marsw.github.io/Python-Tutorial/07_v2_applications.slides.html#/4)
- [檔案總管操作](https://marsw.github.io/Python-Tutorial/07_v2_applications.slides.html#/5)

---
@snap[midpoint slide1]
<h1>總結</h1>
@snapend

+++
### 爬蟲過程
1. (觀察)找出拿到資料的網址：換換看參數
2. (程式)獲取該網址中的資料：`requests`
3. (程式/觀察)解析出想要的資訊：Python 內建、XPath 
4. (自訂)決定儲存方式
5. (程式)更快速穩定彈性的重複以上步驟：函式

+++
### 爬蟲觀念
- 若資料有多個來源，可以多方比對，確保爬取的來源資訊正確
- 如果對方網站會有阻擋的行為，代表不希望爬蟲影響網站運作，可以配合 `time.sleep()`，不太過頻繁抓取
```python
import time
time.sleep(程式休息秒數)
```
---
### Appendix
- [Python 入門](https://tw.pyladies.com/events/topic.html?id=36)
- [Python 入門(週末密集充實版)](https://tw.pyladies.com/events/topic.html?id=46)
- [進階爬蟲](https://tw.pyladies.com/events/topic.html?id=25)


