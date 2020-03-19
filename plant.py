import sys
import numpy as np
import math
import pygame as pg 

class plant:
    def __init__(self,x,y,grate):
        self.x = x
        self.y = y
        self.size = 1
        self.grate = grate

    def grow(self):
        self.size *= 1 + self.grate

    def eaten(self):
        self.size /= 1 + self.grate
        if self.size < 1:
            self.__del__()

    def __del__(self):
        print("tree eaten")