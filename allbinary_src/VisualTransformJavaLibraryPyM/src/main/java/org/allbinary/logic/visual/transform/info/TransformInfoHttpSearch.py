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

from org.allbinary.logic.visual.transform.info.TransformInfoHttp import TransformInfoHttp


class TransformInfoHttpSearch(TransformInfoHttp):
    

    def __init__(self, searchRequest: SearchRequest) -> None:
        super().__init__(searchRequest.getPropertiesHashMap(), searchRequest.getPageContext())
        if searchRequest.getStoreFront().getName() is not None:
            self.setStoreName(searchRequest.getStoreFront().getName())
        else:
            self.setStoreName(StringUtil.getInstance().EMPTY_STRING)
        dataFileName: str = searchRequest.getXslFile()
        self.setTemplateFile(dataFileName)
    

    # throws Exception
    def getPath(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.URLGLOBALS.getMainPath())
        stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(self.getStoreName())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        return str(stringBuffer)
    

    # throws Exception
    def getTemplateFilePath(self) -> AbPath:
        return AbPath(self.getPath(), self.getTemplateFile())
    

    # throws Exception
    def getObjectConfigFilePath(self) -> AbPath:
        return AbPath(self.getPath(), self.getObjectConfigFile())
    

    # throws Exception
    def getDataFilePath(self) -> AbPath:
        return AbPath(self.getPath(), self.getDataFile())
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.control.search.SearchRequest import SearchRequest
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


