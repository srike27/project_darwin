import sys
import pygame as pg 
import animal as a
import plant as p
import numpy as np


def run_game():
    population = 10
    vegetation = 10
    xlist = np.random.uniform(0,1920,population)
    ylist = np.random.uniform(0,1080,population)
    xplist = np.random.uniform(0,1920,population)
    yplist = np.random.uniform(0,1080,population)
    animals = []
    plants = []
    for i in range(population):
        animals.append(a.animal(int(xlist[i]),int(ylist[i])))
    for i in range(vegetation):
        plants.append(p.plant(int(xplist[i]),int(yplist[i]),0.01))
    done = False
    is_blue = False
    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((1920,1080))
    pg.display.set_caption("first screen")
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        for i in range(vegetation):
            plants[i].grow()
            for j in range(population):
                dist = np.sqrt((plants[i].x - animals[j].px)**2+(plants[i].y - animals[j].py)**2)
                if dist <= (plants[i].size + animals[j].size):
                    plants[i].eaten()
                    animals[j].grow()
            pg.draw.circle(screen, (100,255,0),[int(round(plants[i].x)),int(round(plants[i].y))],int(plants[i].size),0)
        for i in range(population):
            x = (animals[i].px)
            y = (animals[i].py)
            if (x>1920-animals[i].size or x<animals[i].size):
                animals[i].velx = -int(0.5*animals[i].velx)
                #animals[i].ax = -1*animals[i].ax
                if(x>1920 -animals[i].size):
                    animals[i].px = 1920 - animals[i].size
                else: animals[i].px = animals[i].size
            if (y>1080 -animals[i].size or y<animals[i].size):
                animals[i].vely = -int(0.5*animals[i].vely)
                #animals[i].ay =-1*animals[i].ay
                if(y>1080-animals[i].size):
                    animals[i].py = 1080 -animals[i].size
                else: animals[i].py = animals[i].size  
            animals[i].impulse(np.random.normal(0.0,0.1),np.random.normal(0.0,0.1))
            pg.draw.circle(screen, color,[int(round(animals[i].px)),int(round(animals[i].py))],int(animals[i].size),0)
        pg.display.flip()
        clock.tick(30)

run_game()
