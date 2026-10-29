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
# package org.allbinary.logic.util.event

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class AllBinaryEventObject:
    NULL_EVENT: AllBinaryEventObject = None

    def _init_fields(self) -> None:
        self.source: object = None
    

    def __init__(self, anyType: object) -> None:
        self._init_fields()
        self.source = anyType
    

    def getSource(self) -> object:
        return self.source
    

    def setSource(self, source: object) -> None:
        self.source = source
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from jsinterop.annotations.JsProperty import JsProperty


AllBinaryEventObject.NULL_EVENT = AllBinaryEventObject(NullUtil.getInstance().NULL_OBJECT)

