#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: bas.py
# @time: 2019/7/25 11:15
# @Software: PyCharm


__author__ = 'A.Star'

from matplotlib import pylab as plt
import numpy as np
from copy import deepcopy
from slapy.swarm.bas import BASEngine

npa = np.array
npr = np.random

# 带边界处理的BAS


class BAS(BASEngine):
    def __init__(self, steps=100, eps=0.01, chromosome=None, dim=2, bound=None, fitness_function=None, *,
                 fitness_value=-np.inf, init_method='random', step0=1, c=5, eta=0.95, **kwargs):
        super().__init__(steps, eps, chromosome, dim, bound, fitness_function, fitness_value=fitness_value,
                         init_method=init_method, **kwargs)
        self.eta = eta
        self.c = c
        self.step = step0

    def update(self, *args, **kwargs):
        d0 = self.step / self.c
        dir = npr.rand(self.dim) - 1
        dir = dir / (self.eps + np.linalg.norm(dir))
        xleft = self.chromosome + dir * d0
        fleft = self.fitness_function(xleft)
        xright = self.chromosome - dir * d0
        fright = self.fitness_function(xright)
        self.chromosome -= self.step * dir * np.sign(-fleft + fright)
        # 边界处理规则
        self.transboundary()

        if self.fitness() > self.gbest.fitness_value:
            self.gbest = deepcopy(self)
        self.step *= self.eta

    def fitness(self, *args, **kwargs):
        return super(BASEngine, self).fitness(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        super(BASEngine, self).initialize(*args, **kwargs)
        self.gbest = deepcopy(self)
        self.best = []
        self.path = []

    def analysis(self, *args, **kwargs):
        print('-' * 15)
        print("best:", self.best)
        print('-' * 15)
        print("path:", self.path)
        print('-' * 15)
        plt.figure(1)
        path = npa(self.path)
        plt.plot(path[:, 0], path[:, 1], 'r+-')
        plt.figure(2)
        plt.title('itor in each steps')
        plt.plot(self.best, 'r-', label='best')
        plt.xlabel("Iteration")
        plt.ylabel("function value")
        plt.show()
        print(self.gbest.chromosome)

    def record(self, *args, **kwargs):
        print(len(self.path))
        self.path.append(deepcopy(self.chromosome))
        self.best.append(self.fitness_value)
