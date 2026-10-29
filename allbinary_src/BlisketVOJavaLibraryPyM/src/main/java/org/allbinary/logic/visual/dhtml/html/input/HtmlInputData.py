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
# package org.allbinary.logic.visual.dhtml.html.input

from __future__ import annotations



class HtmlInputData:
    instance: HtmlInputData = None

    def _init_fields(self) -> None:
        self.TEXT: str = "text"
        self.RADIO: str = "radio"
        self.CHECKBOX: str = "checkbox"
        self.HIDDEN: str = "hidden"
        self.IMAGE: str = "image"
        self.PASSWORD: str = "password"
        self.RESET: str = "reset"
        self.SUBMIT: str = "submit"
        self.TYPES: list[str] = [self.TEXT, self.RADIO, self.CHECKBOX, self.HIDDEN, self.IMAGE, self.PASSWORD, self.RADIO, self.RESET, self.SUBMIT]

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> HtmlInputData:
        return HtmlInputData.instance


HtmlInputData.instance = HtmlInputData()

