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
        self.size_cap = 100

    def grow(self):
        if self.size < self.size_cap:
            self.size *= 1 + self.grate

    def eaten(self,erate):
        self.size /= 1 + erate
        if self.size < 1:
            self.__del__()

    def __del__(self):
        print("plant eaten")