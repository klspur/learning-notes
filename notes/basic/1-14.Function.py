#--- Function 函式 ---

# 基本用法
# 使用 def 定義函式

def hello():
    print("Hello, Python!")

hello()  # 呼叫函式

# --- 傳入參數 (Parameters) ---

def greet(name):
    print(f"Hi, {name}!")

greet("小明")

# --- 多個參數 ---

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# --- 預設參數值 (Default Parameters) ---

def intro(name, country="Taiwan"):
    print(f"我是 {name}，我來自 {country}。")

intro("承諺")
intro("Adam", "Japan")

# --- 任意參數 (*args) ---
# 當參數數量不固定時使用 *args，會以 tuple 接收

def total(*numbers):
    print(numbers)
    return sum(numbers)

print(total(1, 2, 3, 4))

# --- 任意關鍵字參數 (**kwargs) ---
# 使用 **kwargs 接收 key=value 形式參數，會以 dict 儲存

def profile(**info):
    print(info)

profile(name="承諺", job="Data Engineer", age=24)

# --- 回傳值 (return) ---
# 函式可以回傳多個值，會以 tuple 形式返回

def calc(a, b):
    return a+b, a-b, a*b

x, y, z = calc(10, 5)
print(x, y, z)

# --- 變數作用域 (Scope) ---
# 區域變數 (local) 只能在函式內使用
# 全域變數 (global) 可在程式任何地方存取

x = 10  # 全域

def test():
    x = 5  # 區域 (不同於全域)
    print(x)

test()
print(x)

# 若要在函式內修改全域變數，使用 global

y = 10

def modify():
    global y
    y = 20

modify()
print(y)

# --- Lambda 函式 (匿名函式) ---
# 簡短、一次性使用的小型函式

square = lambda n: n * n
print(square(4))

# 搭配 sorted() 排序複合資料
users = [("承諺", 24), ("Adam", 30), ("Bob", 20)]
sorted_users = sorted(users, key=lambda x: x[1])  # 依年齡排序
print(sorted_users)

# 限制位置參數：函數不許輸入參數名稱
# 在參數名稱後加上 ,/
def my_function(name, /):
  print("Hello", name)

my_function("Ariel") #正確
#my_function(name = "Ariel") # 錯誤

# 關鍵字參數：呼叫函數時必須輸入參數名稱
# 在參數名稱前加上 *,
def my_function(*, name):
  print("Hello", name)

#my_function("Ariel") #錯誤
my_function(name = "Ariel") # 正確