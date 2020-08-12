import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
l=50
w=30
h=20
x,y,z = mc.player.getTilePos()

x1=x+l
y1=y+h
z1=z+w

mc.setBlocks(x,y,z,x1,y1,z1,57)
mc.setBlocks(x+1,y+1,z+1,x1-1,y1-1,z1-1,0)

