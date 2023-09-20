from pico2d import *
import math
#math.cos(math.radians(90))
open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')

def recmove(x,y):
  while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x+2
    delay(0.001)
  while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y=y+2
    delay(0.001)
  while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x-2
    delay(0.001)
  while(y>90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y=y-2
    delay(0.001)
  while(x<400):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x+2
    delay(0.001)

def cirmove(x,y,z):
    while(z<360+270):
     clear_canvas_now()
     grass.draw_now(400,30)
     character.draw_now(x,y)
     x=400+210*math.cos(math.radians(z))
     y=300+210*math.sin(math.radians(z))
     z=1+z
     delay(0.001)
    

while(True):  
 recmove(400,90)
 cirmove(400,90,270)
close_canvas()
