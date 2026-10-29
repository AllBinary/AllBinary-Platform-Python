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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelper import TagHelper


class StoreFrontHelper(TagHelper):

    def _init_fields(self) -> None:
        self.storeFrontInterface: StoreFrontInterface = None
        self.currentLocation: str = None
        self.currentHomeLocation: str = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        storeName: str = hashMap.get(StoreFrontData.getInstance().NAME)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
            self.currentLocation = Replace(CommonSeps.getInstance().SPACE, "%20").all(self.storeFrontInterface.getCurrentHostName() + self.storeFrontInterface.getCurrentHostNamePath())
            self.currentHomeLocation = Replace(CommonSeps.getInstance().SPACE, "%20").all(self.storeFrontInterface.getCurrentHomeHostName() + self.storeFrontInterface.getCurrentHomeHostNamePath())
        else:
            stringUtil: StringUtil = StringUtil.getInstance()
            self.storeFrontInterface = StoreFront()
            self.currentLocation = stringUtil.EMPTY_STRING
            self.currentHomeLocation = stringUtil.EMPTY_STRING
    

    def getCurrentLocation(self) -> str:
        return self.currentLocation
    

    def getCurrentHomeLocation(self) -> str:
        return self.currentHomeLocation
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.string.CommonSeps import CommonSeps


