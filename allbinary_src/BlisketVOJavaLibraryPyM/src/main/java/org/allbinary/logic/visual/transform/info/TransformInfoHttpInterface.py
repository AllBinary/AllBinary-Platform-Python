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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


# Java interface
class TransformInfoHttpInterface(TransformInfoInterface):
    

    def getWeblisketSession(self) -> WeblisketSessionInterface:
        raise NotImplementedError()
    

    def getPageContext(self) -> PageContext:
        raise NotImplementedError()
    

    def getPropertiesHashMap(self) -> dict:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface


