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

from java.lang.JavaRuntimeStatic import lazy_static


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
        self.PM: str = "pm"
        self._PM: str = ".pm"
        self.KTS: str = "kts"
        self._KTS: str = ".kts"
        self.CBL: str = "cbl"
        self._CBL: str = ".cbl"
        self.COB: str = "cob"
        self._COB: str = ".cob"
        self.F90: str = "f90"
        self._F90: str = ".f90"
        self.F: str = "f"
        self._F: str = ".f"
        self.DART: str = "dart"
        self._DART: str = ".dart"
        self.EX: str = "ex"
        self._EX: str = ".ex"
        self.EXS: str = "exs"
        self._EXS: str = ".exs"
        self.KOTLIN: str = "kotlin"
        self.TYPESCRIPT: str = "typescript"
        self.JAVASCRIPT: str = "javascript"
        self.C_PLUS_PLUS: str = "c++"
        self.PYTHON: str = "python"
        self.C_SHARP: str = "c#"
        self.RUST_NAME: str = "rust"
        self.RUBY: str = "ruby"
        self.PERL: str = "perl"
        self.OBJECT_PASCAL: str = "objectpascal"
        self.OCAML: str = "ocaml"
        self.HASKELL: str = "haskell"
        self.HAXE: str = "haxe"
        self.ERLANG: str = "erlang"
        self.COBOL: str = "cobol"
        self.FORTRAN: str = "fortran"
        self.ELIXIR: str = "elixir"
        self.CPLUSPLUS: str = "cplusplus"
        self.GOLANG: str = "golang"
        self.CSHARP_ALIAS: str = "csharp"
        self.C23: str = "c23"
        self.PASCAL: str = "pascal"
        self.OBJECT_PASCAL_ALIAS: str = "object pascal"
        self.KT_SHORT_NAME: str = "Kt"
        self.TS_SHORT_NAME: str = "Ts"
        self.JS_SHORT_NAME: str = "Js"
        self.CPP_SHORT_NAME: str = "Cpp"
        self.PY_SHORT_NAME: str = "Py"
        self.GO_SHORT_NAME: str = "Go"
        self.CS_SHORT_NAME: str = "Cs"
        self.ADA_SHORT_NAME: str = "Ada"
        self.RUST_SHORT_NAME: str = "Rust"
        self.LUA_SHORT_NAME: str = "Lua"
        self.C_SHORT_NAME: str = "C"
        self.ZIG_SHORT_NAME: str = "Zig"
        self.RB_SHORT_NAME: str = "Rb"
        self.PL_SHORT_NAME: str = "Pl"
        self.PAS_SHORT_NAME: str = "Pas"
        self.ML_SHORT_NAME: str = "Ml"
        self.HS_SHORT_NAME: str = "Hs"
        self.HX_SHORT_NAME: str = "Hx"
        self.ERL_SHORT_NAME: str = "Erl"
        self.CBL_SHORT_NAME: str = "Cbl"
        self.F90_SHORT_NAME: str = "F90"
        self.DART_SHORT_NAME: str = "Dart"
        self.EX_SHORT_NAME: str = "Ex"
        self.UNCRYPTED_EXTENSION: str = self.XML
        self.ENCRYPTED_EXTENSION: str = "abd"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommonDataFileStrings:
        return CommonDataFileStrings.instance


def _CommonDataFileStrings_instance() -> object:
    return CommonDataFileStrings()

lazy_static(CommonDataFileStrings, "instance", _CommonDataFileStrings_instance)

