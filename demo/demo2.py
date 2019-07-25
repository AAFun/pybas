#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo2.py
# @time: 2019/7/25 10:52
# @Software: PyCharm


__author__ = 'A.Star'

from bas import BAS


def f(x):
    c, d = x
    return 1 / ((1 + (c + d + 1) ** 2 * (19 - 14 * c + 3 * d ** 2 - 14 * d + 6 * c * d + 3 * d ** 2)) * (
            30 + (2 * c - 3 * d) ** 2 * (18 - 32 * c + 12 * c ** 2 + 48 * d - 36 * c * d + 27 * d ** 2)))


if __name__ == '__main__':
    bas_engine = BAS(
        steps=500,
        dim=2,
        fitness_function=f,
        step=1,
        eta=0.95,
        bound=[[-2, 2], [-2, 2]],
        transboundary_rules='mod'
    )
    bas_engine.run()
