# --- 數值型別 (Numeric Types) ---
# Python 有三種主要的數值型別：
# 1. int    -> 整數 (integer)
# 2. float  -> 浮點數 (decimal, real number)
# 3. complex -> 複數 (complex number, 含實部與虛部)

x = 1        # int
y = 2.8      # float
z = 1j       # complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# --- 型別轉換 (Type Conversion) ---
# 可使用 int()、float()、complex() 互相轉換

a = float(x)  # int -> float
b = int(y)    # float -> int (小數會被截斷)
c = complex(x)  # int -> complex

print(a, b, c)

# --- 隨機數 (Random Numbers) ---
# Python 沒有內建 random 類型，但可透過 random 模組生成隨機數。
import random

rand_num = random.randrange(1, 10)  # 生成 [1, 9] 的隨機整數
print(rand_num)

# --- 數學運算 (Arithmetic Operations) ---
# + 加、- 減、* 乘、/ 除、% 餘數、** 次方、// 取整除

a = 1
b = 4

print(a + b)  # 19
print(a - b)  # 11
print(a * b)  # 60
print(a / b)  # 3.75
print(a % b)  # 3
print(a ** b) # 15^4 = 50625
print(a // b) # 3

# --- 內建數學模組 (math module) ---
import math

print(math.sqrt(64))   # 開根號 -> 8.0
print(math.ceil(1.4))  # 無條件進位 -> 2
print(math.floor(1.4)) # 無條件捨去 -> 1
print(math.pi)         # 圓周率 3.141592...

# --- 實作範例：圓面積與球體積 ---
# 使用 math 模組與公式練習數學應用

radius = 5
circle_area = math.pi * radius**2
sphere_volume = (4/3) * math.pi * radius**3

print(f"半徑 {radius} 的圓面積為: {circle_area:.2f}") # .2f 分成三個部分：.(小數格式)、2(小數點後要保留2位)、f(浮點數)
print(f"半徑 {radius} 的球體積為: {sphere_volume:.2f}")

# --- 小結 ---
# ✅ Python 數字型別：int / float / complex
# ✅ 型別轉換：int()、float()、complex()
# ✅ 隨機數：random 模組
# ✅ 常用數學運算：+、-、*、/、%、**、//
# ✅ math 模組提供進階運算：sqrt()、ceil()、floor()、pi 等
