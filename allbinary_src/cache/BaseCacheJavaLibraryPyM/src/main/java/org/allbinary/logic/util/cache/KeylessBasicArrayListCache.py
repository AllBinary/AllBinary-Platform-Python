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
# package org.allbinary.logic.util.cache

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.util.cache.IndexedBasicArrayListCache import IndexedBasicArrayListCache


@java_inherited_overloads
class KeylessBasicArrayListCache(IndexedBasicArrayListCache):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicArrayListUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def get(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        try:
            if self.index >= self.list_.size():
                self.addDefault()
            list_: BasicArrayList = self.getAt(((setattr(self, "index", self.index + 1) or self.index) - 1))
            return list_
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET, e)
            return self.basicArrayListUtil.getImmutableInstance()
    

    def clear(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        java_super_call(super(), "clear")
        basicArrayList: BasicArrayList = None
        for index in range(self.list_.size() - 1, 0 - 1, -1):
            basicArrayList = (self.list_.objectArray[index])
            basicArrayList.clear()
    

    def log(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.util.BasicArrayList import BasicArrayList
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("S: ")
        stringBuffer.appendint(self.list_.size())
        S_LABEL: str = " s: "
        basicArrayList: BasicArrayList = None
        for index in range(self.list_.size() - 1, 0 - 1, -1):
            stringBuffer.append(S_LABEL)
            basicArrayList = (self.list_.objectArray[index])
            stringBuffer.appendint(basicArrayList.size())
        return str(stringBuffer)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


