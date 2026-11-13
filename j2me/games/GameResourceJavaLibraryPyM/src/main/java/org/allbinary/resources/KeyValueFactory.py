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
# package org.allbinary.resources

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class KeyValueFactory:
    instance: KeyValueFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.util.ABHashtable import ABHashtable
        self.MAP: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> KeyValueFactory:
        return KeyValueFactory.instance
    

    def get(self, key: str) -> str:
        if not self.MAP.containsKey(key):
            return key
        return self.MAP.get(key)
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.util.ABHashtable import ABHashtable


def _KeyValueFactory_instance() -> object:
    return KeyValueFactory()

lazy_static(KeyValueFactory, "instance", _KeyValueFactory_instance)

