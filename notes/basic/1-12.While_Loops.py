#---loop(while)迴圈---
#while：當條件為真時，重複執行一系列語句。

# 基本用法
i = 1
while i < 6:
    print(i)
    i += 1 #請務必增加 i 的值，否則循環將無限持續

#使用 break 跳出迴圈
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#使用 continue 跳過當前迴圈，繼續下一個迴圈
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# 使用 else 在 while 循環結束後執行一段代碼
# 如果迴圈被 break 語句停止， else 區塊不會被執行
i = 1
while i < 6:
    print(i)
    i += 1 
else:
    print("i is no longer less than 6")