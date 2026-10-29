# Generated Code Do Not Modify
# package org.allbinary.game.collision

from __future__ import annotations

from org.allbinary.game.collision.CollisionProcessor import CollisionProcessor


class Collision2DProcessor(CollisionProcessor):

    def __init__(self) -> None:
        super().__init__()
    

    def isCollision(self, myLayer: AllBinaryLayer, myLayer2: AllBinaryLayer) -> bool:
        if myLayer2.getXP() >= myLayer.getX2() or myLayer2.getYP() >= myLayer.getY2() or myLayer2.getX2() <= myLayer.getXP() or myLayer2.getY2() <= myLayer.getYP():
            return False
        else:
            return True
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


