#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: rbas.py
# @time: 2018/8/29 18:36
# @Software: PyCharm


from slapy.swarm.bas import BASEngine
import numpy as np
from copy import deepcopy

npr = np.random



# 模拟退火结合的BAS


class RBASEngine(BASEngine):
    def __init__(self, steps=100, eps=0.01, chromosome=None, dim=2, bound=None, fitness_function=None, *,
                 fitness_value=-np.inf, init_method='random', step0=1, c=5, eta=0.95, **kwargs):
        """
        :param steps: 迭代次数
        :param eps: 精度
        :param chromosome: 数据值
        :param dim: 数据维度
        :param bound: 数据范围
        :param fitness_function: 评价函数
        :param fitness_value: 评价值
        :param init_method: 初始化参数
        :param step0: 初值
        :param c:
        :param eta:
        :param kwargs:
        """
        super().__init__(steps, eps, chromosome, dim, bound, fitness_function, fitness_value=fitness_value,
                         init_method=init_method, step0=step0, c=c, eta=eta, **kwargs)

    def update(self, *args, **kwargs):
        d0 = self.step / self.c
        dir = npr.rand(self.dim) - 1
        dir = dir / (self.eps + np.linalg.norm(dir))
        xleft = self.chromosome + dir * d0
        fleft = self.fitness_function(xleft)
        xright = self.chromosome - dir * d0
        fright = self.fitness_function(xright)

        if self.fitness() > self.gbest.fitness_value:
            self.gbest = deepcopy(self)
            self.chromosome -= self.step * dir * np.sign(-fleft + fright)
        else:
            if npr.rand() < self.step:
                self.chromosome -= self.step * dir * np.sign(fleft - fright)
            else:
                self.chromosome -= self.step * dir * np.sign(-fleft + fright)

        self.step *= self.eta

RBAS = RBASEngine