#
# AllBinary Open License Version 1
# Copyright (c) 2022 AllBinary
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
# package org.allbinary.graphics.displayable.screen

from __future__ import annotations



class AboutPaintableFactory:
    instance: AboutPaintableFactory = None

    def _init_fields(self) -> None:
        self.paintableArray: list[Paintable] = [NullPaintable.getInstance()]
    

    @staticmethod
    def getInstance() -> AboutPaintableFactory:
        return AboutPaintableFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
        INFO: list[str] = ["Built with the", "AllBinary Platform", StringUtil.getInstance().EMPTY_STRING, "Comments or Questions:", "support@allbinary.com"]
        DEVELOPERS: list[str] = ["Developed By:", "Travis Berthelot"]
        self.paintableArray = AboutPaintable.getInstance(INFO, DEVELOPERS).getPaintableArrayInstance()
from org.allbinary.game.paint.AboutPaintable import AboutPaintable
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.logic.string.StringUtil import StringUtil


AboutPaintableFactory.instance = AboutPaintableFactory()

