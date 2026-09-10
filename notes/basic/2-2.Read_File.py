#--- Read Files 開啟文件 ---

# 方法1：此方法需要手動關閉文件，以釋放系統資源。
df = open("/Users/kire/06. VScode/python_project/ETL_Learn/data/shipments.csv")

# 方法2：with語句會自動關閉文件，無需手動調用close()方法。
with open("/Users/kire/06. VScode/python_project/ETL_Learn/data/shipments.csv") as df:
    print(df.read())

# 快速檢視文件
print(df.read()) # 讀取整個文件
print(df.readline()) # 讀取文件中的一行

# 使用 pandas 讀取 CSV 文件
import pandas as pd

#df.head(n)        # 顯示前n行數據
#df.tail(n)        # 顯示後n行數據
#df.info()         # 顯示數據的基本信息
#df.describe()     # 顯示數據的統計信息
#df.columns        # 顯示數據的列名
#df.shape          # 顯示數據的行數和列數
#df.isnull().sum() # 顯示每列的缺失值數量

# close()；關閉文件，釋放資源。使用完文件後，應該關閉文件以釋放系統資源。
# 使用 with 語句可以自動關閉文件，無需手動調用 close() 方法。

df = open("/Users/kire/06. VScode/python_project/ETL_Learn/data/shipments.csv")
print(df.read())
df.close()