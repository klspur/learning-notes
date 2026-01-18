# Python Operators 學習筆記
# =========================
# --- 運算子類型 ---
# Python 主要運算子分為以下幾類：
# 1. 算術運算子 (Arithmetic Operators)
# 2. 指派運算子 (Assignment Operators)
# 3. 比較運算子 (Comparison Operators)
# 4. 邏輯運算子 (Logical Operators)
# 5. 身分運算子 (Identity Operators)
# 6. 成員運算子 (Membership Operators)
# 7. 位元運算子 (Bitwise Operators)

# --- 1️⃣ 算術運算子 ---
a = 10
b = 3
print(a + b)   # 加法 -> 13
print(a - b)   # 減法 -> 7
print(a * b)   # 乘法 -> 30
print(a / b)   # 除法 -> 3.333...
print(a % b)   # 取餘數 -> 1
print(a ** b)  # 次方 -> 10^3 = 1000
print(a // b)  # 取整除 -> 3

# --- 2️⃣ 指派運算子 ---
x = 5
x += 3   # x = x + 3 -> 8
x -= 2   # x = x - 2 -> 6
x *= 4   # x = x * 4 -> 24
x /= 3   # x = x / 3 -> 8.0
x %= 5   # x = x % 5 -> 3.0
x **= 2  # x = x^2 -> 9.0
x //= 4  # x = x // 4 -> 2.0
print(x)

# --- 3️⃣ 比較運算子 ---
a = 10
b = 20
print(a == b)  # 相等 -> False
print(a != b)  # 不相等 -> True
print(a > b)   # 大於 -> False
print(a < b)   # 小於 -> True
print(a >= 10) # 大於等於 -> True
print(b <= 10) # 小於等於 -> False

# --- 4️⃣ 邏輯運算子 ---
x = True
y = False
print(x and y)  # 兩者皆 True -> False
print(x or y)   # 任一 True -> True
print(not x)    # 反轉 -> False

# --- 5️⃣ 身分運算子 (is / is not) ---
# 用於判斷兩個變數是否指向同一個物件 (記憶體位置)
# is：檢查兩個變數是否指向記憶體中的相同物件
# ==：檢查兩個變數的值是否相等

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)      # False，內容相同但不同物件
print(x is z)      # True，同一個物件
print(x is not y)  # True

# --- 6️⃣ 成員運算子 (in / not in) ---
# 用於檢查元素是否存在於序列 (list, tuple, string, etc.)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)     # True
print("grape" not in fruits)  # True

# --- 7️⃣ 位元運算子 (Bitwise Operators) ---
# 用於二進位操作，常見於低階運算或效能優化。
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (左移), >> (右移)

a = 6   # 110 (二進位)
b = 3   # 011
print(a & b)   # AND -> 010 -> 2
print(a | b)   # OR  -> 111 -> 7
print(a ^ b)   # XOR -> 101 -> 5
print(~a)      # NOT -> -7 (取反)
print(a << 1)  # 左移一位 -> 12
print(a >> 1)  # 右移一位 -> 3

# --- 綜合練習：條件運算 ---
# 結合多種運算子實作邏輯判斷

score = 85
is_pass = (score >= 60) and (score <= 100)
print(f"分數 {score} 是否及格: {is_pass}")

# --- 小結 ---
# ✅ 算術：+ - * / % ** //
# ✅ 指派：= += -= *= /= %= **= //=
# ✅ 比較：== != > < >= <=
# ✅ 邏輯：and / or / not
# ✅ 身分：is / is not
# ✅ 成員：in / not in
# ✅ 位元：& | ^ ~ << >>

