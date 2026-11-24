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
# package org.allbinary.data.tables

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class TableDataFactory:
    instance: TableDataFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        self.INTEGER_MAX_VALUE_STRING: str = str(2147483647)
        self.ZERO_STRING: str = CommonPhoneStrings.getInstance().ZERO

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TableDataFactory:
        return TableDataFactory.instance
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings


def _TableDataFactory_instance() -> object:
    return TableDataFactory()

lazy_static(TableDataFactory, "instance", _TableDataFactory_instance)

