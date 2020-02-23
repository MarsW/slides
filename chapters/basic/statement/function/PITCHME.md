@snap[midpoint slide1]
<h1>函式</h1>
@snapend

+++
### 函式語法
```python
# 定義函式
def 函式名稱(參數1,參數2,...):
    程式碼
    程式碼
    程式碼
    return 物件1,物件2,物件3
# 呼叫函式
函式名稱(引數1,引數2,...)
```
  
- 參數(patameter)是定義函式時指定的名稱，可有可無
- 引數(argumwnt)是函數呼叫時傳入的真正物件，在呼叫時會建立參數和引數的綁定關係。
    - 需和參數的個數一樣
- 函式內的程式碼可以有各種可能(eg. 迴圈、判斷式、運算...)
- return回傳可有可無(若無會回傳None)，用tuple可回傳多個物件

+++
### 生活中的函式-洗衣機
```python
def 洗衣機():
    注水
    旋轉清洗
    排水
    旋轉脫水
```

<table>
    <tbody><tr>
        <td><img src="assets/img/func_wash_hand.jpg"></td>
        <td><img src="assets/img/func_wash_machine.jpg"></td>
    </tr>
</tbody></table>

+++
### 生活中的函式-咖啡機

![func_coffie](assets/img/func_coffie.png)

+++
### 函式的好處
- 自己打造工具 
- 利用呼叫，方便重複利用
- 程式碼更為簡潔   

+++
### 內建函式可能的樣貌
```python
def max(data):
    num_max = -999999999
    for i in data:
        if i>=num_max:
            num_max = i
    return num_max
    
print(max([1,2,7,9,10]))
a=max([1,2,7,9,10])
print(a)
```
+++
### Appendix
- [可視範圍](https://tw.pyladies.com/~marsw/book_basic/basic_06.slides.html#/3)

