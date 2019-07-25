#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: __init__.py.py
# @time: 2018/8/28 10:36
# @Software: PyCharm

from bas.rbas import RBAS
from bas.bas import BAS

from astartool.setuptool import get_version

version = (0, 0, 2, 'final', 0)
__version__ = get_version(version)

del get_version
