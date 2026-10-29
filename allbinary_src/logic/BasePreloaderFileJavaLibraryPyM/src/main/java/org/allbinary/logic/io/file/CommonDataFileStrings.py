# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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
# package org.allbinary.logic.io.file

from __future__ import annotations



class CommonDataFileStrings:
    instance: CommonDataFileStrings = None

    def _init_fields(self) -> None:
        self.XML: str = "xml"
        self._XML: str = ".xml"
        self.JSON: str = "json"
        self._JSON: str = ".json"
        self.XSL: str = "xsl"
        self._XSL: str = ".xsl"
        self.JAVA: str = "java"
        self._JAVA: str = ".java"
        self.KT: str = "kt"
        self._KT: str = ".kt"
        self.TS: str = "ts"
        self._TS: str = ".ts"
        self.JS: str = "js"
        self._JS: str = ".js"
        self.CPP: str = "cpp"
        self._CPP: str = ".cpp"
        self.H: str = "h"
        self._H: str = ".h"
        self.PY: str = "py"
        self._PY: str = ".py"
        self.GO: str = "go"
        self._GO: str = ".go"
        self.CS: str = "cs"
        self._CS: str = ".cs"
        self.ADB: str = "adb"
        self._ADB: str = ".adb"
        self.ADS: str = "ads"
        self._ADS: str = ".ads"
        self.ADA: str = "ada"
        self._ADA: str = ".ada"
        self.RUST: str = "rs"
        self._RUST: str = ".rs"
        self.C: str = "c"
        self._C: str = ".c"
        self.CSHARP: str = "cs"
        self._CSHARP: str = ".cs"
        self.ERL: str = "erl"
        self._ERL: str = ".erl"
        self.HS: str = "hs"
        self._HS: str = ".hs"
        self.HX: str = "hx"
        self._HX: str = ".hx"
        self.LUA: str = "lua"
        self._LUA: str = ".lua"
        self.PAS: str = "pas"
        self._PAS: str = ".pas"
        self.ML: str = "ml"
        self._ML: str = ".ml"
        self.PL: str = "pl"
        self._PL: str = ".pl"
        self.RB: str = "rb"
        self._RB: str = ".rb"
        self.ZIG: str = "zig"
        self._ZIG: str = ".zig"
        self.UNCRYPTED_EXTENSION: str = self.XML
        self.ENCRYPTED_EXTENSION: str = "abd"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommonDataFileStrings:
        return CommonDataFileStrings.instance


CommonDataFileStrings.instance = CommonDataFileStrings()

