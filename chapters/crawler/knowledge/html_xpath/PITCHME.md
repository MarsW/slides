@snap[midpoint slide1]
<h1>HTML & XPath</h1>
@snapend

+++
### HTML(Hyper Text Markup Language)
- 右鍵 > 檢視網頁原始碼
- 是用來描述網頁的一種標記語言 (markup language)
- 由一堆標記標籤(markup tag)所構成

+++
#### 常見標籤(tag)
- 連結：`<a href="網址">連結文字</a>`
- 圖片：`<img src=“圖片網址“/>`
- 內文標題：`<h1>`~`<h6>`
- 換行：`<br>`
- 表格：整張表格`<table>`, 列`<tr>`, 欄`<td>`

+++
### [範例網頁](http://tw.pyladies.com/~marsw/sample.html)

```html
<html>
    <head>
        <title>Title</title>
    </head>
    <body>
        <h1>Subtitle</h1>
        <a href="http://tw.pyladies.com/">PyLadies Website</a>
        <p>
            This is a paragraph <br>
            <a href="http://www.meetup.com/PyLadiesTW/">PyLadies Meetup</a> <br>
            <a href="https://www.facebook.com/pyladies.tw">PyLadies FB</a> <br>
        </p>
        <img src="https://tw.pyladies.com/images/logos/twgirl_logo.png" width="99px"/>
    </body>
</html>
```
@[6](內文標題`<h1>` )
@[7,10,11](連結`<a>`)
@[13](圖片`<img>` )

+++
### Nodes
- 小孩`/`：下一層節點，或是該標籤的「屬性 @」或「文字 text()」
- 子孫`//`：全搜索的意思，常用在搜尋不知道有幾層節點的狀況
    - 放在開頭，就是整份文件搜尋：
        - `//table` 是找尋全文件中的table標籤(整份文件的子孫)
    - 放在中間，就是前一個節點node(父節點)下全搜尋：
        - `//table//text()` 是找尋全文件中table標籤底下的所有文字(table下的子孫)
- 同輩`.`：以現在的節點node搜索，常用在同時呈現同一階層的資料 
<br>
<br>

+++
##### 範例
- body
    - 小孩：h1、a(Website)、p、img
    - 子孫：h1、text()、a、@href、p、img、@src、@width
- a
    - 小孩：@href、text()

```html
<html>
    <head>
        <title>Title</title>
    </head>
    <body>
        <h1>Subtitle</h1>
        <a href="http://tw.pyladies.com/">PyLadies Website</a>
        <p>
            This is a paragraph <br>
            <a href="http://www.meetup.com/PyLadiesTW/">PyLadies Meetup</a> <br>
            <a href="https://www.facebook.com/pyladies.tw">PyLadies FB</a> <br>
        </p>
        <img src="https://tw.pyladies.com/images/logos/twgirl_logo.png" width="99px"/>
    </body>
</html>
```
@[6,7,8,12,13]()
@[6,7,8,9,10,11,12,13]()

+++
@title[程式碼demo]
<iframe height="600px" width="100%" src="https://repl.it/@MARSW/XPathexample1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

+++
### Appendix
- [XPath 進階語法](https://tw.pyladies.com/~marsw/crawler02.slides.html#/7)