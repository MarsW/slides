@snap[midpoint slide1]
<h1>字典</h1>
### (dictionary) `dict`
@ul[](false)
- @size[80%]字典基本操作
- @size[80%]字典的迭代
- @size[80%]常用的資料型別
- @size[80%]補充知識-字典相關好用功能
@ulend

---
@snap[midpoint slide1]
<h1>字典基本操作</h1>
@snapend

+++
@title[字典宣告]
#### 字典宣告
``` python 
dict_member = {"Mars":20, "姿君":25, "毛毛":10}
```
@ul[](false)
- 字典用大括號{}宣告，每個 key 及其對應的 value 為一組元素
{key1:value1, key2:value2}
- key 需為不可變物件 (eg. int、float、str)
@ulend
@[1](字串 "Mars", "姿君", "毛毛" 是字典的 key)
@[1](而 key "Mars" 對應的 value 是 20)
@[1]( 　key "姿君"  對應的 value 是 25)

+++
@title[字典取值]
#### 字典取值
```python 
dict_member = {"Mars":20, "姿君":25, "毛毛":10}
print(dict_member["Mars"])
```
@size[80%](*20*)
@ul[para_n](false)
- **`字典名稱[key]`**：字典以鍵值 key 去存取資料 value，<br>很像是串列用索引 index 去存取：**`串列名稱[index]`**
@ulend
<br>
<br>

```python 
list_value = [20,25,10]
print(list_value[0])
```
+++
@title[為何要用字典]
#### 想像 會員儲值 的情境
Mars 剛開始有 $20、姿君 有 $25、毛毛 有 $10  
Mars 儲值 $15、姿君 儲值 $5  

+++
#### 用 串列 `list` 儲存資料
``` python
list_member = [["Mars",20],["姿君",25],["毛毛",10]]
list_member[0][1]+=15
list_member[1][1]+=5
print(l)
```
@size[80%](*`[['Mars', 35], ['姿君', 30], ['毛毛', 10]]`*)
@[1](Mars 剛開始有 $20、姿君 有 $25、毛毛 有 $10)
@[2](Mars 儲值 15元 # Mars是第1個會員{index=0},錢是在會員的第2個位置{index=1} )
@[3](再來是 姿君儲值 5元 # 姿君是第2個會員{index=1},錢是在會員的第2個位置{index=1} )
<br>
<br>

@ul[para_n]
- 但這是剛好我們知道 Mars 是第1個會員,姿君是第2個
@ulend

+++
#### 串列 `list` 改值的彈性寫法
```python
list_member = [["Mars",20],["姿君",25],["毛毛",10]]
for member in list_member:
    if member[0]=="Mars":
        member[1]+=15
for member in list_member:
    if member[0]=="姿君":
        member[1]+=5
print(l)
```
@size[80%](*`[['Mars', 35], ['姿君', 30], ['毛毛', 10]]`*)
@[2](查詢所有會員)
@[3](如果會員的名字{index=0} 是 Mars)
@[4](就把會員的錢{index=1} 多加上 $15)
@[5](再次查詢所有會員：這次要是幫姿君儲值)
@[6](如果會員的名字{index=0} 是 姿君)
@[7](就把會員的錢{index=1} 多加上 $5)

+++
#### 用字典可以方便的存取資料
```python
dict_member = {"Mars":20,"姿君":25,"毛毛":10}
dict_member["Mars"] += 15
dict_member["姿君"] += 5
print(dict_member)
print(dict_member["Mars"],dict_member["姿君"])
```
@size[80%](*`{'Mars': 35, '姿君': 30, '毛毛': 10}`*)  
@size[80%](*`35 30`*)

+++
#### [練習] 計算庫存
水果庫存、價格都以字典型別儲存，  
請計算若水果都賣出後，可賺進多少錢？
``` python
stock={
    "banana":5,
    "apple":3,
    "orange":10
}
price={
    "banana":5,
    "apple":20,
    "orange":15
}
```
@ul[para_n]
- @size[70%]Hints:
@ulend

<pre class="fragment" style="margin: -30px 0px !important;">
  <code>revenue = 0
revenue += stock["____"] * price["____"]
revenue += stock["____"] * price["____"]
revenue += stock["____"] * price["____"]
print(revenue)
</code>
</pre>

Note:

``` python
revenue += stock["banana"] \* price["banana"]  
revenue += stock["apple"]  \* price["apple"]  
revenue += stock["orange"] \* price["orange"]  
print(revenue)  
```