@snap[midpoint slide1]
<h1>Request & Response</h1>
@snapend
+++
@title[在瀏覽器輸入網址]
@snap[north span-70]
![req_resp_01](assets/img/req_resp/req_resp.001.jpeg)
@snapend
@snap[south span-90]
當我們在手機、電腦(client)  
開啟 瀏覽器(browser)，輸入 網址(url)，  
瀏覽器就會去跟那個網址對應  位置(IP)  
的 伺服器(server) 發送需求(request)
@snapend

+++
@title[瀏覽器詢問伺服器]
@snap[north span-70]
![req_resp_02](assets/img/req_resp/req_resp.002.jpeg)
@snapend
@snap[south span-90]
如果伺服器還活著，就會回傳(response)  
瀏覽器相對的資訊，通常是網頁樣貌。
@snapend

+++
@title[瀏覽器獲得回傳資訊]
@snap[north span-70]
![req_resp_03](assets/img/req_resp/req_resp.003.jpeg)
@snapend
@snap[south span-90]
而網頁樣貌只是一長串人類看不懂的  
原始碼(HTML)，原始碼通常除了文字，  
還會包含著網頁需要哪些素材(圖像影音)、  
該怎麼排版(CSS)、有哪些互動效果(JS)...。
@snapend

+++
@title[瀏覽器再多次發送需求]
@snap[north span-70]
![req_resp_04](assets/img/req_resp/req_resp.004.jpeg)
@snapend
@snap[south span-90]
這些素材瀏覽器  
也會一一再向伺服器發送需求
@snapend
+++
@title[瀏覽器組合成畫面]
@snap[north span-70]
![req_resp_05](assets/img/req_resp/req_resp.005.jpeg)
@snapend
@snap[south span-90]
最後，  
瀏覽器會把從伺服器回傳的原始碼&素材，  
組合成我們看到的畫面。
@snapend

+++
@title[Chrome 開發人員工具觀察]
@snap[north span-70]
![req_resp_05](assets/img/req_resp/req_resp.png)
@snapend
@snap[south span-90]
從 Chrome 開發人員工具 也可以看到，  
每個元素(原始碼, 素材...)   
都是一個需求(request)，  
而每次我們使用 `requests.get(url)`，  
就是發送一個需求
@snapend

+++
### 小結
- 每個原始碼、圖片... 都是分別獨立的需求跟伺服器拿取  
- 可以先透過 Chrome 開發人員工具 找尋真正需要的素材，  
  再發送 request
- 或先以網址發送 request，獲得 response 網頁樣貌，可以得知有哪些素材如果有需要再一一對素材向伺服器發送 request   
(eg. 抓取網頁的所有圖像影音)

+++
### Appendix
- [Request Method](https://tw.pyladies.com/~marsw/crawler03.slides.html#/1/3)：`GET`, `POST`
- [Cookie](https://tw.pyladies.com/~marsw/crawler03.slides.html#/2)



