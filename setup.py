# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  setup.py
@Time    :  2022/5/20 2:52 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='hitfilter',
    packages=find_packages(),
    include_package_data=True,
    author="kamalyes",
    version="0.0.1",
    auth_email="mryu168@163.com",
    python_requires=">=3.8",
    description="基于DFA的敏感词过滤器",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamalyes/hitfilter",
    platforms='any',
    license="MIT"
)
