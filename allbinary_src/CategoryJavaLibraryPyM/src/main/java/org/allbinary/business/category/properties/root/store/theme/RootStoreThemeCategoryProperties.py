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
# package org.allbinary.business.category.properties.root.store.theme

from __future__ import annotations

from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties


class RootStoreThemeCategoryProperties(RootStoreCategoryProperties):

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, abPath: AbPath) -> None:
        super().__init__(transformInfoInterface, abPath)
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, node: Node) -> None:
        super().__init__(transformInfoInterface, node)
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, categoryPropertiesHashMap: dict) -> None:
        super().__init__(transformInfoInterface, categoryPropertiesHashMap)
    

    # throws Exception
    def initPath(self) -> None:
        transformInfoHttpStoreInterface: TransformInfoHttpStoreInterface = self.transformInfoInterface
        storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(transformInfoHttpStoreInterface.getStoreName())
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(storeFrontInterface.getName())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().THEMEPATH)
        abPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        httpServletRequest: HttpServletRequest = transformInfoHttpStoreInterface.getPageContext().getRequest()
        self.webAppAbPath = AbPath(str(httpServletRequest.getContextPath()) + str(abPath), StringUtil.getInstance().EMPTY_STRING)
        self.setRootFilePath(AbPath(str(self.URLGLOBALS.getMainPath()) + str(abPath), StringUtil.getInstance().EMPTY_STRING))
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.transform.info.TransformInfoHttpStoreInterface import TransformInfoHttpStoreInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Node import Node


