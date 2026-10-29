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
# package views.admin.storefront

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.HttpContextView import HttpContextView


class AddValidationStoreFrontView(HttpContextView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.newStoreFrontInterface: StoreFrontInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.newStoreFrontInterface = StoreFront(self.getPageContext().getRequest())
        if self.newStoreFrontInterface.getName() is None:
            self.newStoreFrontInterface.setName(self.getWeblisketSession().getStoreName())
    

    def isValid(self) -> bool:
        try:
            valid: bool = True
            if self.newStoreFrontInterface.isValid() == False:
                valid = False
            if StoreFrontFactory.getInstance(self.newStoreFrontInterface.getName()) is not None:
                valid = False
            if AbFile.createAbFileFromAbPath(AbPath(self.getStoreViewsPath(), StringUtil.getInstance().EMPTY_STRING)).isFile():
                valid = False
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    # throws Exception
    def getStoreViewsPath(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.URLGLOBALS.getMainPath())
        stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(self.newStoreFrontInterface.getName())
        return str(stringBuffer)
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.newStoreFrontInterface.isValid() == False:
                stringBuffer.append(self.newStoreFrontInterface.validationInfo())
            if StoreFrontFactory.getInstance(self.newStoreFrontInterface.getName()) is not None:
                stringBuffer.append("Store name already used<br/>")
            if AbFile.createAbFileFromAbPath(AbPath(self.getStoreViewsPath(), StringUtil.getInstance().EMPTY_STRING)).isFile():
                stringBuffer.append("Store name clashes with template name<br/>")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def view(self) -> str:
        return self.views.ValidationOnlyTempUtil.getInstance().view(self)
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


