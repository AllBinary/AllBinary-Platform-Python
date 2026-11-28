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



class MyCanvasEventSource:

    def _init_fields(self) -> None:
        if "command" not in vars(self): self.command: str = None
        if "treeNode" not in vars(self): self.treeNode: MutableTreeNode = None
        self.angle: float = 0.0

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__._constructor2(self, *args)
        elif len(args) == 3:
            __class__._constructor3(self, *args)
    

    def _constructor2(self, command: str, treeNode: MutableTreeNode) -> None:
        __class__._init_fields(self)
        self.command = command
        self.treeNode = treeNode
    

    def _constructor3(self, command: str, angle: float, treeNode: MutableTreeNode) -> None:
        __class__._init_fields(self)
        self.command = command
        self.treeNode = treeNode
        self.setAngle(angle)
    

    def getCommand(self) -> str:
        return self.command
    

    def getTreeNode(self) -> MutableTreeNode:
        return self.treeNode
    

    def getAngle(self) -> float:
        return self.angle
    

    def setAngle(self, angle: float) -> None:
        self.angle = angle
# from javax.swing.tree.MutableTreeNode import MutableTreeNode


