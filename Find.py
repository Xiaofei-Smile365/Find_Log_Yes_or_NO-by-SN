# -*- coding: UTF-8 -*-

"""

@author:smile

@file:Find.py

@time:2020/10/28

"""

import os
import re

import pandas as pd

def find(log, sn, file_name, result_file):
    print("新建文件以存储log文件名")
    # 新建文件以存储log文件名
    file = open(file_name, 'w')
    new_file_columns = ['file_name']
    data = pd.DataFrame(columns=new_file_columns)
    data.to_csv(file_name, index=False)
    file.close()

    print("遍历文件夹，获取文件名")
    # 遍历文件夹，获取文件名
    file_name_list = []

    def getFlist(path, name_list):
        for root, dirs, files in os.walk(path):
            name_list = name_list + files
        return name_list
    file_name_list = getFlist(log, file_name_list)

    print("遍历后的文件名写入到文件中")
    # 遍历后的文件名写入到文件中
    data = pd.DataFrame(data=file_name_list)
    data.to_csv(file_name, mode='a', header=False, index=False)  # 写入到文件

    print("获取需查找的SN")
    # 获取需查找的SN
    sn_data = pd.read_excel(sn)
    sn_df = pd.DataFrame(sn_data)
    sn_name_list = sn_df["SN"]

    print("执行查找")
    # 执行查找
    sn_result_yes = []
    for sn_name in sn_name_list:
        result_sum = 0
        for log_name in file_name_list:
            result_single = re.findall(str(sn_name), str(log_name))
            result_sum = result_sum + len(result_single)
        if result_sum >= 1:
            sn_result = "Yes"
        else:
            sn_result = "No"
        sn_result_yes.append([str(sn_name), str(sn_result)])

    print("新建文件以存储查找结果")
    # 新建文件以存储查找结果
    sn_result_file = open(result_file, 'w')
    new_file_columns = ['SN', "Result"]
    data = pd.DataFrame(columns=new_file_columns)
    data.to_csv(result_file, index=False)
    file.close()

    print("Result写入到文件中\n")
    # Result写入到文件中
    data = pd.DataFrame(data=sn_result_yes)
    data.to_csv(result_file, mode='a', header=False, index=False)  # 写入到文件


if __name__ == '__main__':
    print("The Program is Start!\n")
    print("Find程式开始\n")
    # 文件路径、文件名等定义
    source_log = "./source_Log/"
    file_name_from_source_log = "./file_name_from_source_log.csv"
    sn_list = "./SN_List.xlsx"
    result = "./result.csv"

    # find函数，实现根据sn查找log，并将结果写入到文件
    find(source_log, sn_list, file_name_from_source_log, result)
    print("Find程式结束\n")

    print("The Program is Over!\n")
    pass
