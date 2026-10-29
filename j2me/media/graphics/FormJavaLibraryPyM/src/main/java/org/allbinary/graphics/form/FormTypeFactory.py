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
# package org.allbinary.graphics.form

from __future__ import annotations



class FormTypeFactory:
    instance: FormTypeFactory = None

    def _init_fields(self) -> None:
        self.UNK: str = "Unknown FormType"
        self.NULL_FORM_TYPE: FormType = FormType(StringUtil.getInstance().NULL_STRING)
        self.TEMP_HORIZONTAL_FORM: FormType = FormType("TempHorizontal")
        self.HORIZONTAL_FORM: FormType = FormType("Horizontal")
        self.VERTICAL_CENTER_FORM: FormType = FormType("Vertical")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FormTypeFactory:
        return FormTypeFactory.instance
    

    def getFormType(self) -> FormType:
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        formType: FormType = None
        if displayInfo.isPortrait():
            formType = self.VERTICAL_CENTER_FORM
        else:
            formType = self.HORIZONTAL_FORM
        return formType
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.graphics.form.FormType import FormType


FormTypeFactory.instance = FormTypeFactory()

