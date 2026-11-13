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
# package org.allbinary.string

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class CommonSeps:
    instance: CommonSeps = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from jsinterop.annotations.JsProperty import JsProperty
        self.NEW_LINE: str = "\n"
        self.SEMICOLON: str = ";"
        self.EQUALS: str = "="
        self.SPACE: str = " "
        self.COMMA: str = ","
        self.COLON: str = ":"
        self.PERIOD: str = "."
        self.UNDERSCORE: str = "_"
        self.COLON_SEP: str = str(StringMaker().append(self.COLON).append(self.SPACE))
        self.COMMA_SEP: str = str(StringMaker().append(self.COMMA).append(self.SPACE))
        self.PARENTHESIS_OPEN: str = "("
        self.PARENTHESIS_CLOSE: str = ")"
        self.BRACE_OPEN: str = "{"
        self.BRACE_CLOSE: str = "}"
        self.BRACKET_OPEN: str = "["
        self.BRACKET_CLOSE: str = "]"
        self.DASH: str = "-"
        self.PERCENT: str = "%"
        self.AMPERSAND: str = "&"
        self.FORWARD_SLASH: str = "/"
        self.BACK_SLASH: str = "\\"
        self.QUESTION: str = "?"
        self.QUOTE: str = "\""
        self.QUOTE_END: str = "\","
        self.COMMENT: str = "//"
        self.INDENT: str = "    "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommonSeps:
        from jsinterop.annotations.JsMethod import JsMethod
        return CommonSeps.instance
# from jsinterop.annotations.JsType import JsType
# from org.allbinary.logic.string.StringMaker import StringMaker
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsProperty import JsProperty


def _CommonSeps_instance() -> object:
    return CommonSeps()

lazy_static(CommonSeps, "instance", _CommonSeps_instance)

