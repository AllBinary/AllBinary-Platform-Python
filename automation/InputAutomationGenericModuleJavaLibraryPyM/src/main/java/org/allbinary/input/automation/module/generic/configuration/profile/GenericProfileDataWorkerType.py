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
# package org.allbinary.input.automation.module.generic.configuration.profile

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerTypeInterface import GenericProfileDataWorkerTypeInterface


class GenericProfileDataWorkerType(GenericProfileDataWorkerTypeInterface):
    hashMap: HashMap = None
    SAVED_CAPTURE: GenericProfileDataWorkerType = None
    SCREEN_CAPTURE: GenericProfileDataWorkerType = None
    COMPARISON: GenericProfileDataWorkerType = None
    MOTION: GenericProfileDataWorkerType = None

    def _init_fields(self) -> None:
        self.name: str = None
    

    def __init__(self, name: str) -> None:
        self._init_fields()
        self.setName(name)
        GenericProfileDataWorkerType.hashMap.put(self.getName(), self)
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerData import GenericProfileDataWorkerData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = ModDomHelper.createTextNode(document, GenericProfileDataWorkerData.NAME, self.name)
        return node
    

    def toString(self) -> str:
        return "GenericProfileDataWorkerType: " + self.getName()

    def __str__(self) -> str:
        return self.toString()
    

    @staticmethod
    def getInstance(node: Node) -> GenericProfileDataWorkerType:
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.w3c.dom.Node import Node
        name: str = DomNodeHelper.getTextNodeValue(node)
        return GenericProfileDataWorkerType.hashMap.get(name)
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.input.media.image.InputImageType import InputImageType
# from org.allbinary.logic.StdUtil import StdUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


def _GenericProfileDataWorkerType_hashMap() -> object:
    from java.util.HashMap import HashMap
    from org.allbinary.logic.StdUtil import StdUtil
    return StdUtil.getInstance().createHashMap()

lazy_static(GenericProfileDataWorkerType, "hashMap", _GenericProfileDataWorkerType_hashMap)

def _GenericProfileDataWorkerType_SAVED_CAPTURE() -> object:
    from org.allbinary.input.automation.module.generic.configuration.profile.SavedCaptureGenericProfileDataWorkerType import SavedCaptureGenericProfileDataWorkerType
    return SavedCaptureGenericProfileDataWorkerType.SAVED_CAPTURE

lazy_static(GenericProfileDataWorkerType, "SAVED_CAPTURE", _GenericProfileDataWorkerType_SAVED_CAPTURE)

def _GenericProfileDataWorkerType_SCREEN_CAPTURE() -> object:
    from org.allbinary.input.media.image.InputImageType import InputImageType
    return GenericProfileDataWorkerType("Screen " + InputImageType.CAPTURE.getName())

lazy_static(GenericProfileDataWorkerType, "SCREEN_CAPTURE", _GenericProfileDataWorkerType_SCREEN_CAPTURE)

def _GenericProfileDataWorkerType_COMPARISON() -> object:
    from org.allbinary.input.media.image.InputImageType import InputImageType
    return GenericProfileDataWorkerType(InputImageType.COMPARISON.getName())

lazy_static(GenericProfileDataWorkerType, "COMPARISON", _GenericProfileDataWorkerType_COMPARISON)

def _GenericProfileDataWorkerType_MOTION() -> object:
    from org.allbinary.input.media.image.InputImageType import InputImageType
    return GenericProfileDataWorkerType(InputImageType.MOTION.getName())

lazy_static(GenericProfileDataWorkerType, "MOTION", _GenericProfileDataWorkerType_MOTION)

