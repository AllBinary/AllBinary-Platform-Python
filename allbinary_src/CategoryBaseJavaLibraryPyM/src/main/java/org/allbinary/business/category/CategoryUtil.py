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
# package org.allbinary.business.category

from __future__ import annotations

import threading


class CategoryUtil:
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getPathLevel(categoryPath: AbPath) -> int:
        with CategoryUtil._lock:
            return CategoryUtil._getPathLevel_unlocked(categoryPath)

    @staticmethod
    def _getPathLevel_unlocked(categoryPath: AbPath) -> int:
        count: int = StringUtils.countMatches(str(categoryPath), AbPathData.getInstance().SEPARATOR)
        return count
    

    @staticmethod
    def getNameFromNode(node: Node) -> str:
        with CategoryUtil._lock:
            return CategoryUtil._getNameFromNode_unlocked(node)

    @staticmethod
    def _getNameFromNode_unlocked(node: Node) -> str:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.business.category.CategoryData import CategoryData
        attributes: NamedNodeMap = node.getAttributes()
        attrNode: Attr = attributes.getNamedItem(CategoryData.getInstance().LABEL)
        if attrNode is not None:
            return attrNode.getValue()
        else:
            labelNode: Node = DomSearchHelper.getNodeNoThrow(CategoryData.getInstance().LABEL, node.getChildNodes())
            if labelNode is not None:
                return DomNodeHelper.getTextNodeValue(labelNode)
        return StringUtil.getInstance().EMPTY_STRING
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringUtil import StringUtil
from org.apache.commons.lang3.StringUtils import StringUtils
from org.w3c.dom.Attr import Attr
from org.w3c.dom.NamedNodeMap import NamedNodeMap
from org.w3c.dom.Node import Node


