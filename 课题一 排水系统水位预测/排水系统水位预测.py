import pandas as pd
import numpy as np

#读取数据Rainfall_information.xlsx
# Rainfall_information = '课题一 排水系统水位预测\\Rainfall_information.xlsx'
# data = pd.read_excel(Rainfall_information)
# print(data.head(10))

#读取47次的场降雨下监测数据并合并为一个
all_data = []
for x in range(1,48):
    rain_data_path = f'课题一 排水系统水位预测\\data\\rain_{x}.csv'
    df = pd.read_csv(rain_data_path)
    df['rain_id'] = x  
    all_data.append(df)
data = pd.concat(all_data, ignore_index=True)#ignore_index忽略原来的索引重置索引
#print(data)

#数据清理，查找缺失值
print("=" * 50)
print("数据缺失值检查：")
print(data.isnull().sum())#统计每一列的缺失值数量
print(f"总缺失值数量：{data.isnull().sum().sum()}")

#检查是否有负数
print("=" * 50)
print("负数检查：")
print((data[['Node_1', 'Node_2', 'Node_3', 'Node_4', 'Rain']] < 0).sum())

# 数据总体特征描述
print("=" * 50)
print("\n数据范围统计：")
print(data[['Node_1', 'Node_2', 'Node_3', 'Node_4', 'Rain']].describe())

# 一次性检查并转换
print("=" * 50)
print("数据类型检查：")
print(data.dtypes)

#保存处理后的数据
data.to_csv('课题一 排水系统水位预测/cleaned_data.csv', index=False)