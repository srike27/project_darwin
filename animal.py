import sys
import numpy as np
import math
import pygame as pg
import timing as t 
import roulette as r

class animal:

    def __init__(self,x,y,btime,parent = None):
        self.btime = btime
        if parent == None:
            self.size = np.random.uniform(low = 5.0,high = 50)
            self.size_norm = self.size/50.0
            self.size_cap = 50
            self.speed = np.random.uniform(low = 0.0, high = 10.0)
            self.speed_norm = self.speed/10.0
            self.attack = np.random.uniform(low =0.0,high = 1.0)
            self.stamina_cap = np.random.uniform(low = 0.0, high = 1.0)
            self.aggressiveness = np.random.uniform(low = 0.0, high = 1.0)
            self.metabolism = np.random.uniform(low = 0.0, high = 1.0)
            self.sight = np.random.uniform(low = 0.0, high = 200.0)
            self.sight_norm = self.sight/200.0
            self.grate = np.random.uniform(low = 0.0, high = 1.0)
            self.hunger = np.random.uniform(low = 0.0, high = 1.0)
            self.brate = np.random.uniform(low = 0.0, high = 1.0)
            self.drate = np.random.uniform(low = 0.0, high = 1.0)
        else:
            self.size = parent.size + np.random.normal(0.0,0.1)
            self.size_norm = self.size/50.0
            self.size_cap = 50
            self.speed = parent.speed + np.random.normal(0.0,0.1)
            self.speed_norm = self.speed/10.0
            self.attack = parent.attack + np.random.normal(0.0,0.1)
            self.stamina_cap = parent.stamina_cap + np.random.normal(0.0,0.1)
            self.aggressiveness = parent.aggressiveness + np.random.normal(0.0,0.1)
            self.metabolism = parent.metabolism + np.random.normal(0.0,0.1)
            self.sight = parent.sight + np.random.normal(0.0,0.1)
            self.sight_norm = self.sight/200.0
            self.grate = parent.grate + np.random.normal(0.0,0.1)
            self.hunger = parent.hunger + np.random.normal(0.0,0.1)
            self.brate = parent.brate + np.random.normal(0.0,0.1)
            self.drate = parent.drate + np.random.normal(0.0,0.1)
        self.erate = self.size/200
        self.stamina = self.stamina_cap * 5
        self.dtime = int(self.drate/(self.metabolism)*1000)
        self.action_time = int(50*self.stamina/self.metabolism)
        self.fat = 0.5
        if self.action_time < 50:
            self.action_time = 50
        a = t.timing(self.dtime,0,0)
        self.dtime = self.btime + a
        self.counter = 0
        #print(self.dtime.eons,self.dtime.days,self.dtime.ticks)
        self.normalize()
        self.px = x
        self.py = y
        self.velx = 0
        self.vely = 0
        self.ax = 0
        self.ay = 0
        self.wheel = r.roulette(self)

    def reproduce(self,wtime):
        angle = np.random.uniform(low = 0.0,high = 2 * np.pi)
        nx = self.px + 2*self.size*np.cos(angle)
        ny = self.py + 2*self.size*np.cos(angle)
        self.fat /= 1.5
        return animal(nx,ny,wtime,self)

    def animal_action(self,wtime):
        self.wheel.update_roulette(self)
        if self.counter == 0:
            self.decision = self.wheel.spin_roulette()
        if self.decision == 0:
            if self.counter == self.action_time - 1:
                print("!!!!!!!!!!!!!!!!ANIMAL BORN YEAAAAAAAAH!!!!!!!!!!!")
                return self.reproduce(wtime)
        if self.decision == 1:
            return None
        if self.decision == 2:
            return None
        if self.decision == 3:
            return None
    
    def __del__(self):
        print("animal has died")

    def updatestate(self):
        self.erate = self.size/200
        self.fat /= 1.01
        tmvx = self.velx
        tmvy = self.vely
        self.px += self.velx
        self.py += self.vely
        self.velx = self.stamina * (self.velx + self.ax)
        self.vely = self.stamina * (self.vely + self.ay)
        self.cspd =math.sqrt(self.velx*self.velx+self.vely*self.vely)
        if self.fat < 0.1:
            self.dtime = self.dtime - t.timing(ticks = 10,days = 0,eons = 0)
        if self.cspd > self.speed:
            self.velx = self.velx/self.cspd*self.speed
            self.vely = self.vely/self.cspd*self.speed
        if self.cspd > 1:
            self.stamina /= 1.001
        if self.cspd <= 1:
            self.stamina *= 1.001
            if self.stamina > self.stamina_cap*5:
                self.stamina = self.stamina_cap*5
        if self.ax==0:
            self.velx = tmvx
        if self.ay==0:
            self.vely = tmvy
        self.counter += 1
        if self.counter == self.action_time:
            self.counter = 0 

    def impulse(self,acx,acy):
        self.ax = acx
        self.ay = acy
        self.updatestate()
        self.ax = 0
        self.ay = 0

    def grow(self):
        if self.size <= self.size_cap:
            self.fat *= 1.1
            if self.fat > 1:
                self.fat = 1
            self.size *= 1 + (1-self.metabolism)*(self.grate)/100

    def normalize(self):
        total = np.sqrt(self.grate**2 + self.aggressiveness**2+self.attack**2+self.brate**2+self.drate**2+self.hunger**2+self.sight_norm**2+self.size_norm**2+self.stamina_cap**2+self.metabolism**2+self.speed_norm**2)
        self.size /= total
        self.speed /= total
        self.stamina_cap /= total
        self.attack /= total
        self.aggressiveness /= total
        self.metabolism /= total
        self.sight /= total
        self.hunger /= total
        self.brate /= total
        self.drate /= total
        self.grate /= total
