# --- 基本概念 ---
# Boolean (布林值) 只有兩種狀態：True 或 False。
# 通常用於條件判斷與控制流程。

print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False

# 可以將比較結果存成變數
is_greater = 5 > 2
print(is_greater)  # True

# --- if 條件判斷 ---
# Boolean 常搭配 if 使用。
a = 200
b = 33
if b > a:
    print("b 大於 a")
else:
    print("b 不大於 a")

# --- bool() 函式 ---
# 可用於判斷任意物件的真偽。
# 以下內容會被視為 False：
#   False, None, 0, 空字串"", 空 list/tuple/dict/set

print(bool("Hello"))  # True
print(bool(15))        # True
print(bool([]))        # False
print(bool(0))         # False
print(bool(None))      # False

# --- 自訂物件的真偽 ---
# 若類別未定義 __len__ 或 __bool__，則預設為 True。
# bool()函數可以評估任何值的布林值

class MyClass():
    def __len__(self):
        return 0

obj = MyClass()
print(bool(obj))  # False，因為 __len__ 回傳 0

# --- 常見布林運算子 ---
# and：兩者皆 True 才為 True
# or：任一為 True 即 True
# not：反轉布林值

x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# --- 布林在函式中的應用 ---
def is_adult(age):
    return age >= 18

print(is_adult(20))  # True
print(is_adult(15))  # False

# --- 實作範例：登入驗證模擬 ---
user = "admin"
password = "1234"

login = (user == "admin") and (password == "1234")
if login:
    print("登入成功！")
else:
    print("帳號或密碼錯誤。")

# --- 小結 ---
# ✅ Boolean 僅有 True / False 兩種值
# ✅ 比較運算會回傳布林值 (>, <, ==, !=, >=, <=)
# ✅ bool() 可測試物件是否為「真」或「假」
# ✅ and / or / not 控制多條件邏輯
# ✅ 常見應用：if 判斷、函式回傳、資料驗證

