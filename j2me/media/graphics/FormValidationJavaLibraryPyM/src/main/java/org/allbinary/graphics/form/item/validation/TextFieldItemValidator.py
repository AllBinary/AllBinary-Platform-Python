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
# package org.allbinary.graphics.form.item.validation

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidatorBase import ValidatorBase


class TextFieldItemValidator(ValidatorBase):

    def _init_fields(self) -> None:
        self.textFieldItem: ABTextFieldItem = None
        self.min: int = None
        self.max: int = None
        self.allowOnEmpty: bool = None
    

    def __init__(self, textFieldItem: ABTextFieldItem, min: int, max: int, allowOnEmpty: bool) -> None:
        super().__init__()
        self._init_fields()
        self.textFieldItem = textFieldItem
        self.min = min
        self.max = max
        self.allowOnEmpty = allowOnEmpty
    

    def isValid(self) -> bool:
        booleanFactory: BooleanFactory = BooleanFactory.getInstance()
        result: bool = booleanFactory.TRUE
        string: str = self.textFieldItem.getString()
        textLength: int = len(string)
        if (textLength == 0 and self.allowOnEmpty) or textLength > self.min and textLength < self.max:
            pass
        else:
            if textLength < self.min:
                result = booleanFactory.FALSE
            elif textLength > self.max:
                result = booleanFactory.FALSE
        return result
    

    def toList(self) -> BasicArrayList:
        list_: BasicArrayList = BasicArrayListD()
        string: str = self.textFieldItem.getString()
        textLength: int = len(string)
        if textLength > self.min and textLength < self.max:
            pass
        else:
            label: str = self.textFieldItem.getLabel()
            name: str = label[0:len(label) - 2]
            if textLength < self.min:
                list_.add(str(StringMaker().append(name).append(" is to short")))
            elif textLength > self.max:
                list_.add(str(StringMaker().append(name).append(" is to long")))
        return list_
from org.allbinary.graphics.form.item.ABTextFieldItem import ABTextFieldItem
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


