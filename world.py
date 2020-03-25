import sys
import pygame as pg 
import animal as a
import plant as p
import numpy as np
import timing as t


def run_game():
    worldtime = t.timing(ticks = 0,days = 0,eons = 0)
    population = 100
    vegetation = 10
    xlist = np.random.uniform(0,1920,population)
    ylist = np.random.uniform(0,1080,population)
    xplist = np.random.uniform(0,1920,vegetation)
    yplist = np.random.uniform(0,1080,vegetation)
    animals = []
    plants = []
    for i in range(population):
        animals.append(a.animal(int(xlist[i]),int(ylist[i]),worldtime))
    for i in range(vegetation):
        plants.append(p.plant(int(xplist[i]),int(yplist[i]),0.01))
    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((1920,1080))  #comment out for fast sim
    pg.display.set_caption("first screen")  #comment out for fast sim
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))  #comment out for fast sim
        color = (255, 100, 0)
        for i in range(vegetation):
            plants[i].grow()
            for j in range(population):
                dist = np.sqrt((plants[i].x - animals[j].px)**2+(plants[i].y - animals[j].py)**2)
                if dist <= (plants[i].size + animals[j].size):
                    plants[i].eaten(animals[j].erate)
                    animals[j].grow()
            pg.draw.circle(screen, (100,255,0),[int(round(plants[i].x)),int(round(plants[i].y))],int(plants[i].size),0) #comment out for fast sim
        kill_plant_list = []
        kill_animal_list = []
        for i in range(vegetation):
            if (plants[i].size < 1):
                kill_plant_list.append(i)
        for plnt in kill_plant_list:
            plants.pop(plnt)
        newanimlist = [] 
        for i in range(population):
            print(animals[i].dtime.days)
            x = (animals[i].px)
            y = (animals[i].py)
            if (x>1920-animals[i].size or x<animals[i].size):
                animals[i].velx = -int(0.5*animals[i].velx)
                if(x>1920 -animals[i].size):
                    animals[i].px = 1920 - animals[i].size
                else: animals[i].px = animals[i].size
            if (y>1080 -animals[i].size or y<animals[i].size):
                animals[i].vely = -int(0.5*animals[i].vely)
                if(y>1080-animals[i].size):
                    animals[i].py = 1080 -animals[i].size
                else: animals[i].py = animals[i].size  
            #animals do something here for now random motion
            newanim = animals[i].animal_action(worldtime)
            if newanim is not None:
                newanimlist.append(newanim)
            animals[i].impulse(np.random.normal(0.0,0.1),np.random.normal(0.0,0.1))
            if (worldtime > animals[i].dtime):
                kill_animal_list.append(i)
            pg.draw.circle(screen, color,[int(round(animals[i].px)),int(round(animals[i].py))],int(animals[i].size),0)  #comment out for fast sim
        animals = animals + newanimlist
        for anml in kill_animal_list:
            animals.pop(anml)
        vegetation = len(plants)
        population = len(animals)
        pg.display.flip()  #comment out for fast sim
        worldtime.next()
        clock.tick(30)

run_game()
