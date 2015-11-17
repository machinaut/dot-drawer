#!/usr/bin/env python

import PIL
import PIL.Image
import PIL.ImageColor
import PIL.ImageDraw
import random

# 1/4, 3/8, 1/2, 5/8

def randcolor():
    r = random.random()
    if r < 0.25: return 0
    if r < 0.50: return 5
    if r < 0.75: return 10
    return 15

def getcolor(w, x, y):
    p = w.getpixel((x,y))[0]
    print p,
    if p < 50:  return 20.*3./4.
    if p < 100: return 20.*5./8.
    if p < 150: return 20.*1./2.
    if p < 200: return 20.*3./8.
    if p < 250: return 20.*1./4.
    return 0

size = (48*20, 24*20)  # given in 16ths of inches
white = PIL.ImageColor.getcolor('white', 'RGB')
black = PIL.ImageColor.getcolor('black', 'RGB')

im = PIL.Image.new('RGB', size, white)
w = PIL.Image.open('transformedworld6.png')
draw = PIL.ImageDraw.Draw(im)

for x in range(1,47):
    for y in range(1,23):
        r = int(round(getcolor(w,x-1,y-1)))
        x1 = (x * 20) - (r / 2)
        x2 = (x * 20) + (r / 2)
        y1 = (y * 20) - (r / 2)
        y2 = (y * 20) + (r / 2)
        draw.chord([x1,y1,x2,y2], 0, 360, black)

im.save('dot.jpg')
