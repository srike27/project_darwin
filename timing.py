import sys
import numpy as np
import math
import pygame as pg 

def compare(timing1,timing2):
    num1 = timing1.ticks + timing1.days*1000 + timing1.eons*1000*1000
    num2 = timing2.ticks + timing2.days*1000 + timing2.eons*1000*1000
    if num1>num2:
        return 1
    else:
        return -1

class timing:
    def __init__(self,ticks,days,eons):
        self.ticks = ticks
        self.days = days
        self.eons = eons

    def next(self):
        self.ticks += 1
        if self.ticks > 1000:
            self.days += 1
            self.ticks = 0
        if self.days > 1000:
            self.eons += 1
            self.days = 0

    def __add__(self,a):
        num = self.ticks + 1000*self.days + 1000*1000*self.eons
        num2= a.ticks + a.days*1000 + self.eons*1000*1000
        nf = num + num2
        eons = nf//(1000*1000)
        days = nf//(1000) - 1000*eons
        ticks = nf - 1000*days - 1000*1000*eons
        out = timing(ticks= ticks,days = days,eons = eons)
        return out
