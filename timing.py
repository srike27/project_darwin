import sys
import numpy as np
import math
import pygame as pg 

def compare(timing1,timing2):
    num1 = timing1.ticks + timing1.days*timing1.ticks + timing1.ticks*timing1.days*timing1.eons
    num2 = timing2.ticks + timing2.days*timing2.ticks + timing2.ticks*timing2.days*timing2.eons
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