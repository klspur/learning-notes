#---loop(for)迴圈---
#for：執行一系列語句，對列表、元組、集合等中的每個元素執行一次。

# 建立一數列為範例
fruits = ["apple", "banana", "cherry"]

# 基本用法
# 對list/tuples迴圈，不需要事先指定索引變量
for x in fruits:
    print(x)

#對str迴圈，會將字串拆解成單個字元
for x in "banana":
    print(x)

#使用 break 跳出迴圈
for x in fruits:
    if x == "banana":
        break
    print(x)

#使用 continue 跳過當前迴圈，繼續下一個迴圈
for x in fruits:
    if x == "banana":
        continue
    print(x)

#使用 enumerate() 函數獲取索引和值
for i, x in enumerate(fruits):
    print(f'第 {i+1} 筆水果是 {x}')

#使用 range() 產生數字序列，並使用 for 迴圈遍歷
for x in range(6):  #range(6) 會產生 0~5 的數字列
    print(x)

for x in range(2, 6):  #range(2, 6) 會產生 2~5 的數字列
    print(x)

for x in range(2, 30, 3):  #range(2, 30, 3) 會產生 2~29 的數字列，步長為3
    print(x)

#使用 else 在 for 迴圈中，當迴圈正常結束時會執行 else 區塊
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#如果迴圈被 break 語句停止， else 區塊不會被執行。
for x in range(6):
    if x == 3: 
        break
    print(x)
else:
    print("Finally finished!")