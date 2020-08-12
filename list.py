from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()

linel1 = []
linel2 = []
linel3 = []

for i in range(1,4):
    linel1.append(1*i)
    linel2.append(2*i)
    linel3.append(3*i)

x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,str(linel1),str(linel2),str(linel3))