# 指定文件夹，合并文件夹下所有的表格(要求表格的的列名一致，表格格式限于xlsx，csv)

import os
import pandas as pd
from  tqdm import tqdm

# 指定合并文件夹的路径
dir_path = input("请指定要合并的文件夹的路径：")

# 首先获取所有文件的路径
fileList = os.listdir(dir_path)

# 读取第一个文件的内容
if (fileList[0].split('.'))[-1] == "csv":
    df1 = pd.read_csv(dir_path + '/' + fileList[0])
elif (fileList[0].split('.'))[-1] == "xlsx":
    df1 = pd.read_excel(dir_path + '/' + fileList[0])
else:
    print('请确认表格格式为xlsx或csv')
    



for file in tqdm(fileList):
    if (file.split('.'))[-1] == "csv":
        df = pd.read_csv(dir_path + '/' + file)
    elif (fileList[0].split('.'))[-1] == "xlsx":
        df = pd.read_excel(dir_path + '/' + file)
    else:
        print(f'请确认{file}为xlsx或csv')

    df1 = df1.append(df)
    print(df1.shape)
    df1 = df1.drop_duplicates()
    
    df1.to_csv(dir_path + '/' + 'all.csv', index=False, encoding='utf-8-sig')