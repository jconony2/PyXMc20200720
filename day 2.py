# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:00:17 2020

@author: user

"""
X = 100
Y = 100
Z = 100
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.player.setTilePos(X,Y,Z)