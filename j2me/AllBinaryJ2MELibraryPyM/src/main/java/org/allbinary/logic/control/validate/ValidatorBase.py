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
# package org.allbinary.logic.control.validate

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.control.validate.ValidatorBaseInterface import ValidatorBaseInterface


class ValidatorBase(ValidatorBaseInterface):
    instance: ValidatorBase = None
    

    @staticmethod
    def getInstance() -> ValidatorBase:
        return ValidatorBase.instance
    

    def __init__(self) -> None:
        pass
    

    def isValid(self) -> bool:
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        return BooleanFactory.getInstance().TRUE
    

    def validationInfo(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().EMPTY_STRING
    

    def toHashtable(self) -> ABHashtable[object, object]:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.util.ABHashtable import ABHashtable
        return StdUtil.getInstance().NULL_TABLE
    

    def toList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        return BasicArrayListUtil.getInstance().getImmutableInstance()
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
# from org.allbinary.util.ABHashtable import ABHashtable


def _ValidatorBase_instance() -> object:
    return ValidatorBase()

lazy_static(ValidatorBase, "instance", _ValidatorBase_instance)

