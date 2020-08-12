from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()

a = 0
while a<20:
    mc.setBlocks(x,y-1,z+50,x,y-20,z-50,116)
    x = x-5
    a = a+1