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

from org.allbinary.graphics.form.item.validation.TextFieldItemValidator import TextFieldItemValidator


class PasswordValidator(TextFieldItemValidator):
    

    def __init__(self, textFieldItem: ABTextFieldItem, min: int, max: int, allowOnEmpty: bool) -> None:
        super().__init__(textFieldItem, min, max, allowOnEmpty)
from org.allbinary.graphics.form.item.ABTextFieldItem import ABTextFieldItem


