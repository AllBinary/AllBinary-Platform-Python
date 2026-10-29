#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.layer

from __future__ import annotations

from org.allbinary.layer.Layer import Layer


class NullLayer(Layer):
    instance: NullLayer = None
    

    @staticmethod
    def getInstance() -> NullLayer:
        return NullLayer.instance
    

    def __init__(self) -> None:
        super().__init__(0, 0)
    

    def paint(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics


NullLayer.instance = NullLayer()

