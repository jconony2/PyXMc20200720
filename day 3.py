# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:32:53 2020

@author: user
"""
X = 80.112233
Y = 180.112233
Z = 80.112233



from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.player.setPos(X,Y,Z)