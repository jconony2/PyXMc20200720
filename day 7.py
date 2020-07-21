# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:25:53 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()


X,Y,Z = mc.player.getTilePos()

mc.setBlock(X+1,Y,Z,169)
mc.setBlock(X-1,Y,Z,169)
mc.setBlock(X,Y,Z+1,169)
mc.setBlock(X,Y,Z-1,169)
mc.setBlock(X+1,Y,Z+1,169)
mc.setBlock(X-1,Y,Z+1,169)
mc.setBlock(X+1,Y,Z-1,169)
mc.setBlock(X-1,Y,Z-1,169)









