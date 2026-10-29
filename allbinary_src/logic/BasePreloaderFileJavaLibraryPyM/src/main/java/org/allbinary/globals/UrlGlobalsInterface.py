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
# package org.allbinary.globals

from __future__ import annotations



class UrlGlobalsInterface:
    

    # throws Exception
    def getMainPath(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def getTestHtmlPath(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def getWebappPath(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def isTestingMode(self) -> bool:
        return False
from org.allbinary.logic.string.StringUtil import StringUtil


