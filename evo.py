#!/usr/bin/env python
import copy
import PIL
import PIL.Image
import PIL.ImageColor
import PIL.ImageDraw
import random

inch = 10
drills = [.0, .25, .325, .5, .625, .75]
size = (48*inch, 24*inch)
white = PIL.ImageColor.getcolor('white', 'RGB')
black = PIL.ImageColor.getcolor('black', 'RGB')
t = PIL.Image.open('transformedworld.png')

grid = [[0.0]*46 for i in range(22)]

def score(a, b, x, y):
    s = 0.0
    for x in range(x*inch,(x+2)*inch):
        for y in range(y*inch, (y*2)+inch):
            pa = a.getpixel((x,y))[0]
            pb = b.getpixel((x,y))[0]
            s += (pa - pb) ** 2
    return s

def render(grid):
    im = PIL.Image.new('RGB', size, white)
    draw = PIL.ImageDraw.Draw(im)
    for x in range(1,47):
        for y in range(1,23):
            d = grid[y-1][x-1] * inch
            x1 = int(round((x * inch) - (d / 2)))
            x2 = int(round((x * inch) + (d / 2)))
            y1 = int(round((y * inch) - (d / 2)))
            y2 = int(round((y * inch) + (d / 2)))
            draw.chord([x1,y1,x2,y2], 0, 360, black)
    return im

im = render(grid)

for i in range(1000):
    if i % 100 == 0: print i
    newgrid = copy.deepcopy(grid)
    x = random.randrange(46)
    y = random.randrange(22)
    d = random.choice(drills)
    newgrid[y][x] = d
    newim = render(newgrid)
    if score(newim, t, x, y) < score(im, t, x, y):
        grid = newgrid
        im = newim

im.save('evo.jpg')
print grid
