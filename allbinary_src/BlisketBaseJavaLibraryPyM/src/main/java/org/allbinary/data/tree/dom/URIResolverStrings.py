# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.data.tree.dom

from __future__ import annotations



class URIResolverStrings:
    instance: URIResolverStrings = None

    def _init_fields(self) -> None:
        self.IMPORT_URL: str = "/{import url}"
        self.ATTEMPT: str = "attempt to use xsl:import: href="
        self.BASE: str = "\nBase= "
        self.NEW_PATH: str = "\nNew path= "
        self.NOTE: str = "\nNote: "
        self.URL_GLOBAL: str = " is a urlglobal"
        self.REQUIRED_EXTENSION: str = "\nRequired Extension: "
        self.RESOLVE: str = "resolve"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> URIResolverStrings:
        return URIResolverStrings.instance


URIResolverStrings.instance = URIResolverStrings()

