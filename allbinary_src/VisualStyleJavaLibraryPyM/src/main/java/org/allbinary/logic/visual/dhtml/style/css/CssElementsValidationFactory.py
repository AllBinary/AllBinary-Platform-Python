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
# package org.allbinary.logic.visual.dhtml.style.css

from __future__ import annotations



class CssElementsValidationFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def getInstance_j1_1(cssElementStyleNodeList: BasicArrayList) -> BasicArrayList:
        from org.allbinary.logic.visual.dhtml.style.css.CssElementValidationFactory import CssElementValidationFactory
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
        from org.w3c.dom.Node import Node
        styles: BasicArrayList = BasicArrayListD()
        size: int = cssElementStyleNodeList.size()
        cssElementStyleNode: Node = None
        cssValidationInterface: ValidationInterface = None
        for index in range(0, size):
            cssElementStyleNode = cssElementStyleNodeList.get(index)
            cssValidationInterface = CssElementValidationFactory.getInstance(cssElementStyleNode)
            styles.add(cssValidationInterface)
        return styles
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def getInstance_j1_2(hashMap: HashMap) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        styles: BasicArrayList = BasicArrayListD()
        return styles

    @staticmethod
    def getInstance(*args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "BasicArrayList" for base in type(args[0]).__mro__)):
            return CssElementsValidationFactory.getInstance_j1_1(*args)
        if len(args) == 1:
            return CssElementsValidationFactory.getInstance_j1_2(*args)
        return getattr(CssElementsValidationFactory, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
# from org.w3c.dom.Node import Node


