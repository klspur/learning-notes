# Strings are arrays
# 1. Python 中的字串是 Unicode 字元陣列 
# 2. 單個字元只是一個長度為 1 的字串，方括弧可查詢字串元素的位置。（第一個字元位置為0）

# --- 基本定義 ---
# 字串 (String) 是由單引號 ' 或雙引號 " 包起來的文字。
x = "Hello"
y = 'World'
print(x, y)

# --- 多行字串 ---
# 使用三個單引號或三個雙引號包裹可建立多行字串。
a = '''
這是一個
多行字串
'''
print(a)

# --- 字串索引 (Indexing) ---
# 字串可視為字元陣列，索引從 0 開始。
word = "Python"
print(word[0])  # 第一個字元 P
print(word[-1]) # 最後一個字元 n

# --- 字串切片 (Slicing) ---
print(word[0:3])  # 'Pyt'
print(word[2:])   # 'thon'
print(word[:4])   # 'Pyth'

# --- 字串長度 ---
print(len(word))  # 6

# --- in 與 not in 運算子 ---
text = "Learning Python is fun!"
print("Python" in text)      # True
print("Java" not in text)    # True

# --- 字串迴圈 ---
for ch in "Data":
    print(ch)

# --- 字串合併與重複 ---
a = "Hello"
b = "World"
print(a + " " + b)  # 合併 (Concatenation)
print(a * 3)         # 重複三次

# --- 字串方法 (String Methods) ---
msg = " hello, python! "

print(msg.upper())    # 全部大寫
print(msg.lower())    # 全部小寫
print(msg.strip())    # 移除前後空白
print(msg.replace("python", "world"))  # 取代文字
print(msg.split(","))  # 以逗號分割成 list

# --- 字串格式化 (String Formatting) ---
# 1️⃣ 使用 f-string (推薦用法)
name = "承諺"
age = 24
print(f"Hello, my name is {name}, and I am {age} years old.")

# 2️⃣ 使用 format()
print("Hello, my name is {}, and I am {} years old.".format(name, age))

# 3️⃣ 指定位置
print("{1} 是 {0} 歲".format(age, name))

# --- 字串內建函式 ---
# 常見有：len(), type(), str(), int(), float() 等

num = 25
text = str(num)
print(type(text))  # <class 'str'>

# --- 字元編碼 ---
# ord() 取得字元的 Unicode 編碼值；chr() 則將數值轉回字元。
print(ord('A'))  # 65
print(chr(65))   # 'A'

# --- 實作範例：字串清理與格式化 ---
raw_name = "  lIanXin hosPital  "
clean_name = raw_name.strip().title()  # 去空白並轉換首字大寫
print(clean_name)  # 'Lianxin Hospital'

# --- 小結 ---
# ✅ 建立字串：單引號、雙引號、多行字串
# ✅ 索引與切片：存取部分內容
# ✅ 方法：upper()、lower()、strip()、replace()、split()
# ✅ 格式化：f-string、format()
# ✅ 轉型與編碼：str()、ord()、chr()

# 應用練習題
# =========================
# --- 題目 1：字串長度與首尾字元 ---
# 請寫一段程式，輸入一個字串，輸出：
# - 字串長度
# - 第一個字元與最後一個字元
text = input("請輸入一個字串")
print(f"長度: {len(text)}，字首: {text[0]}，字尾: {text[-1]}")

# --- 題目 2：檢查關鍵字是否存在 ---
# 使用 'in' 或 'not in' 判斷字串中是否包含特定單字。
lyric = "My Final Breath. Swollow by the womb of death." 
text = input("請輸入一個英文單字")
if text in lyric:
    print(f"'{text}'在句子中")
else:
    print(f"'{text}'不在句子中")

