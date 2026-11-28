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
# package org.allbinary.logic.control.contraints.display.browser

from __future__ import annotations

from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface


class DisplayInBrowserContraints(DisplayInBrowserContraintsInterface):

    def _init_fields(self) -> None:
        if "frameable" not in vars(self): self.frameable: bool = False
        if "mountable" not in vars(self): self.mountable: bool = False
        if "quickFrameable" not in vars(self): self.quickFrameable: bool = False
        if "mountedLink" not in vars(self): self.mountedLink: str = None
    

    def __init__(self, node: Node) -> None:
        from org.w3c.dom.Node import Node
        __class__._init_fields(self)
    

    def isMountable(self) -> bool:
        return self.mountable
    

    def setMountable(self, mountable: bool) -> None:
        self.mountable = mountable
    

    def isFrameable(self) -> bool:
        return self.frameable
    

    def setFrameable(self, frameable: bool) -> None:
        self.frameable = frameable
    

    def isQuickFrameable(self) -> bool:
        return self.quickFrameable
    

    def setQuickFrameable(self, quickFrameable: bool) -> None:
        self.quickFrameable = quickFrameable
    

    def getMountedLink(self) -> str:
        return self.mountedLink
    

    def setMountedLink(self, mountedLink: str) -> None:
        self.mountedLink = mountedLink
# from org.w3c.dom.Node import Node


