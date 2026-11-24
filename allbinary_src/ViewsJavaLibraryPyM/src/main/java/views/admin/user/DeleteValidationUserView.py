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
# package views.admin.user

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.admin.user.UserView import UserView


class DeleteValidationUserView(*java_bases(UserView, ValidationComponentInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.userName: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.username.UserName import UserName
        from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(transformInfoInterface)
        self._init_fields()
        httpServletRequest: HttpServletRequest = self.getPageContext().getRequest()
        hashMap: HashMap = RequestParams(httpServletRequest).toHashMap()
        self.userName = UserName(hashMap).get()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("User Name: " + self.userName, self, self.commonStrings.CONSTRUCTOR)
    

    def isValid(self) -> bool:
        from org.allbinary.business.user.username.UserName import UserName
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if UserName.getInstance().isValid(self.userName) == True:
                self.user = UserEntityFactory.getInstance().getUser(self.userName)
                if self.user is None:
                    return False
            else:
                return False
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        from org.allbinary.business.user.username.UserName import UserName
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            if UserName.getInstance().isValid(self.userName) == True:
                self.user = UserEntityFactory.getInstance().getUser(self.userName)
                if self.user is None:
                    stringBuffer.append("User does not exist.<br />")
            else:
                stringBuffer.append("User Name is not valid.<br />")
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return super().getTransformInfoInterface()
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.user.username.UserName import UserName
# from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
# from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


