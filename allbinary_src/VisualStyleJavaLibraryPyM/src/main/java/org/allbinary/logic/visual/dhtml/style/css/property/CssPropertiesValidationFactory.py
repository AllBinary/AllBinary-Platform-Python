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
# package org.allbinary.logic.visual.dhtml.style.css.property

from __future__ import annotations



class CssPropertiesValidationFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(nodeList: NodeList) -> BasicArrayList:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyData import CssPropertyData
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyValidationFactory import CssPropertyValidationFactory
        propertiesVector: BasicArrayList = BasicArrayListD()
        for index in range(0, nodeList.getLength()):
            node: Node = nodeList.item(index)
            if node.getNodeName().compareTo(CssPropertyData.getInstance().NAME) == 0:
                cssPropertyValidationInterface: ValidationInterface = CssPropertyValidationFactory.getInstance(node)
                propertiesVector.add(cssPropertyValidationInterface)
        return propertiesVector
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(hashMap: dict) -> BasicArrayList:
        styles: BasicArrayList = BasicArrayListD()
        return styles
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


