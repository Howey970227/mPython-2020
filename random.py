import time,random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
time.sleep(3)

x,y,z = mc.player.getTilePos()

color = random.randrange(0,16)
mc.setBlocks(x+50, y-1, z+50, x-50, y-1, z-50, 95,color)