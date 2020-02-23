import requests
def get_html(stock_id):
    url = "https://fund.bot.com.tw/Z/ZC/ZCW/CZKC1.djbcd?a={}&b=D&c=1440".format(stock_id)
    resp_html = requests.get(url)
    html = resp_html.text
    return html

def parse_html(html):
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
    return datas

for stock_id in [2330,2317]:
    html = get_html(stock_id)
    datas = parse_html(html)
    for i in range(0,len(datas)):
        print(stock_id,datas[i])
