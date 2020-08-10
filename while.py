from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
        x,y,z = mc.player.getTilePos()
        
        mc.postToChat("I'm watchimg youX:"+str(x)+"Y:"+str(y)+"Z"+str(z))
        time.sleep(3)