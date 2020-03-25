import sys
import pygame as pg 
import animal as a
import plant as p
import numpy as np
import timing as t

class roulette:
    def __init__(self,a):
        self.reproduce_vect = a.brate*a.drate*(1-a.grate)*(1-a.hunger)
        self.fight_vect = a.aggressiveness*a.attack*a.stamina*a.size_norm
        self.flight_vect = a.speed_norm*a.stamina*a.drate
        self.feed_vect = a.hunger*(1-a.stamina)*a.brate*a.grate
        total = self.reproduce_vect + self.feed_vect + self.flight_vect + self.fight_vect
        self.reproduce_p = self.reproduce_vect/total
        self.fight_p = self.fight_vect/total
        self.flight_p = self.flight_vect/total
        self.feed_p = self.feed_vect/total


    def update_roulette(self,a):
        self.reproduce_vect = a.brate*a.drate*(1-a.grate)*(1-a.hunger)
        self.fight_vect = a.aggressiveness*a.attack*a.stamina*a.size_norm
        self.flight_vect = a.speed_norm*a.stamina*a.drate
        self.feed_vect = 3*a.hunger*(1-a.stamina)*a.brate*a.grate
        total = self.reproduce_vect + self.feed_vect + self.flight_vect + self.fight_vect
        self.reproduce_p = self.reproduce_vect/total
        self.fight_p = self.fight_vect/total
        self.flight_p = self.flight_vect/total
        self.feed_p = self.feed_vect/total

    def spin_roulette(self):
        lim_rep = int(100*self.reproduce_p)
        lim_fight = lim_rep + int(100*self.fight_p)
        lim_flight = lim_fight + int(100*self.flight_p)
        lim_feed = lim_flight + int(100*self.feed_p)
        seed = np.random.randint(low = 0,high = 100)
        if(seed < lim_rep):
            return 0
        elif(seed > lim_rep and seed < lim_fight):
            return 1
        elif(seed > lim_fight and seed < lim_flight):
            return 2
        elif(seed > lim_flight and seed <= lim_feed):
            return 3
