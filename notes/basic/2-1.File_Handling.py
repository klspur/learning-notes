#---File Handling 文件處理---

# open()函數：接受文件名和模式作為參數
# 文件開啟四種方法：
#1. "r" - 讀取（默認模式，文件必須存在）
#2. "a" - 追加（如果文件不存在，則創建新文件）
#3. "w" - 寫入（如果文件存在，則覆蓋原有內容；如果文件不存在，則創建新文件）
#4. "x" - 創建（如果文件已存在，則操作失敗）

file = open("example.txt", "r") 

# 指定文件的編碼方式
file = open("example.txt", "r", encoding="utf-8")

# 指定文件是否以二進位制或文本模式處理
# 1."t" - 文本模式（默認）
# 2."b" - 二進位制模式

f = open("demofile.txt", "rt")
f = open("demofile.txt", "b")