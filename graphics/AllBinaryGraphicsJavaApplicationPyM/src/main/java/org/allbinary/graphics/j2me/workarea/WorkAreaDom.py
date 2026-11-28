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



class WorkAreaDom:
    WORKAREA: str = "workArea"
    NAME: str = "name"
    FRAMES: str = "frames"

    def _init_fields(self) -> None:
        if "name" not in vars(self): self.name: str = None
        if "canvasNodeList" not in vars(self): self.canvasNodeList: BasicArrayList = None
    

    def __init__(self, document: Document) -> None:
        from org.allbinary.dom.DomHelper import DomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        __class__._init_fields(self)
        workAreaNodeList: NodeList = document.getElementsByTagName(WorkAreaDom.WORKAREA)
        if workAreaNodeList is not None:
            numberOfworkAreas: int = workAreaNodeList.getLength()
            if numberOfworkAreas == 1:
                numberOfNodes: int = workAreaNodeList.getLength()
                nameNode: Node = DomHelper.getInstance().searchNodeList(WorkAreaDom.NAME, workAreaNodeList.item(0).getChildNodes())
                nameTextNode: Node = nameNode.getFirstChild()
                self.name = nameTextNode.getNodeValue()
            else:
                raise Exception("Wrong Number of WorkAreas: " + str(numberOfworkAreas))
            self.canvasNodeList = DomHelper.getInstance().getChildrenWithoutTextNodes(WorkAreaDom.FRAMES, workAreaNodeList.item(0).getChildNodes())
        else:
            raise Exception("workArea Node Not Found")
    

    def getName(self) -> str:
        return self.name
    

    def getCanvasNodes(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.canvasNodeList
# from org.allbinary.dom.DomHelper import DomHelper
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


