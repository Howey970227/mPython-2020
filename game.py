from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x+i
    for J in range(10):
        r = random.randrange(0,16)
        z = z+1
        mc.setBlock(x,y,z,35,r)

ans = random.randrange(1,16)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
         hit = hits[0]
         block = mc.getBlockWithData(hit.pos)
         data = block.data
         if data == ans :
             mc.postToChat('喔~好棒棒')
             mc.setBlock(hit.pos,11)
         else:
            mc.postToChat('恭喜猜錯')