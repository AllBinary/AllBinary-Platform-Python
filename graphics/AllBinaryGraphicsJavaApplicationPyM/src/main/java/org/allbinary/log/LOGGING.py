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

from java.lang.JavaRuntimeStatic import lazy_static


class LOGGING:
    logging: BasicArrayList = None
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
        if "name" not in vars(self): self.name: str = None
    

    def __init__(self, value: str) -> None:
        __class__._init_fields(self)
        self.name = value
        LOGGING.logging.add(value)
    

    @staticmethod
    def contains(logType: LOGGING) -> bool:
        return LOGGING.logging.contains(str(logType))
    

    def toString(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil


def _LOGGING_logging() -> object:
    from org.allbinary.util.BasicArrayList import BasicArrayList
    from org.allbinary.util.BasicArrayListD import BasicArrayListD
    return BasicArrayListD()

lazy_static(LOGGING, "logging", _LOGGING_logging)

def _LOGGING_GRAPHICSPAINT() -> object:
    return LOGGING("Graphics Paint")

lazy_static(LOGGING, "GRAPHICSPAINT", _LOGGING_GRAPHICSPAINT)

def _LOGGING_GRAPHICSCREATION() -> object:
    return LOGGING("Graphics Creation")

lazy_static(LOGGING, "GRAPHICSCREATION", _LOGGING_GRAPHICSCREATION)

def _LOGGING_GRAPHICSDELETION() -> object:
    return LOGGING("Graphics Deletion")

lazy_static(LOGGING, "GRAPHICSDELETION", _LOGGING_GRAPHICSDELETION)

def _LOGGING_LOADINGERROR() -> object:
    return LOGGING("Loading Error")

lazy_static(LOGGING, "LOADINGERROR", _LOGGING_LOADINGERROR)

def _LOGGING_MENUEVENT() -> object:
    return LOGGING("Menu Action Event")

lazy_static(LOGGING, "MENUEVENT", _LOGGING_MENUEVENT)

def _LOGGING_MOUSEEVENT() -> object:
    return LOGGING("Mouse Action Event")

lazy_static(LOGGING, "MOUSEEVENT", _LOGGING_MOUSEEVENT)

def _LOGGING_KEYEVENT() -> object:
    return LOGGING("Keyboard Action Event")

lazy_static(LOGGING, "KEYEVENT", _LOGGING_KEYEVENT)

def _LOGGING_ACTIONEVENT() -> object:
    return LOGGING("Action Event")

lazy_static(LOGGING, "ACTIONEVENT", _LOGGING_ACTIONEVENT)

def _LOGGING_ADJUSTMENTEVENT() -> object:
    return LOGGING("Adjustment Action Event")

lazy_static(LOGGING, "ADJUSTMENTEVENT", _LOGGING_ADJUSTMENTEVENT)

def _LOGGING_COMPONENTEVENT() -> object:
    return LOGGING("Component Action Event")

lazy_static(LOGGING, "COMPONENTEVENT", _LOGGING_COMPONENTEVENT)

def _LOGGING_CONTAINEREVENT() -> object:
    return LOGGING("Container Action Event")

lazy_static(LOGGING, "CONTAINEREVENT", _LOGGING_CONTAINEREVENT)

def _LOGGING_FOCUSEVENT() -> object:
    return LOGGING("Focus Action Event")

lazy_static(LOGGING, "FOCUSEVENT", _LOGGING_FOCUSEVENT)

def _LOGGING_HIERARCHYEVENT() -> object:
    return LOGGING("Hierarchy Action Event")

lazy_static(LOGGING, "HIERARCHYEVENT", _LOGGING_HIERARCHYEVENT)

def _LOGGING_INPUTEVENT() -> object:
    return LOGGING("Input Action Event")

lazy_static(LOGGING, "INPUTEVENT", _LOGGING_INPUTEVENT)

def _LOGGING_INVOCATIONEVENT() -> object:
    return LOGGING("Invocation Action Event")

lazy_static(LOGGING, "INVOCATIONEVENT", _LOGGING_INVOCATIONEVENT)

def _LOGGING_ITEMEVENT() -> object:
    return LOGGING("Item Action Event")

lazy_static(LOGGING, "ITEMEVENT", _LOGGING_ITEMEVENT)

def _LOGGING_PAINTEVENT() -> object:
    return LOGGING("Paint Action Event")

lazy_static(LOGGING, "PAINTEVENT", _LOGGING_PAINTEVENT)

def _LOGGING_TEXTEVENT() -> object:
    return LOGGING("Text Action Event")

lazy_static(LOGGING, "TEXTEVENT", _LOGGING_TEXTEVENT)

def _LOGGING_WINDOWEVENT() -> object:
    return LOGGING("Window Action Event")

lazy_static(LOGGING, "WINDOWEVENT", _LOGGING_WINDOWEVENT)

