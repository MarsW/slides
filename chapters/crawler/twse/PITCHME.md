@snap[midpoint slide1]
<h1>爬蟲<br>台灣證交所</h1>
@snapend

+++
### HTML
```python
import requests 
from lxml import etree
url = "____"
resp_html = requests.get(url)
html = resp_html.text
page = etree.HTML(html)
    datas = []
    for tr in page.xpath("//tr"):
        row = []
        for td_text in tr.xpath(".//td//text()"):
            row.append(td_text.strip())
        if row:
            datas.append(row)
            print(row)
```
Note:
https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20200222&stockNo=2330

+++
### CSV
```python
import requests
url = "____"
resp = requests.get(url)
html = resp.text
html = html.replace("\r","")
for row in html.split("\n"):
    datas = row.split('","')
    if len(datas)==9:
        datas[0] = datas[0].replace('"','')
        datas[-1] = datas[-1].replace('"','')
        print(datas)
```
Note:
https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=20200222&stockNo=2330

