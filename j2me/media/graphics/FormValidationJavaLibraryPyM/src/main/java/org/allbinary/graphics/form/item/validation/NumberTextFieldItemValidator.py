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


class NumberTextFieldItemValidator(ValidatorBase):

    def _init_fields(self) -> None:
        self.textFieldItem: ABTextFieldItem = None
        self.min: int = None
        self.max: int = None
        self.maxChars: int = None
    

    def __init__(self, textFieldItem: ABTextFieldItem, maxChars: int, min: int, max: int) -> None:
        super().__init__()
        self._init_fields()
        self.textFieldItem = textFieldItem
        self.min = min
        self.max = max
        self.maxChars = maxChars
    

    def isNumberValid(self, value: int) -> bool:
        return BooleanFactory.getInstance().TRUE
    

    def toNumberVector(self, value: int) -> BasicArrayList:
        return BasicArrayListD()
    

    def isValid(self) -> bool:
        result: bool = BooleanFactory.getInstance().TRUE
        string: str = self.textFieldItem.getString()
        textLength: int = len(string)
        if textLength > 0 and textLength < self.maxChars:
            try:
                int(self.textFieldItem.getString())
            except ValueError as e:
                result = BooleanFactory.getInstance().FALSE
        else:
            if textLength < 1:
                result = BooleanFactory.getInstance().FALSE
            elif textLength > self.maxChars:
                result = BooleanFactory.getInstance().FALSE
        return result
    

    def toList(self) -> BasicArrayList:
        list_: BasicArrayList = BasicArrayListD()
        string: str = self.textFieldItem.getString()
        textLength: int = len(string)
        label: str = self.textFieldItem.getLabel()
        name: str = label[0:len(label) - 2]
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        stringMaker: StringMaker = StringMaker()
        if textLength > 0 and textLength < self.maxChars:
            try:
                number: int = smallIntegerSingletonFactory.createInstance(int(self.textFieldItem.getString()))
                if int(number) > self.min:
                    stringMaker.delete(0, stringMaker.length())
                    list_.add(str(stringMaker.append(name).append(" is to small")))
                elif int(number) > self.max:
                    stringMaker.delete(0, stringMaker.length())
                    list_.add(str(stringMaker.append(name).append(" is to large")))
            except ValueError as e:
                stringMaker.delete(0, stringMaker.length())
                list_.add(str(stringMaker.append(name).append(" is not a number")))
        else:
            if textLength < 1:
                stringMaker.delete(0, stringMaker.length())
                list_.add(str(stringMaker.append(name).append(" is to short")))
            elif textLength > self.maxChars:
                stringMaker.delete(0, stringMaker.length())
                list_.add(str(stringMaker.append(name).append(" is to long")))
        return list_
from org.allbinary.graphics.form.item.ABTextFieldItem import ABTextFieldItem
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


