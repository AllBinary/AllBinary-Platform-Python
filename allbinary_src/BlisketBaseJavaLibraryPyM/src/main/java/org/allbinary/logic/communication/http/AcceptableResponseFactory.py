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
# package org.allbinary.logic.communication.http

from __future__ import annotations



class AcceptableResponseFactory:
    instance: AcceptableResponseFactory = None

    def _init_fields(self) -> None:
        self.HTML: AcceptableResponse = AcceptableResponse("text/html", "html", 0)
        self.WML: AcceptableResponse = AcceptableResponse("text/wml", "wml", 1)
        self.VXML: AcceptableResponse = AcceptableResponse("text/vxml", "vxml", 2)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AcceptableResponseFactory:
        return AcceptableResponseFactory.instance
from org.allbinary.logic.communication.http.AcceptableResponse import AcceptableResponse


AcceptableResponseFactory.instance = AcceptableResponseFactory()

