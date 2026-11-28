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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.control.validate.ValidatorBase import ValidatorBase


@java_inherited_overloads
class TextFieldItemValidator(ValidatorBase):
    def _java_defaults(self):
        vars(self).setdefault("textFieldItem", None)
        vars(self).setdefault("min", 0)
        vars(self).setdefault("max", 0)
        vars(self).setdefault("allowOnEmpty", False)

    def _init_fields(self) -> None:
        if "textFieldItem" not in vars(self): self.textFieldItem: ABTextFieldItem = None
        if "min" not in vars(self): self.min: int = 0
        if "max" not in vars(self): self.max: int = 0
        if "allowOnEmpty" not in vars(self): self.allowOnEmpty: bool = False
    

    def __init__(self, textFieldItem: ABTextFieldItem, min: int, max: int, allowOnEmpty: bool) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.form.item.ABTextFieldItem import ABTextFieldItem
        super().__init__()
        __class__._init_fields(self)
        self.textFieldItem = textFieldItem
        self.min = min
        self.max = max
        self.allowOnEmpty = allowOnEmpty
    

    def isValid(self) -> bool:
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
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
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
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
# from org.allbinary.graphics.form.item.ABTextFieldItem import ABTextFieldItem
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


