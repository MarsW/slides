import requests
def get_html(stock_id,sdate="20200201",source=""):
    if source=="fund_bot":
        url = "https://fund.bot.com.tw/Z/ZC/ZCW/CZKC1.djbcd?a={}&b=D&c=1440".format(stock_id)
    elif source=="twse":
        url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}".format(sdate,stock_id)
    else:
        return ""
    resp = requests.get(url)
    html = resp.text
    return html

def parse_fundbot(html):
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

def parse_twse_html(html):
    page = etree.HTML(html)
    datas = []
    for index,tr in enumerate(page.xpath("//tr")):
        if index>1:
            row = []
            for td_text in tr.xpath(".//td//text()"):
                text= td_text.strip().replace(",","")
                if text.count("/")==2:
                    y,m,d = text.split("/")
                    y = int(y)+1911
                    text = "{}/{}/{}".format(y,m,d)
                row.append(text)
            if row:
                datas.append([row[0],row[3],row[4],row[5],row[6],str(round(float(row[1])/1000))])
    return datas

for stock_id in [2330,2317]:
    html = get_html(stock_id,source="fund_bot")
    datas = parse_fundbot(html)
    # html = get_html(2330,source="twse")
    # datas = parse_twse_html(html)
    for i in range(0,len(datas)):
        print(stock_id,datas[i])