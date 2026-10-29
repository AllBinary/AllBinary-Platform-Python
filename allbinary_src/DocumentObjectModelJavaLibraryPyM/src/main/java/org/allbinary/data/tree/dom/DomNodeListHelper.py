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
# package org.allbinary.data.tree.dom

from __future__ import annotations



class DomNodeListHelper:
    

    @staticmethod
    def getVector(nodeList: NodeList) -> BasicArrayList:
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        vector: BasicArrayList = BasicArrayListD()
        size: int = nodeList.getLength()
        for index in range(0, size):
            vector.add(DomNodeHelper.getTextNodeValue(nodeList.item(index)))
        return vector
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.w3c.dom.NodeList import NodeList


