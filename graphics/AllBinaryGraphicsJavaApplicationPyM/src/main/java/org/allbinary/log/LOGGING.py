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
# package org.allbinary.log

from __future__ import annotations

from org.allbinary.util.BasicArrayListD import BasicArrayListD


class LOGGING:
    logging: BasicArrayList = BasicArrayListD()
    GRAPHICSPAINT: LOGGING = None
    GRAPHICSCREATION: LOGGING = None
    GRAPHICSDELETION: LOGGING = None
    LOADINGERROR: LOGGING = None
    MENUEVENT: LOGGING = None
    MOUSEEVENT: LOGGING = None
    KEYEVENT: LOGGING = None
    ACTIONEVENT: LOGGING = None
    ADJUSTMENTEVENT: LOGGING = None
    COMPONENTEVENT: LOGGING = None
    CONTAINEREVENT: LOGGING = None
    FOCUSEVENT: LOGGING = None
    HIERARCHYEVENT: LOGGING = None
    INPUTEVENT: LOGGING = None
    INVOCATIONEVENT: LOGGING = None
    ITEMEVENT: LOGGING = None
    PAINTEVENT: LOGGING = None
    TEXTEVENT: LOGGING = None
    WINDOWEVENT: LOGGING = None

    def _init_fields(self) -> None:
        self.name: str = None
    

    def __init__(self, value: str) -> None:
        self._init_fields()
        self.name = value
        self.LOGGING.logging.add(value)
    

    @staticmethod
    def contains(logType: LOGGING) -> bool:
        return self.LOGGING.logging.contains(str(logType))
    

    def toString(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.StdUtil import StdUtil


LOGGING.GRAPHICSPAINT = LOGGING("Graphics Paint")

LOGGING.GRAPHICSCREATION = LOGGING("Graphics Creation")

LOGGING.GRAPHICSDELETION = LOGGING("Graphics Deletion")

LOGGING.LOADINGERROR = LOGGING("Loading Error")

LOGGING.MENUEVENT = LOGGING("Menu Action Event")

LOGGING.MOUSEEVENT = LOGGING("Mouse Action Event")

LOGGING.KEYEVENT = LOGGING("Keyboard Action Event")

LOGGING.ACTIONEVENT = LOGGING("Action Event")

LOGGING.ADJUSTMENTEVENT = LOGGING("Adjustment Action Event")

LOGGING.COMPONENTEVENT = LOGGING("Component Action Event")

LOGGING.CONTAINEREVENT = LOGGING("Container Action Event")

LOGGING.FOCUSEVENT = LOGGING("Focus Action Event")

LOGGING.HIERARCHYEVENT = LOGGING("Hierarchy Action Event")

LOGGING.INPUTEVENT = LOGGING("Input Action Event")

LOGGING.INVOCATIONEVENT = LOGGING("Invocation Action Event")

LOGGING.ITEMEVENT = LOGGING("Item Action Event")

LOGGING.PAINTEVENT = LOGGING("Paint Action Event")

LOGGING.TEXTEVENT = LOGGING("Text Action Event")

LOGGING.WINDOWEVENT = LOGGING("Window Action Event")

