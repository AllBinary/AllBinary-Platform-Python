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

from java.lang.JavaRuntimeStatic import lazy_static


class AllBinaryEventObject:
    NULL_EVENT: AllBinaryEventObject = None

    def _init_fields(self) -> None:
        if "source" not in vars(self): self.source: object = None
    

    def __init__(self, anyType: object) -> None:
        from jsinterop.annotations.JsConstructor import JsConstructor
        __class__._init_fields(self)
        self.source = anyType
    

    def getSource(self) -> object:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.source
    

    def setSource(self, source: object) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        self.source = source
# from jsinterop.annotations.JsType import JsType
# from org.allbinary.logic.NullUtil import NullUtil
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsConstructor import JsConstructor
# from jsinterop.annotations.JsProperty import JsProperty


def _AllBinaryEventObject_NULL_EVENT() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return AllBinaryEventObject(NullUtil.getInstance().NULL_OBJECT)

lazy_static(AllBinaryEventObject, "NULL_EVENT", _AllBinaryEventObject_NULL_EVENT)

