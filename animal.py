import sys
import numpy as np
import math
import pygame as pg 

class animal:
    def updatestate(self):
        tmvx = self.velx
        tmvy = self.vely
        self.px+=self.velx
        self.py+=self.vely
        self.velx = self.velx + self.ax
        self.vely = self.vely + self.ay
        self.cspd =math.sqrt(self.velx*self.velx+self.vely*self.vely)
        if self.ax==0:
            self.velx = tmvx
        if self.ay==0:
            self.vely = tmvy

    def impulse(self,acx,acy):
        self.ax = acx
        self.ay = acy
        self.updatestate()
        self.ax = 0
        self.ay = 0

    def frictiony(self,nu):
        #self.mtest()
        if self.cspd != 0: 
            #print(self.velx,self.vely)
            self.ax = -round((self.velx/self.speed)*nu)
            #self.ay = -round((self.vely/self.speed)*nu)
            #print(self.ax)
            #print(self.ay)
            self.updatestate()
            #print("velx",self.velx)
            #print("vely",self.vely)
            self.ax = 0
            #self.ay = 0
        else:
            self.ax=0
            #self.ay=0
            #self.mtest()



    def frictionx(self,nu):
        #self.mtest()
        if self.cspd != 0: 
            #print(self.velx,self.vely)
            #self.ax = -round((self.velx/self.speed)*nu)
            self.ay = -round((self.vely/self.speed)*nu)
            #print(self.ax)
            #print(self.ay)
            self.updatestate()
            #print("velx",self.velx)
            #print("vely",self.vely)
            #self.ax = 0
            self.ay = 0
        else:
            #self.ax=0
            self.ay=0
            #self.mtest()

    def friction(self,nu):
        #self.mtest()
        if self.speed != 0: 
            #print(self.velx,self.vely)
            self.ax = -round((self.velx/self.speed)*nu)
            self.ay = -round((self.vely/self.speed)*nu)
            #print(self.ax)
            #print(self.ay)
            self.updatestate()
            #print("velx",self.velx)
            #print("vely",self.vely)
            self.ax = 0
            self.ay = 0
        else:
            self.ax=0
            self.ay=0
            #self.mtest()

    def grow(self):
        self.size *= 1 + (1-self.metabolism)*(self.grate)/100     

    def mtest(self):
        if self.velx != 0 and self.vely != 0:
            self.mflag = 1
        else:
            self.mflag = 0
    

    def normalize(self):
        total = np.sqrt(self.grate**2 + self.aggressiveness**2+self.attack**2+self.brate**2+self.drate**2+self.hunger**2+self.sight_norm**2+self.size_norm**2+self.stamina**2+self.metabolism**2+self.speed_norm**2)
        self.size /= total
        self.speed /= total
        self.stamina /= total
        self.attack /= total
        self.aggressiveness /= total
        self.metabolism /= total
        self.sight /= total
        self.hunger /= total
        self.brate /= total
        self.drate /= total
        self.grate /= total

    def __init__(self,x,y):
        self.size = np.random.uniform(low = 5.0,high = 50)
        self.size_norm = self.size/50.0
        self.speed = np.random.uniform(low = 0.0, high = 10.0)
        self.speed_norm = self.speed/10.0
        self.attack = np.random.uniform(low =0.0,high = 1.0)
        self.stamina = np.random.uniform(low = 0.0, high = 1.0)
        self.aggressiveness = np.random.uniform(low = 0.0, high = 1.0)
        self.metabolism = np.random.uniform(low = 0.0, high = 1.0)
        self.sight = np.random.uniform(low = 0.0, high = 200.0)
        self.sight_norm = self.sight/200.0
        self.grate = np.random.uniform(low = 0.0, high = 1.0)
        self.hunger = np.random.uniform(low = 0.0, high = 1.0)
        self.brate = np.random.uniform(low = 0.0, high = 1.0)
        self.drate = np.random.uniform(low = 0.0, high = 1.0)
        self.normalize()
        self.px = x
        self.py = y
        self.velx = 0
        self.vely = 0
        self.ax = 0
        self.ay = 0
        self.speed =math.sqrt(self.velx*self.velx+self.vely*self.vely)
        self.mtest()
        self.vthresh = self.speed

    
