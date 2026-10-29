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
# package views.generic.user

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class UpdateValidationUserView(HttpStoreComponentView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.user: UserInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.user = NewUserFactory.getInstance(transformInfoInterface)
    

    def isValid(self) -> bool:
        try:
            if UserEntityFactory.getInstance().getUser(self.user.getUserName()) is None:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("User does not exist", self, self.commonStrings.IS_VALID)
                return False
            if self.user.isValid() == False:
                return False
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            if UserEntityFactory.getInstance().getUser(self.user.getUserName()) is None:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("User does not exist", self, "validationInfo()")
                stringBuffer.append("Unable to update user that does not exist.<br />")
            if self.user.isValid() == False:
                stringBuffer.append(self.user.validationInfo())
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def view(self) -> str:
        return self.views.ValidationOnlyTempUtil.getInstance().view(self)
from org.allbinary.business.user.NewUserFactory import NewUserFactory
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


