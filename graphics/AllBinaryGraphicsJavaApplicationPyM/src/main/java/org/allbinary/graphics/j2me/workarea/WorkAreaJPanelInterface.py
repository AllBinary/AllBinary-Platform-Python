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
# package org.allbinary.graphics.j2me.workarea

from __future__ import annotations

from org.allbinary.graphics.j2me.workarea.KeyListener import KeyListener


# Java interface
class WorkAreaJPanelInterface(KeyListener):
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def deselect(self) -> None:
        raise NotImplementedError()
    

    def select(self) -> None:
        raise NotImplementedError()
    

    def changeZoom(self, factor: int) -> None:
        raise NotImplementedError()
    

    def explodeAll(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def autoRotate(self, increments: int, totalAngle: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def autoExplode(self, numberOfFrames: int, explodeType: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def autoMirror(self) -> None:
        raise NotImplementedError()
    

    def play(self) -> None:
        raise NotImplementedError()
    

    def stop(self) -> None:
        raise NotImplementedError()
    

    def isPlaying(self) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def toDocument(self) -> Document:
        raise NotImplementedError()
from org.w3c.dom.Document import Document


