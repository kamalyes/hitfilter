# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  filtration_key.py
@Time    :  2022/5/20 2:52 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  过滤垃圾词
"""
list_keywords = []
with open("keywords", encoding='UTF-8') as file:
    lines = file.readlines()
    for index in lines:
        if index.isalpha() or index.isupper() or index.isupper() or index.isalnum():
            pass
        else:
            list_keywords.append(index)
    list_delete_repetition = {}.fromkeys(list_keywords).keys()
with open("keywords_bak", "a", encoding='UTF-8') as file:
    file.writelines(list_delete_repetition)
print(len(lines), len(set(list_delete_repetition)))
