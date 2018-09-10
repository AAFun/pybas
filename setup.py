#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 0005 上午 1:29
# @Author  : 河北雪域网络科技有限公司 A.Star
# @Site    : 
# @File    : setup.py
# @Software: PyCharm

# !/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import slapy

setup(
    name="pybas",
    version=bas.__version__,
    description=(
        'Python implementation algorithm'
    ),
    long_description=open('README.rst').read(),
    author='A.Star',
    author_email='chenxiaolong12315@163.com',
    maintainer='A.Star',
    maintainer_email='chenxiaolong12315@163.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://gitee.com/snowlandltd/snowland-algorithm-python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'numpy>=1.12.0',
        'gaft>=0.5.4'
    ],
)
