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
# package org.allbinary.graphics.j2me.workarea.canvas.event

from __future__ import annotations

from org.allbinary.graphics.j2me.workarea.canvas.event.EventObject import EventObject


class MyCanvasEvent(EventObject):
    

    def __init__(self, source: object) -> None:
        super().__init__(source)
    

    def getSource(self) -> object:
        return super().getSource()
    

    def toString(self) -> str:
        return str(super())

    def __str__(self) -> str:
        return self.toString()
    

    def getCommand(self) -> str:
        myEventSource: MyCanvasEventSource = self.getSource()
        return myEventSource.getCommand()
    

    def getTreeNode(self) -> MutableTreeNode:
        myEventSource: MyCanvasEventSource = self.getSource()
        return myEventSource.getTreeNode()
    

    def getAngle(self) -> float:
        myEventSource: MyCanvasEventSource = self.getSource()
        return myEventSource.getAngle()
# from javax.swing.tree.MutableTreeNode import MutableTreeNode


