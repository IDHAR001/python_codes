#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: json_steve
import os


def file_paths():
    """
    获取当前目录下所有非文件的路径
    :return: 返回路径列表
    """
    path_list = []
    for root, dirs, files in os.walk('.'):
        # 不能是空文件
        if not len(files) == 0:
            for file_name in files:
                # 拼接路径
                path = os.path.join(root, file_name)
                # print(path)
                path_list.append(path)
    return path_list


def count_lines(path):
    """
    根据文件路径统计文件的行数
    :param path: 文件路径
    :return: 行数
    """
    num = 1
    f = open(path, 'rb')
    for line in f:
        num += 1
    f.close()
    return num

if __name__ == '__main__':
    count = 0  # 总行数
    for path in file_paths():
        print(path)
        count += count_lines(path)
    print(count)
