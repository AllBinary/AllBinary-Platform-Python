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
# package org.allbinary.logic.string

from __future__ import annotations



class ServletStrings:
    instance: ServletStrings = None

    def _init_fields(self) -> None:
        self.DOPOST: str = "doPost"
        self.DOGET: str = "doGet"
        self.REQUEST_EXCEPTION: str = "Request Failed"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ServletStrings:
        return ServletStrings.instance


ServletStrings.instance = ServletStrings()

