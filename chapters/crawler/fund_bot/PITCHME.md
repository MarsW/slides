@snap[midpoint slide1]
<h1>爬蟲<br>台灣銀行</h1>
@snapend

+++
@title[程式碼]
```python
import requests 
url = "____"
resp = requests.get(url)
html = resp.text
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
    print(datas[i])
```
Note:
https://fund.bot.com.tw/Z/ZC/ZCW/CZKC1.djbcd?a=2330&b=D&c=1440
