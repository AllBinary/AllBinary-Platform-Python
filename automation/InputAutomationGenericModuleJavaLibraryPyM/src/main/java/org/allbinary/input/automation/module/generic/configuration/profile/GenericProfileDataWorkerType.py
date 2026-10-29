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

from org.allbinary.input.media.image.InputImageType import InputImageType
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerTypeInterface import GenericProfileDataWorkerTypeInterface
from org.allbinary.input.automation.module.generic.configuration.profile.SavedCaptureGenericProfileDataWorkerType import SavedCaptureGenericProfileDataWorkerType


class GenericProfileDataWorkerType(GenericProfileDataWorkerTypeInterface):
    hashMap: dict = StdUtil.getInstance().createHashMap()
    SAVED_CAPTURE: GenericProfileDataWorkerType = SavedCaptureGenericProfileDataWorkerType.SAVED_CAPTURE
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
        node: Node = ModDomHelper.createTextNode(document, GenericProfileDataWorkerData.NAME, self.name)
        return node
    

    def toString(self) -> str:
        return "GenericProfileDataWorkerType: " + self.getName()

    def __str__(self) -> str:
        return self.toString()
    

    @staticmethod
    def getInstance(node: Node) -> GenericProfileDataWorkerType:
        name: str = DomNodeHelper.getTextNodeValue(node)
        return GenericProfileDataWorkerType.hashMap.get(name)
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


GenericProfileDataWorkerType.SCREEN_CAPTURE = GenericProfileDataWorkerType("Screen " + InputImageType.CAPTURE.getName())

GenericProfileDataWorkerType.COMPARISON = GenericProfileDataWorkerType(InputImageType.COMPARISON.getName())

GenericProfileDataWorkerType.MOTION = GenericProfileDataWorkerType(InputImageType.MOTION.getName())

