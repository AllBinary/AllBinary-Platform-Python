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

from org.allbinary.logic.util.visitor.Visitor import Visitor


class TextItemNumberVisitor(Visitor):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def visit(self, anyType: object) -> object:
        value: str = anyType
        if len(value) < 2:
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if stringValidationUtil.isNumber(value):
                return BooleanFactory.getInstance().TRUE
            else:
                try:
                    TextNotificationUtil.getInstance().fireError("Numbers Only")
                except Exception as e:
                    commonStrings: CommonStrings = CommonStrings.getInstance()
                    self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.VISIT, e)
                return BooleanFactory.getInstance().FALSE
        else:
            return BooleanFactory.getInstance().FALSE
from org.allbinary.game.input.TextNotificationUtil import TextNotificationUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonStrings import CommonStrings


