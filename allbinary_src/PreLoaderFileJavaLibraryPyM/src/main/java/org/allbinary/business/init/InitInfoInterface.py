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
# package org.allbinary.business.init

from __future__ import annotations



# Java interface
class InitInfoInterface:
    

    def isTesting(self) -> bool:
        raise NotImplementedError()
    

    def getTesting(self) -> str:
        raise NotImplementedError()
    

    def getTestHtmlPath(self) -> str:
        raise NotImplementedError()
    

    def getMainPath(self) -> str:
        raise NotImplementedError()
    

    def setTesting(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestHtmlPath(self, value: AbPath) -> None:
        raise NotImplementedError()
    

    def setMainPath(self, value: AbPath) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def isTestingValid(self, testing: str) -> bool:
        raise NotImplementedError()
    

    def isTestHtmlPathValid(self, value: AbPath) -> bool:
        raise NotImplementedError()
    

    def isMainPathValid(self, value: AbPath) -> bool:
        raise NotImplementedError()
from org.allbinary.logic.io.path.AbPath import AbPath


